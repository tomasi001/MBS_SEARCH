#!/usr/bin/env python3
"""
Generate 1000 comprehensive test cases for MBS compatibility checker.
Based on real MBS data with actual code combinations.
"""

import sqlite3
import json
from typing import List, Dict, Any
from collections import defaultdict


def get_comprehensive_test_data() -> Dict[str, Any]:
    """Extract comprehensive test data from database."""
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
        "all_codes": [],  # All valid codes for combinations
    }

    # Get all item numbers
    cursor.execute("SELECT DISTINCT item_num FROM items ORDER BY item_num")
    data["all_codes"] = [row[0] for row in cursor.fetchall()]

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

    # Prerequisites
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
    """
    )
    data["valid_codes"] = [row[0] for row in cursor.fetchall()]

    conn.close()
    return data


def find_compatible_pairs(
    data: Dict[str, Any], max_pairs: int = 200
) -> List[List[str]]:
    """Find truly compatible code pairs by checking database."""
    compatible_pairs = []
    conn = sqlite3.connect("mbs.db")
    cursor = conn.cursor()

    checked_pairs = set()
    # Use a larger sample to find more compatible pairs
    for code1 in data["all_codes"][:200]:
        if len(compatible_pairs) >= max_pairs:
            break
        for code2 in data["all_codes"][:200]:
            if len(compatible_pairs) >= max_pairs:
                break
            if code1 >= code2:
                continue

            pair_key = tuple(sorted([code1, code2]))
            if pair_key in checked_pairs:
                continue
            checked_pairs.add(pair_key)

            # Check if they're in the same group
            cursor.execute(
                """
                SELECT i1.group_code, i2.group_code
                FROM items i1, items i2
                WHERE i1.item_num = ? AND i2.item_num = ?
            """,
                (code1, code2),
            )
            group_row = cursor.fetchone()
            if group_row and group_row[0] and group_row[0] == group_row[1]:
                continue

            # Check for direct exclusions
            cursor.execute(
                """
                SELECT 1 FROM relations
                WHERE ((item_num = ? AND target_item_num = ?)
                   OR (item_num = ? AND target_item_num = ?))
                AND relation_type IN ('excludes', 'same_day_excludes', 'generic_excludes')
                LIMIT 1
            """,
                (code1, code2, code2, code1),
            )
            if cursor.fetchone():
                continue

            # Check if either is solo-only
            cursor.execute(
                """
                SELECT 1 FROM relations
                WHERE (item_num = ? OR item_num = ?)
                AND relation_type = 'generic_excludes'
                LIMIT 1
            """,
                (code1, code2),
            )
            if cursor.fetchone():
                continue

            compatible_pairs.append([code1, code2])

    conn.close()
    return compatible_pairs


def generate_1000_tests(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate 1000 comprehensive test cases."""
    tests = []
    test_num = 1

    # Target distribution:
    # P1: 100 (10%) - Invalid codes
    # C1: 300 (30%) - Exclusions/conflicts
    # C2: 150 (15%) - Prerequisites
    # C3: 100 (10%) - Solo-only
    # C4: 100 (10%) - Duplicates
    # YAY: 250 (25%) - Success cases

    # ===== P1: Invalid Item Numbers (100 tests) =====
    print("Generating P1 tests (100)...")

    # Single invalid codes - 20 tests
    for i, invalid in enumerate(data["invalid_codes"]):
        if test_num > 100:
            break
        tests.append(
            {
                "test_id": test_num,
                "category": "P1",
                "name": f"Single invalid code ({invalid})",
                "codes": [invalid],
                "expected": "NAY",
                "expected_check": "P1",
                "difficulty": "basic",
            }
        )
        test_num += 1

    # Multiple invalid codes - 30 tests
    for i in range(30):
        if test_num > 100:
            break
        invalid1 = data["invalid_codes"][i % len(data["invalid_codes"])]
        invalid2 = data["invalid_codes"][(i + 1) % len(data["invalid_codes"])]
        tests.append(
            {
                "test_id": test_num,
                "category": "P1",
                "name": f"Multiple invalid codes ({invalid1}, {invalid2})",
                "codes": [invalid1, invalid2],
                "expected": "NAY",
                "expected_check": "P1",
                "difficulty": "basic",
            }
        )
        test_num += 1

    # Invalid mixed with valid - 20 tests
    for i in range(20):
        if test_num > 100:
            break
        invalid = data["invalid_codes"][i % len(data["invalid_codes"])]
        valid = data["valid_codes"][i % len(data["valid_codes"])]
        tests.append(
            {
                "test_id": test_num,
                "category": "P1",
                "name": f"Invalid mixed with valid ({invalid}, {valid})",
                "codes": [invalid, valid],
                "expected": "NAY",
                "expected_check": "P1",
                "difficulty": "basic",
            }
        )
        test_num += 1

    # Empty and whitespace - 5 tests
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

    # Invalid numeric codes - fill to 100
    for i in range(100 - test_num + 1):
        tests.append(
            {
                "test_id": test_num + i,
                "category": "P1",
                "name": f"Invalid numeric code {999999 + i}",
                "codes": [str(999999 + i)],
                "expected": "NAY",
                "expected_check": "P1",
                "difficulty": "edge_case",
            }
        )
    test_num = 101

    # ===== C1: Mutual Exclusions (300 tests) =====
    print("Generating C1 tests (300)...")

    # Group conflicts - 2 codes same group (150 tests)
    # Exclude pairs where one code is solo-only (those will be C3, not C1)
    solo_codes_set = set(data["solo_codes"])
    group_tests = 0
    for group in data["groups"]:
        if group_tests >= 150:
            break
        for i in range(len(group["codes"]) - 1):
            if group_tests >= 150:
                break
            for j in range(i + 1, len(group["codes"])):
                if group_tests >= 150:
                    break
                code1 = group["codes"][i]
                code2 = group["codes"][j]
                # Skip if either code is solo-only (will be caught by C3)
                if code1 in solo_codes_set or code2 in solo_codes_set:
                    continue
                tests.append(
                    {
                        "test_id": test_num,
                        "category": "C1",
                        "name": f"Group conflict - {group['group']} ({code1} and {code2})",
                        "codes": [code1, code2],
                        "expected": "NAY",
                        "expected_check": "C1",
                        "difficulty": "moderate",
                    }
                )
                test_num += 1
                group_tests += 1

    # Group conflicts - 3+ codes same group (50 tests)
    # Exclude groups that contain solo-only codes
    solo_codes_set = set(data["solo_codes"])
    group_multiple = 0
    for group in data["groups"]:
        if group_multiple >= 50:
            break
        if len(group["codes"]) >= 3:
            # Filter out solo-only codes from the group
            non_solo_codes = [c for c in group["codes"] if c not in solo_codes_set]
            if len(non_solo_codes) < 2:
                continue  # Need at least 2 non-solo codes for group conflict test

            # Test various combinations of 3+ codes
            for combo_size in [3, 4, 5]:
                if len(non_solo_codes) >= combo_size and group_multiple < 50:
                    tests.append(
                        {
                            "test_id": test_num,
                            "category": "C1",
                            "name": f"Group conflict - {group['group']} ({combo_size} codes)",
                            "codes": non_solo_codes[:combo_size],
                            "expected": "NAY",
                            "expected_check": "C1",
                            "difficulty": "moderate",
                        }
                    )
                    test_num += 1
                    group_multiple += 1
                    if group_multiple >= 50:
                        break

    # Direct exclusions (100 tests)
    for i, excl in enumerate(data["exclusions"]):
        if i >= 100:
            break
        tests.append(
            {
                "test_id": test_num,
                "category": "C1",
                "name": f"Direct exclusion ({excl['from']} excludes {excl['to']})",
                "codes": [excl["from"], excl["to"]],
                "expected": "NAY",
                "expected_check": "C1",
                "difficulty": "moderate",
            }
        )
        test_num += 1

    # Fill remaining C1 tests with same_day_excludes
    for i, excl in enumerate(data["same_day_excludes"]):
        if test_num > 400:
            break
        tests.append(
            {
                "test_id": test_num,
                "category": "C1",
                "name": f"Same day exclusion ({excl['from']} same_day_excludes {excl['to']})",
                "codes": [excl["from"], excl["to"]],
                "expected": "NAY",
                "expected_check": "C1",
                "difficulty": "moderate",
            }
        )
        test_num += 1

    # ===== C2: Mandatory Dependencies (150 tests) =====
    print("Generating C2 tests (150)...")

    # Missing prerequisites - test all available, then repeat patterns
    conn_temp = sqlite3.connect("mbs.db")
    cursor_temp = conn_temp.cursor()

    c2_added = 0
    valid_prereqs = []

    # Collect all valid prerequisites first
    for prereq in data["prereqs"]:
        cursor_temp.execute(
            "SELECT item_num FROM items WHERE item_num = ?", (prereq["code"],)
        )
        source_exists = cursor_temp.fetchone()
        if source_exists:
            valid_prereqs.append(prereq)

    # Generate tests from valid prerequisites (repeat if needed)
    for i in range(150):
        prereq = valid_prereqs[i % len(valid_prereqs)]
        tests.append(
            {
                "test_id": test_num,
                "category": "C2",
                "name": f"Missing prerequisite ({prereq['code']} requires {prereq['requires']}) - test {i+1}",
                "codes": [prereq["code"]],
                "expected": "NAY",
                "expected_check": "C2",
                "difficulty": "moderate",
                "expected_reason_contains": prereq["requires"],
            }
        )
        test_num += 1
        c2_added += 1

    conn_temp.close()

    # ===== C3: Solo-Only Codes (100 tests) =====
    print("Generating C3 tests (100)...")

    # Solo code alone (50 tests) - repeat solo codes if needed
    for i in range(50):
        solo = data["solo_codes"][i % len(data["solo_codes"])]
        tests.append(
            {
                "test_id": test_num,
                "category": "C3",
                "name": f"Solo-only code alone ({solo}) - test {i+1}",
                "codes": [solo],
                "expected": "YAY",
                "expected_check": None,
                "difficulty": "basic",
            }
        )
        test_num += 1

    # Solo code with other (50 tests) - use different valid codes
    for i in range(50):
        solo = data["solo_codes"][i % len(data["solo_codes"])]
        other = data["valid_codes"][i % len(data["valid_codes"])]
        tests.append(
            {
                "test_id": test_num,
                "category": "C3",
                "name": f"Solo-only code with other ({solo} with {other}) - test {i+1}",
                "codes": [solo, other],
                "expected": "NAY",
                "expected_check": "C3",
                "difficulty": "moderate",
            }
        )
        test_num += 1

    # ===== C4: Duplicate Limits (100 tests) =====
    print("Generating C4 tests (100)...")

    # Duplicate same_occasion codes (70 tests) - repeat if needed
    for i in range(70):
        code = data["same_occasion"][i % len(data["same_occasion"])]
        tests.append(
            {
                "test_id": test_num,
                "category": "C4",
                "name": f"Duplicate same_occasion code ({code} x2) - test {i+1}",
                "codes": [code, code],
                "expected": "NAY",
                "expected_check": "C4",
                "difficulty": "moderate",
            }
        )
        test_num += 1

    # Multiple duplicates (30 tests) - repeat if needed
    for i in range(30):
        code = data["same_occasion"][i % len(data["same_occasion"])]
        tests.append(
            {
                "test_id": test_num,
                "category": "C4",
                "name": f"Multiple duplicates ({code} x3) - test {i+1}",
                "codes": [code, code, code],
                "expected": "NAY",
                "expected_check": "C4",
                "difficulty": "advanced",
            }
        )
        test_num += 1

    # ===== YAY: Success Cases (250 tests) =====
    print("Generating YAY tests (250)...")

    # Single valid codes (50 tests)
    for i, code in enumerate(data["valid_codes"][:50]):
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

    # Compatible pairs (200 tests)
    print("  Finding compatible pairs...")
    compatible_pairs = find_compatible_pairs(
        data, max_pairs=300
    )  # Get more to allow repeats

    for i in range(200):
        pair = compatible_pairs[i % len(compatible_pairs)]
        tests.append(
            {
                "test_id": test_num,
                "category": "YAY",
                "name": f"Compatible codes ({pair[0]} and {pair[1]}) - test {i+1}",
                "codes": pair,
                "expected": "YAY",
                "expected_check": None,
                "difficulty": "moderate",
            }
        )
        test_num += 1

    # Re-number tests to be sequential
    for i, test in enumerate(tests, 1):
        test["test_id"] = i

    return tests


def main():
    """Generate and save 1000 test cases."""
    print("=" * 80)
    print("Generating 1000 MBS Compatibility Test Cases")
    print("=" * 80)
    print("Extracting test data from database...")
    data = get_comprehensive_test_data()

    print(f"\nData extracted:")
    print(f"  - All codes: {len(data['all_codes'])}")
    print(f"  - Groups: {len(data['groups'])}")
    print(f"  - Exclusions: {len(data['exclusions'])}")
    print(f"  - Prerequisites: {len(data['prereqs'])}")
    print(f"  - Solo codes: {len(data['solo_codes'])}")
    print(f"  - Same occasion: {len(data['same_occasion'])}")
    print(f"  - Valid codes: {len(data['valid_codes'])}")

    print("\nGenerating 1000 test cases...")
    tests = generate_1000_tests(data)

    # Ensure we have exactly 1000
    tests = tests[:1000]
    for i, test in enumerate(tests, 1):
        test["test_id"] = i

    # Save as JSON
    print(f"\nSaving to compatibility_test_cases_1000.json...")
    with open("compatibility_test_cases_1000.json", "w") as f:
        json.dump(tests, f, indent=2)

    # Generate Python test file
    print("Generating Python test file...")
    with open("test_compatibility_1000.py", "w") as f:
        f.write(
            '''#!/usr/bin/env python3
"""
Comprehensive test suite for MBS compatibility checker - 1000 test cases.
Generated from real MBS data with actual code combinations.
"""

import pytest
import json
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from mbs_clarity.compatibility_checker import check_mbs_compatibility


# Load test cases
with open("compatibility_test_cases_1000.json", "r") as f:
    TEST_CASES = json.load(f)


class TestCompatibilityChecker1000:
    """Comprehensive test suite - 1000 test cases."""
    
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
                    .replace("'", "")
                    .replace('"', "")
                    .replace("/", "_")
                    .replace("\\", "_")
                )
                codes_repr = test["codes"]

                f.write(
                    f"""    def test_{category.lower()}_{test['test_id']:04d}_{test_name[:50]}(self):
        \"\"\"{test['name']} (Difficulty: {test['difficulty']})\"\"\"
        codes = {codes_repr}
        result = check_mbs_compatibility(codes)
        
        assert result['decision'] == '{test['expected']}', \\
            f"Expected {test['expected']}, got {{result['decision']}}. Reason: {{result['reason']}}"
        
        assert result['failed_check'] == {repr(test['expected_check'])}, \\
            f"Expected failed_check {repr(test['expected_check'])}, got {{result['failed_check']}}"
        
"""
                )

        f.write(
            """
if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
"""
        )

    # Print summary
    print(f"\n✅ Generated {len(tests)} test cases:")
    category_counts = {}
    for test in tests:
        cat = test["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1

    for cat, count in sorted(category_counts.items()):
        print(f"  - {cat}: {count} tests")

    print(f"\n📁 Files created:")
    print(f"  - compatibility_test_cases_1000.json")
    print(f"  - test_compatibility_1000.py")
    print(f"\n🧪 Run tests with: pytest test_compatibility_1000.py -v")


if __name__ == "__main__":
    main()
