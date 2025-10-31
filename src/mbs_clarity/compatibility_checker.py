"""
MBS Code Compatibility Checker

This module provides isolated functionality for checking compatibility between MBS codes.
It implements a simple "Yay or Nay" compatibility assessment based on mutual exclusions
and mandatory dependencies.

This module is completely isolated and does not modify any existing functionality.
"""

from typing import Dict, List, Any
from .db import fetch_item_aggregate


def check_mbs_compatibility(codes: List[str]) -> Dict[str, Any]:
    """
    Check compatibility of a list of MBS codes.

    Args:
        codes: List of MBS item numbers to check

    Returns:
        Dictionary with:
        - decision: "YAY" or "NAY"
        - reason: Human-readable explanation
        - failed_check: Check ID that failed (P1, C1, C2, C3, C4) or None if passed
        - details: Additional details about the failure
    """
    if not codes:
        return {
            "decision": "NAY",
            "reason": "No codes provided for compatibility check.",
            "failed_check": "P1",
            "details": None,
        }

    # Normalize codes (strip whitespace)
    normalized_codes_raw = []
    for code in codes:
        code_clean = code.strip()
        if code_clean:
            normalized_codes_raw.append(code_clean)

    if not normalized_codes_raw:
        return {
            "decision": "NAY",
            "reason": "No valid codes provided for compatibility check.",
            "failed_check": "P1",
            "details": None,
        }

    # Check P1: All codes are valid MBS item numbers
    invalid_codes = []
    items_data = {}
    # Track original counts BEFORE deduplication (for C4 check)
    original_code_counts = {}
    for code in normalized_codes_raw:
        original_code_counts[code] = original_code_counts.get(code, 0) + 1

    # Now deduplicate for processing
    normalized_codes = []
    seen = set()
    for code in normalized_codes_raw:
        if code not in seen:
            normalized_codes.append(code)
            seen.add(code)

    for code in normalized_codes:
        try:
            item_data = fetch_item_aggregate(code)
            if not item_data or not item_data[0]:
                invalid_codes.append(code)
            else:
                item_row, rel_rows, con_rows = item_data
                items_data[code] = {
                    "item": item_row,
                    "relations": [
                        {
                            "relation_type": rel[0],
                            "target_item_num": rel[1],
                            "detail": rel[2],
                        }
                        for rel in rel_rows
                    ],
                    "constraints": [
                        {"constraint_type": con[0], "value": con[1]} for con in con_rows
                    ],
                    "group_code": (
                        item_row[2] if item_row else None
                    ),  # group_code is at index 2
                }
        except Exception:
            invalid_codes.append(code)

    if invalid_codes:
        return {
            "decision": "NAY",
            "reason": f"System Error: The code{'s' if len(invalid_codes) > 1 else ''} {', '.join(invalid_codes)} {'are' if len(invalid_codes) > 1 else 'is'} not a recognised MBS item number{'s' if len(invalid_codes) > 1 else ''}.",
            "failed_check": "P1",
            "details": {"invalid_codes": invalid_codes},
        }

    # Check C4: No duplicate codes when limited to one unit per service occasion
    # Use original_code_counts to detect duplicates BEFORE deduplication
    duplicate_violations = []
    for code, count in original_code_counts.items():
        if count > 1:
            item_info = items_data[code]
            # Check if this code has constraints that limit it to one per service occasion
            has_limit = False
            limit_value = None

            for constraint in item_info["constraints"]:
                constraint_type = constraint["constraint_type"]
                value = constraint["value"]

                if constraint_type == "same_occasion":
                    # Same occasion means only 1 per service occasion
                    has_limit = True
                    limit_value = "1 per service occasion"
                    break
                elif constraint_type == "max_per_window":
                    # Check if value indicates only 1 allowed per occasion
                    if "/occasion" in value.lower() or value == "1/occasion":
                        has_limit = True
                        limit_value = value
                        break

            if has_limit:
                duplicate_violations.append(
                    {"code": code, "count": count, "limit": limit_value}
                )

    if duplicate_violations:
        viol = duplicate_violations[0]
        return {
            "decision": "NAY",
            "reason": f"Duplicate Limit: Item {viol['code']} is limited to {viol['limit']}. It was submitted {viol['count']} time{'s' if viol['count'] > 1 else ''}.",
            "failed_check": "C4",
            "details": {"violations": duplicate_violations},
        }

    # Check C3: Solo-only codes (codes that must be billed alone)
    solo_violations = []
    for code, item_info in items_data.items():
        # Check for constraints that indicate solo-only
        for constraint in item_info["constraints"]:
            constraint_type = constraint["constraint_type"]

            # If it has same_occasion and there are other codes, it might be solo
            # But we need to check if there's explicit solo-only language
            # For now, we'll check if there are exclusion relations that exclude everything else
            # or if there's a generic_excludes relation

            if constraint_type == "same_occasion":
                # Check if this code has generic_excludes (excludes all other items)
                has_generic_exclude = any(
                    rel["relation_type"] == "generic_excludes"
                    for rel in item_info["relations"]
                )

                if has_generic_exclude and len(normalized_codes) > 1:
                    solo_violations.append(code)
                    break

    # Also check for codes with generic_excludes when multiple codes are present
    for code, item_info in items_data.items():
        has_generic_exclude = any(
            rel["relation_type"] == "generic_excludes" for rel in item_info["relations"]
        )

        if has_generic_exclude and len(normalized_codes) > 1:
            if code not in solo_violations:
                solo_violations.append(code)

    if solo_violations:
        solo_code = solo_violations[0]
        item_info = items_data[solo_code]
        item_desc = (
            item_info["item"][4]
            if item_info["item"] and len(item_info["item"]) > 4
            else solo_code
        )
        return {
            "decision": "NAY",
            "reason": f"Co-Claiming Violation: Item {solo_code} has a rule that it must be billed alone. It cannot be billed with the other codes submitted.",
            "failed_check": "C3",
            "details": {"solo_codes": solo_violations},
        }

    # Check C1: No mutual exclusions
    exclusion_violations = []
    seen_pairs = set()  # Track pairs to avoid duplicates

    # Check direct exclusions
    for code1 in normalized_codes:
        item_info1 = items_data[code1]

        # Check excludes relations
        for rel in item_info1["relations"]:
            if rel["relation_type"] == "excludes" and rel["target_item_num"]:
                target = rel["target_item_num"]
                if target in normalized_codes and target != code1:
                    # Create canonical pair to avoid duplicates
                    pair = tuple(sorted([code1, target]))
                    if pair not in seen_pairs:
                        seen_pairs.add(pair)
                        exclusion_violations.append(
                            {
                                "code1": code1,
                                "code2": target,
                                "type": "mutual_exclusion",
                                "detail": rel.get("detail", ""),
                            }
                        )

        # Check same_day_excludes (applies since we're checking same claim)
        for rel in item_info1["relations"]:
            if rel["relation_type"] == "same_day_excludes" and rel["target_item_num"]:
                target = rel["target_item_num"]
                if target in normalized_codes and target != code1:
                    pair = tuple(sorted([code1, target]))
                    if pair not in seen_pairs:
                        seen_pairs.add(pair)
                        exclusion_violations.append(
                            {
                                "code1": code1,
                                "code2": target,
                                "type": "same_day_exclusion",
                                "detail": rel.get("detail", ""),
                            }
                        )

        # Check group conflicts (same group_code means exclusion group)
        group_code1 = item_info1["group_code"]
        if group_code1:
            for code2 in normalized_codes:
                if code1 != code2:
                    item_info2 = items_data[code2]
                    group_code2 = item_info2["group_code"]

                    if group_code1 == group_code2:
                        pair = tuple(sorted([code1, code2]))
                        if pair not in seen_pairs:
                            seen_pairs.add(pair)
                            # Same group code means they're mutually exclusive
                            exclusion_violations.append(
                                {
                                    "code1": code1,
                                    "code2": code2,
                                    "type": "group_conflict",
                                    "detail": f"Both codes are in Group {group_code1}",
                                }
                            )

    if exclusion_violations:
        viol = exclusion_violations[0]
        code1_desc = (
            items_data[viol["code1"]]["item"][4]
            if items_data[viol["code1"]]["item"]
            and len(items_data[viol["code1"]]["item"]) > 4
            else viol["code1"]
        )
        code2_desc = (
            items_data[viol["code2"]]["item"][4]
            if items_data[viol["code2"]]["item"]
            and len(items_data[viol["code2"]]["item"]) > 4
            else viol["code2"]
        )

        if viol["type"] == "group_conflict":
            reason = f"Conflict: Only one Group {items_data[viol['code1']]['group_code']} attendance item is payable. You have submitted both {viol['code1']} and {viol['code2']} which are in the same exclusion group."
        elif viol["type"] == "same_day_exclusion":
            reason = f"Conflict: Item {viol['code1']} is mutually exclusive with {viol['code2']} on the same day for the same patient on the same day."
        else:
            reason = f"Conflict: Item {viol['code1']} is mutually exclusive with {viol['code2']} on the same day for the same patient on the same day."

        return {
            "decision": "NAY",
            "reason": reason,
            "failed_check": "C1",
            "details": {"violations": exclusion_violations},
        }

    # Check C2: Mandatory dependencies (prerequisites)
    missing_dependencies = []

    for code in normalized_codes:
        item_info = items_data[code]

        # Check for prerequisite relations
        for rel in item_info["relations"]:
            if rel["relation_type"] == "prerequisite" and rel["target_item_num"]:
                required = rel["target_item_num"]

                # Check if the required code is in the submitted list
                if required not in normalized_codes:
                    missing_dependencies.append(
                        {
                            "code": code,
                            "required_code": required,
                            "detail": rel.get("detail", ""),
                        }
                    )

    if missing_dependencies:
        dep = missing_dependencies[0]
        # Build a descriptive reason
        reason = f"Missing Dependency: Item {dep['code']} requires a service to which item {dep['required_code']} applies to be claimed, but none was submitted."

        return {
            "decision": "NAY",
            "reason": reason,
            "failed_check": "C2",
            "details": {"missing_dependencies": missing_dependencies},
        }

    # All checks passed!
    return {
        "decision": "YAY",
        "reason": "Compatibility Passed: Based on MBS code rules, the submitted items are compatible for claiming together. (Note: External factors like patient history or provider type are not checked).",
        "failed_check": None,
        "details": None,
    }
