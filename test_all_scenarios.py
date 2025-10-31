#!/usr/bin/env python3
"""Comprehensive test with real codes from database."""

import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.mbs_clarity.compatibility_checker import check_mbs_compatibility

def test(name, codes, expected_decision, expected_check=None):
    """Run a test and return pass/fail."""
    result = check_mbs_compatibility(codes)
    decision = result.get("decision")
    failed_check = result.get("failed_check")
    reason = result.get("reason")
    
    print(f"\n{'='*70}")
    print(f"TEST: {name}")
    print(f"{'='*70}")
    print(f"Codes: {codes}")
    print(f"Expected: decision={expected_decision}, failed_check={expected_check}")
    print(f"Got:      decision={decision}, failed_check={failed_check}")
    print(f"Reason: {reason}")
    
    if decision == expected_decision:
        if expected_check is None or failed_check == expected_check:
            print(f"✓ PASS")
            return True
        else:
            print(f"✗ FAIL - failed_check mismatch")
            return False
    else:
        print(f"✗ FAIL - decision mismatch")
        return False

print("\n" + "="*70)
print("COMPREHENSIVE COMPATIBILITY CHECKER TESTS")
print("Using Real Codes from Database")
print("="*70)

passed = 0
failed = 0

# P1: Invalid codes
if test("P1: Invalid code X999", ["X999"], "NAY", "P1"):
    passed += 1
else:
    failed += 1

# C3: Solo-only code (code 36 has generic_excludes)
if test("C3: Solo-only code 36 with other code", ["36", "3"], "NAY", "C3"):
    passed += 1
else:
    failed += 1

# C3: Solo-only code alone (should pass)
if test("C3: Solo-only code 36 alone", ["36"], "YAY", None):
    passed += 1
else:
    failed += 1

# C1: Group conflict (codes 3 and 4 are both in Group A1)
if test("C1: Group conflict - codes 3 and 4 (same group A1)", ["3", "4"], "NAY", "C1"):
    passed += 1
else:
    failed += 1

# C1: Direct exclusion (code 104 excludes 106)
if test("C1: Direct exclusion - code 104 excludes 106", ["104", "106"], "NAY", "C1"):
    passed += 1
else:
    failed += 1

# C2: Missing prerequisite (code 127 requires 45)
if test("C2: Missing prerequisite - code 127 requires 45", ["127"], "NAY", "C2"):
    passed += 1
else:
    failed += 1

# C2: With prerequisite (should pass)
if test("C2: With prerequisite - code 127 with required 45", ["127", "45"], "YAY", None):
    passed += 1
else:
    failed += 1

# C4: Duplicate with same_occasion (code 11729 has same_occasion)
if test("C4: Duplicate code 11729 (has same_occasion)", ["11729", "11729"], "NAY", "C4"):
    passed += 1
else:
    failed += 1

# YAY: Compatible codes (code 3 alone)
if test("YAY: Single compatible code 3", ["3"], "YAY", None):
    passed += 1
else:
    failed += 1

# YAY: Compatible codes (need codes from different groups)
# Let's find codes that aren't in conflict
if test("YAY: Compatible codes - 3 and 106 (different groups, no exclusion)", ["3", "106"], "YAY", None):
    passed += 1
else:
    failed += 1

# Edge cases
if test("EDGE: Whitespace normalization", [" 3 ", " 4 "], "NAY", "C1"):  # Should still detect conflict
    passed += 1
else:
    failed += 1

if test("EDGE: Duplicate normalization then conflict check", ["3", "3", "4"], "NAY", "C1"):
    passed += 1
else:
    failed += 1

print("\n" + "="*70)
print("SUMMARY")
print("="*70)
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Total:  {passed + failed}")
print("="*70)

if failed == 0:
    print("\n✓ ALL TESTS PASSED!")
    print("\nNote: API endpoint tests require server restart.")
    sys.exit(0)
else:
    print("\n✗ SOME TESTS FAILED")
    sys.exit(1)

