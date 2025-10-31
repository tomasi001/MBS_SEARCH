#!/usr/bin/env python3
"""
Generate 100 comprehensive test cases for MBS compatibility checker.
Based on real MBS data with difficult edge cases.
"""

import sqlite3
import json
from typing import List, Dict, Any, Tuple


def get_test_data() -> Dict[str, Any]:
    """Extract real test data from database."""
    conn = sqlite3.connect("mbs.db")
    cursor = conn.cursor()

    data = {
        "groups": [],
        "exclusions": [],
        "same_day_excludes": [],
        "prereqs": [],
        "solo_codes": [],
        "same_occasion": [],
        "max_per_window": [],
        "valid_codes": [],
        "invalid_codes": ["X999", "INVALID", "99999", "ABCD", "Z9999"],
    }

    # Group conflicts - codes in same exclusion group
    cursor.execute(
        """
        SELECT group_code, GROUP_CONCAT(item_num) as codes
        FROM items 
        WHERE group_code IS NOT NULL 
        GROUP BY group_code 
        HAVING COUNT(item_num) >= 2
        ORDER BY group_code
    """
    )
    for row in cursor.fetchall():
        codes = row[1].split(",")
        if len(codes) >= 2:
            data["groups"].append({"group": row[0], "codes": codes})

    # Direct exclusions
    cursor.execute(
        """
        SELECT DISTINCT r.item_num, r.target_item_num
        FROM relations r
        JOIN items i1 ON r.item_num = i1.item_num
        JOIN items i2 ON r.target_item_num = i2.item_num
        WHERE r.relation_type = 'excludes' AND r.target_item_num IS NOT NULL
    """
    )
    for row in cursor.fetchall():
        data["exclusions"].append({"from": row[0], "to": row[1]})

    # Same day exclusions
    cursor.execute(
        """
        SELECT DISTINCT r.item_num, r.target_item_num
        FROM relations r
        WHERE r.relation_type = 'same_day_excludes' AND r.target_item_num IS NOT NULL
    """
    )
    for row in cursor.fetchall():
        data["same_day_excludes"].append({"from": row[0], "to": row[1]})

    # Prerequisites - include all prerequisites where source exists
    # (Target may not exist, but we still want to test C2 logic)
    cursor.execute(
        """
        SELECT DISTINCT r.item_num, r.target_item_num
        FROM relations r
        JOIN items i1 ON r.item_num = i1.item_num
        WHERE r.relation_type = 'prerequisite' AND r.target_item_num IS NOT NULL
    """
    )
    for row in cursor.fetchall():
        data["prereqs"].append({"code": row[0], "requires": row[1]})

    # Solo-only codes (generic_excludes)
    cursor.execute(
        """
        SELECT DISTINCT r.item_num
        FROM relations r
        JOIN items i ON r.item_num = i.item_num
        WHERE r.relation_type = 'generic_excludes'
    """
    )
    data["solo_codes"] = [row[0] for row in cursor.fetchall()]

    # Same occasion constraints
    cursor.execute(
        """
        SELECT DISTINCT c.item_num
        FROM constraints c
        JOIN items i ON c.item_num = i.item_num
        WHERE c.constraint_type = 'same_occasion'
    """
    )
    data["same_occasion"] = [row[0] for row in cursor.fetchall()]

    # Max per window constraints
    cursor.execute(
        """
        SELECT DISTINCT c.item_num, c.value
        FROM constraints c
        JOIN items i ON c.item_num = i.item_num
        WHERE c.constraint_type = 'max_per_window'
        AND (c.value LIKE '%occasion%' OR c.value LIKE '%1/%')
    """
    )
    for row in cursor.fetchall():
        data["max_per_window"].append({"code": row[0], "limit": row[1]})

    # Valid codes (for YAY tests) - codes that are compatible with many others
    cursor.execute(
        """
        SELECT item_num FROM items 
        WHERE item_num NOT IN (
            SELECT DISTINCT item_num FROM relations 
            WHERE relation_type = 'generic_excludes'
        )
        AND item_num NOT IN (
            SELECT DISTINCT item_num FROM constraints 
            WHERE constraint_type = 'same_occasion'
        )
        LIMIT 50
    """
    )
    data["valid_codes"] = [row[0] for row in cursor.fetchall()]

    conn.close()
    return data


def generate_tests(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate 100 comprehensive test cases."""
    tests = []
    test_num = 1

    # ===== P1: Invalid Item Numbers (20 tests) =====

    # Single invalid code
    tests.append(
        {
            "test_id": test_num,
            "category": "P1",
            "name": "Single invalid code",
            "codes": ["X999"],
            "expected": "NAY",
            "expected_check": "P1",
            "difficulty": "basic",
        }
    )
    test_num += 1

    # Multiple invalid codes
    for i, invalid in enumerate(data["invalid_codes"][:5]):
        tests.append(
            {
                "test_id": test_num,
                "category": "P1",
                "name": f"Multiple invalid codes - test {i+1}",
                "codes": [
                    invalid,
                    (
                        data["invalid_codes"][i + 1]
                        if i + 1 < len(data["invalid_codes"])
                        else "X999"
                    ),
                ],
                "expected": "NAY",
                "expected_check": "P1",
                "difficulty": "basic",
            }
        )
        test_num += 1

    # Invalid mixed with valid
    tests.append(
        {
            "test_id": test_num,
            "category": "P1",
            "name": "Invalid code mixed with valid code",
            "codes": ["X999", "3"],
            "expected": "NAY",
            "expected_check": "P1",
            "difficulty": "basic",
        }
    )
    test_num += 1

    # Empty input
    tests.append(
        {
            "test_id": test_num,
            "category": "P1",
            "name": "Empty codes array",
            "codes": [],
            "expected": "NAY",
            "expected_check": "P1",
            "difficulty": "basic",
        }
    )
    test_num += 1

    # Whitespace-only codes
    tests.append(
        {
            "test_id": test_num,
            "category": "P1",
            "name": "Whitespace-only codes",
            "codes": ["   ", "  ", ""],
            "expected": "NAY",
            "expected_check": "P1",
            "difficulty": "edge_case",
        }
    )
    test_num += 1

    # Invalid numeric codes
    tests.extend(
        [
            {
                "test_id": test_num + i,
                "category": "P1",
                "name": f"Invalid numeric code {999999 + i}",
                "codes": [str(999999 + i)],
                "expected": "NAY",
                "expected_check": "P1",
                "difficulty": "edge_case",
            }
            for i in range(5)
        ]
    )
    test_num += 5

    # ===== C1: Mutual Exclusions (25 tests) =====

    # Group conflicts - 2 codes same group
    for i, group in enumerate(data["groups"][:10]):
        if len(group["codes"]) >= 2:
            tests.append(
                {
                    "test_id": test_num,
                    "category": "C1",
                    "name": f'Group conflict - {group["group"]} ({group["codes"][0]} and {group["codes"][1]})',
                    "codes": [group["codes"][0], group["codes"][1]],
                    "expected": "NAY",
                    "expected_check": "C1",
                    "difficulty": "moderate",
                    "expected_reason_contains": "Group " + group["group"],
                }
            )
            test_num += 1

    # Group conflicts - 3+ codes same group
    for i, group in enumerate(data["groups"][:5]):
        if len(group["codes"]) >= 3:
            tests.append(
                {
                    "test_id": test_num,
                    "category": "C1",
                    "name": f'Group conflict - multiple codes in {group["group"]}',
                    "codes": group["codes"][:3],
                    "expected": "NAY",
                    "expected_check": "C1",
                    "difficulty": "moderate",
                }
            )
            test_num += 1

    # Direct exclusions
    for i, excl in enumerate(data["exclusions"][:10]):
        tests.append(
            {
                "test_id": test_num,
                "category": "C1",
                "name": f'Direct exclusion ({excl["from"]} excludes {excl["to"]})',
                "codes": [excl["from"], excl["to"]],
                "expected": "NAY",
                "expected_check": "C1",
                "difficulty": "moderate",
            }
        )
        test_num += 1

    # Bidirectional exclusion (if A excludes B, and B excludes A)
    for excl1 in data["exclusions"][:5]:
        for excl2 in data["exclusions"][:5]:
            if excl1["from"] == excl2["to"] and excl1["to"] == excl2["from"]:
                tests.append(
                    {
                        "test_id": test_num,
                        "category": "C1",
                        "name": f'Bidirectional exclusion ({excl1["from"]} <-> {excl1["to"]})',
                        "codes": [excl1["from"], excl1["to"]],
                        "expected": "NAY",
                        "expected_check": "C1",
                        "difficulty": "advanced",
                    }
                )
                test_num += 1
                break

    # Same day exclusions
    for i, excl in enumerate(data["same_day_excludes"][:5]):
        tests.append(
            {
                "test_id": test_num,
                "category": "C1",
                "name": f'Same day exclusion ({excl["from"]} same_day_excludes {excl["to"]})',
                "codes": [excl["from"], excl["to"]],
                "expected": "NAY",
                "expected_check": "C1",
                "difficulty": "moderate",
            }
        )
        test_num += 1

    # ===== C2: Mandatory Dependencies (15 tests) =====

    # Missing prerequisite tests - test all prerequisites from data
    # Note: Some prerequisites may reference codes that don't exist (like "45" for 45 minutes)
    # but we still test the C2 logic path - if the code exists and has a prerequisite,
    # it should be detected as missing
    conn_temp = sqlite3.connect("mbs.db")
    cursor_temp = conn_temp.cursor()

    c2_added = 0
    for prereq in data["prereqs"]:
        if c2_added >= 15:
            break
        # Check if source code exists
        cursor_temp.execute(
            "SELECT item_num FROM items WHERE item_num = ?", (prereq["code"],)
        )
        source_exists = cursor_temp.fetchone()

        if source_exists:  # Only test if source code exists
            tests.append(
                {
                    "test_id": test_num,
                    "category": "C2",
                    "name": f'Missing prerequisite ({prereq["code"]} requires {prereq["requires"]})',
                    "codes": [prereq["code"]],
                    "expected": "NAY",
                    "expected_check": "C2",  # Should detect missing prerequisite
                    "difficulty": "moderate",
                    "expected_reason_contains": prereq["requires"],
                }
            )
            test_num += 1
            c2_added += 1

    conn_temp.close()

    # ===== C3: Solo-Only Codes (10 tests) =====

    # Solo code alone (should pass)
    for i, solo in enumerate(data["solo_codes"][:5]):
        tests.append(
            {
                "test_id": test_num,
                "category": "C3",
                "name": f"Solo-only code alone ({solo})",
                "codes": [solo],
                "expected": "YAY",
                "expected_check": None,
                "difficulty": "basic",
            }
        )
        test_num += 1

    # Solo code with other code (should fail)
    for i, solo in enumerate(data["solo_codes"][:5]):
        other = data["valid_codes"][i] if i < len(data["valid_codes"]) else "3"
        tests.append(
            {
                "test_id": test_num,
                "category": "C3",
                "name": f"Solo-only code with other ({solo} with {other})",
                "codes": [solo, other],
                "expected": "NAY",
                "expected_check": "C3",
                "difficulty": "moderate",
            }
        )
        test_num += 1

    # ===== C4: Duplicate Limits (15 tests) =====

    # Duplicate same_occasion code
    for i, code in enumerate(data["same_occasion"][:10]):
        tests.append(
            {
                "test_id": test_num,
                "category": "C4",
                "name": f"Duplicate same_occasion code ({code} x2)",
                "codes": [code, code],
                "expected": "NAY",
                "expected_check": "C4",
                "difficulty": "moderate",
            }
        )
        test_num += 1

    # Multiple duplicates
    for i, code in enumerate(data["same_occasion"][:5]):
        tests.append(
            {
                "test_id": test_num,
                "category": "C4",
                "name": f"Multiple duplicates ({code} x3)",
                "codes": [code, code, code],
                "expected": "NAY",
                "expected_check": "C4",
                "difficulty": "advanced",
            }
        )
        test_num += 1

    # ===== YAY: Success Cases (15 tests) =====

    # Single valid code
    for i, code in enumerate(data["valid_codes"][:5]):
        tests.append(
            {
                "test_id": test_num,
                "category": "YAY",
                "name": f"Single valid code ({code})",
                "codes": [code],
                "expected": "YAY",
                "expected_check": None,
                "difficulty": "basic",
            }
        )
        test_num += 1

    # Compatible pairs (different groups, no exclusions)
    # Find codes that are definitely compatible by checking actual database relationships
    compatible_pairs = []
    conn_pair = sqlite3.connect("mbs.db")
    cursor_pair = conn_pair.cursor()

    checked_pairs = set()
    for code1 in data["valid_codes"][:50]:
        if len(compatible_pairs) >= 10:
            break
        for code2 in data["valid_codes"][:50]:
            if len(compatible_pairs) >= 10:
                break
            if code1 >= code2:
                continue

            pair_key = tuple(sorted([code1, code2]))
            if pair_key in checked_pairs:
                continue
            checked_pairs.add(pair_key)

            # Check if they're in the same group
            cursor_pair.execute(
                """
                SELECT i1.group_code, i2.group_code
                FROM items i1, items i2
                WHERE i1.item_num = ? AND i2.item_num = ?
            """,
                (code1, code2),
            )
            group_row = cursor_pair.fetchone()
            if group_row and group_row[0] and group_row[0] == group_row[1]:
                continue  # Same group - not compatible

            # Check for direct exclusions
            cursor_pair.execute(
                """
                SELECT 1 FROM relations
                WHERE ((item_num = ? AND target_item_num = ?)
                   OR (item_num = ? AND target_item_num = ?))
                AND relation_type IN ('excludes', 'same_day_excludes', 'generic_excludes')
                LIMIT 1
            """,
                (code1, code2, code2, code1),
            )
            if cursor_pair.fetchone():
                continue  # Has exclusion - not compatible

            # Check if either is solo-only (generic_excludes)
            cursor_pair.execute(
                """
                SELECT 1 FROM relations
                WHERE (item_num = ? OR item_num = ?)
                AND relation_type = 'generic_excludes'
                LIMIT 1
            """,
                (code1, code2),
            )
            if cursor_pair.fetchone():
                continue  # One is solo-only - not compatible

            # This pair is compatible!
            compatible_pairs.append([code1, code2])

    conn_pair.close()

    for i, pair in enumerate(compatible_pairs):
        tests.append(
            {
                "test_id": test_num,
                "category": "YAY",
                "name": f"Compatible codes ({pair[0]} and {pair[1]})",
                "codes": pair,
                "expected": "YAY",
                "expected_check": None,
                "difficulty": "moderate",
            }
        )
        test_num += 1

    # Balance test distribution - reduce YAY if needed, ensure all categories covered
    category_counts = {}
    for test in tests:
        cat = test["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1

    # If C2 tests weren't generated (no valid prerequisites), add placeholder tests
    if category_counts.get("C2", 0) == 0:
        # Add C2 tests that will fail with P1 (prerequisite target doesn't exist)
        # This still tests C2 logic path
        for i, prereq in enumerate(data["prereqs"][:15]):
            if len(tests) >= 100:
                break
            tests.append(
                {
                    "test_id": len(tests) + 1,
                    "category": "C2",
                    "name": f'Missing prerequisite - target may not exist ({prereq["code"]} requires {prereq["requires"]})',
                    "codes": [prereq["code"]],
                    "expected": "NAY",
                    "expected_check": "C2",  # Or P1 if target doesn't exist - both valid
                    "difficulty": "advanced",
                }
            )

    # Ensure we have exactly 100 tests
    while len(tests) < 100:
        # Add more YAY tests with valid codes
        remaining = 100 - len(tests)
        for i in range(min(remaining, len(data["valid_codes"]))):
            if len(tests) >= 100:
                break
            code = data["valid_codes"][len(tests) % len(data["valid_codes"])]
            tests.append(
                {
                    "test_id": len(tests) + 1,
                    "category": "YAY",
                    "name": f"Valid code {i+1} ({code})",
                    "codes": [code],
                    "expected": "YAY",
                    "expected_check": None,
                    "difficulty": "basic",
                }
            )

    # Re-number tests
    for i, test in enumerate(tests[:100], 1):
        test["test_id"] = i

    return tests[:100]  # Ensure exactly 100


def main():
    """Generate and save test cases."""
    print("Extracting test data from database...")
    data = get_test_data()

    print("Generating 100 test cases...")
    tests = generate_tests(data)

    # Save as JSON
    with open("compatibility_test_cases.json", "w") as f:
        json.dump(tests, f, indent=2)

    # Generate Python test file
    with open("test_compatibility_comprehensive.py", "w") as f:
        f.write(
            '''#!/usr/bin/env python3
"""
Comprehensive test suite for MBS compatibility checker.
Generated from real MBS data - 100 test cases.
"""

import pytest
import json
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mbs_clarity.compatibility_checker import check_mbs_compatibility


# Load test cases
with open('compatibility_test_cases.json', 'r') as f:
    TEST_CASES = json.load(f)


class TestCompatibilityChecker:
    """Comprehensive test suite for compatibility checker."""
    
'''
        )

        # Group tests by category
        categories = {}
        for test in tests:
            cat = test["category"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(test)

        for category, cat_tests in categories.items():
            f.write(
                f"\n    # ===== {category} Tests ({len(cat_tests)} tests) =====\n\n"
            )

            for test in cat_tests:
                test_name = (
                    test["name"]
                    .replace(" ", "_")
                    .replace("-", "_")
                    .replace("(", "")
                    .replace(")", "")
                    .replace(",", "")
                )
                codes_repr = test["codes"]

                f.write(
                    f'''    def test_{category.lower()}_{test['test_id']:03d}_{test_name}(self):
        """{test['name']} (Difficulty: {test['difficulty']})"""
        codes = {codes_repr}
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == '{test['expected']}', \\
            f"Expected {test['expected']}, got {{result['decision']}}. Reason: {{result['reason']}}"
        
        assert result['failed_check'] == {repr(test['expected_check'])}, \\
            f"Expected failed_check {repr(test['expected_check'])}, got {{result['failed_check']}}"
        
'''
                )

        f.write(
            """
if __name__ == '__main__':
    pytest.main([__file__, '-v'])
"""
        )

    # Print summary
    print(f"\n✅ Generated 100 test cases:")
    category_counts = {}
    for test in tests:
        cat = test["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1

    for cat, count in sorted(category_counts.items()):
        print(f"  - {cat}: {count} tests")

    print(f"\n📁 Files created:")
    print(f"  - compatibility_test_cases.json")
    print(f"  - test_compatibility_comprehensive.py")
    print(f"\n🧪 Run tests with: pytest test_compatibility_comprehensive.py -v")


if __name__ == "__main__":
    main()
