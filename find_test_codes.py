#!/usr/bin/env python3
"""
Helper script to find real MBS codes for testing compatibility checker.
Queries the database to find codes with specific relations and constraints.
"""

import sqlite3
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.mbs_clarity.db import get_conn


def find_test_codes():
    """Find codes with specific relations/constraints for testing."""

    print("=" * 70)
    print("Finding MBS Codes for Compatibility Testing")
    print("=" * 70)
    print()

    with get_conn() as conn:
        cur = conn.cursor()

        # Find codes with generic_excludes (solo-only)
        print("1. CODES WITH generic_excludes (for C3 solo-only tests):")
        print("-" * 70)
        cur.execute(
            """
            SELECT DISTINCT r.item_num, i.description
            FROM relations r
            JOIN items i ON r.item_num = i.item_num
            WHERE r.relation_type = 'generic_excludes'
            LIMIT 5
        """
        )
        solo_codes = cur.fetchall()
        if solo_codes:
            for code, desc in solo_codes:
                desc_short = (desc[:60] + "...") if desc and len(desc) > 60 else desc
                print(f"   Code: {code:6} | {desc_short}")
            print(f"   → Use code {solo_codes[0][0]} for C3 tests")
        else:
            print("   No codes found with generic_excludes")
        print()

        # Find codes with prerequisites
        print("2. CODES WITH prerequisites (for C2 dependency tests):")
        print("-" * 70)
        cur.execute(
            """
            SELECT r.item_num, r.target_item_num, i.description
            FROM relations r
            JOIN items i ON r.item_num = i.item_num
            WHERE r.relation_type = 'prerequisite'
            LIMIT 5
        """
        )
        prereq_codes = cur.fetchall()
        if prereq_codes:
            for code, req_code, desc in prereq_codes:
                desc_short = (desc[:50] + "...") if desc and len(desc) > 50 else desc
                print(f"   Code: {code:6} requires {req_code:6} | {desc_short}")
            test_case = prereq_codes[0]
            print(f"   → Use: code {test_case[0]} requires {test_case[1]}")
        else:
            print("   No codes found with prerequisites")
        print()

        # Find codes with same group_code (potential conflicts)
        print("3. CODES WITH SAME group_code (for C1 group conflict tests):")
        print("-" * 70)
        cur.execute(
            """
            SELECT group_code, GROUP_CONCAT(item_num, ', ') as codes
            FROM items
            WHERE group_code IS NOT NULL AND group_code != ''
            GROUP BY group_code
            HAVING COUNT(*) > 1
            LIMIT 5
        """
        )
        group_conflicts = cur.fetchall()
        if group_conflicts:
            for group_code, codes in group_conflicts:
                code_list = codes.split(", ")
                print(f"   Group {group_code:6} | Codes: {', '.join(code_list[:5])}")
                if len(code_list) >= 2:
                    print(
                        f"   → Use codes {code_list[0]} and {code_list[1]} for C1 group conflict test"
                    )
        else:
            print("   No group conflicts found")
        print()

        # Find codes with excludes relations
        print("4. CODES WITH excludes RELATIONS (for C1 exclusion tests):")
        print("-" * 70)
        cur.execute(
            """
            SELECT r.item_num, r.target_item_num, i.description
            FROM relations r
            JOIN items i ON r.item_num = i.item_num
            WHERE r.relation_type = 'excludes' AND r.target_item_num IS NOT NULL
            LIMIT 5
        """
        )
        excludes = cur.fetchall()
        if excludes:
            for code, target, desc in excludes:
                desc_short = (desc[:50] + "...") if desc and len(desc) > 50 else desc
                print(f"   Code {code:6} excludes {target:6} | {desc_short}")
            test_case = excludes[0]
            print(
                f"   → Use codes {test_case[0]} and {test_case[1]} for C1 exclusion test"
            )
        else:
            print("   No excludes relations found")
        print()

        # Find codes with same_occasion constraint
        print("5. CODES WITH same_occasion CONSTRAINT (for C4 duplicate tests):")
        print("-" * 70)
        cur.execute(
            """
            SELECT DISTINCT c.item_num, i.description
            FROM constraints c
            JOIN items i ON c.item_num = i.item_num
            WHERE c.constraint_type = 'same_occasion'
            LIMIT 5
        """
        )
        same_occasion = cur.fetchall()
        if same_occasion:
            for code, desc in same_occasion:
                desc_short = (desc[:60] + "...") if desc and len(desc) > 60 else desc
                print(f"   Code: {code:6} | {desc_short}")
            print(f"   → Use code {same_occasion[0][0]} for C4 duplicate test")
        else:
            print("   No codes found with same_occasion constraint")
        print()

        # Find some basic valid codes
        print("6. SAMPLE VALID CODES (for YAY success tests):")
        print("-" * 70)
        cur.execute(
            """
            SELECT item_num, description
            FROM items
            ORDER BY CAST(item_num AS INTEGER)
            LIMIT 10
        """
        )
        valid_codes = cur.fetchall()
        if valid_codes:
            codes_only = [str(c[0]) for c in valid_codes[:5]]
            print(f"   Codes: {', '.join(codes_only)}")
            print(f"   → Use these for basic compatibility tests")
        print()

        # Summary
        print("=" * 70)
        print("TEST COMMANDS:")
        print("=" * 70)

        if solo_codes:
            solo_code = solo_codes[0][0]
            print(f"\n# C3 Test: Solo-only code with other codes")
            print(f"curl -X POST http://localhost:8000/api/compatibility/check \\")
            print(f'  -H "Content-Type: application/json" \\')
            print(f'  -d \'{{"codes": ["{solo_code}", "3"]}}\'')

        if prereq_codes:
            code, req_code = prereq_codes[0][0], prereq_codes[0][1]
            print(f"\n# C2 Test: Missing prerequisite")
            print(f"curl -X POST http://localhost:8000/api/compatibility/check \\")
            print(f'  -H "Content-Type: application/json" \\')
            print(f'  -d \'{{"codes": ["{code}"]}}\'')
            print(f"\n# C2 Test: With prerequisite")
            print(f"curl -X POST http://localhost:8000/api/compatibility/check \\")
            print(f'  -H "Content-Type: application/json" \\')
            print(f'  -d \'{{"codes": ["{code}", "{req_code}"]}}\'')

        if group_conflicts:
            code_list = group_conflicts[0][1].split(", ")
            if len(code_list) >= 2:
                print(f"\n# C1 Test: Group conflict")
                print(f"curl -X POST http://localhost:8000/api/compatibility/check \\")
                print(f'  -H "Content-Type: application/json" \\')
                print(f'  -d \'{{"codes": ["{code_list[0]}", "{code_list[1]}"]}}\'')

        if excludes:
            code, target = excludes[0][0], excludes[0][1]
            print(f"\n# C1 Test: Direct exclusion")
            print(f"curl -X POST http://localhost:8000/api/compatibility/check \\")
            print(f'  -H "Content-Type: application/json" \\')
            print(f'  -d \'{{"codes": ["{code}", "{target}"]}}\'')

        if valid_codes:
            codes_str = ", ".join([f'"{c[0]}"' for c in valid_codes[:3]])
            print(f"\n# YAY Test: Compatible codes")
            print(f"curl -X POST http://localhost:8000/api/compatibility/check \\")
            print(f'  -H "Content-Type: application/json" \\')
            print(f"  -d '{{\"codes\": [{codes_str}]}}'")

        print()


if __name__ == "__main__":
    find_test_codes()
