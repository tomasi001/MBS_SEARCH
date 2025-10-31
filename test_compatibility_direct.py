#!/usr/bin/env python3
"""
Direct test of compatibility checker (bypasses server).
This allows testing the logic even if the server needs restarting.
"""

import sys
import os

# Add project root to path (like production server does)
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Add production directory parent to path for imports
sys.path.insert(0, os.path.dirname(project_root))

try:
    from src.mbs_clarity.compatibility_checker import check_mbs_compatibility
    print("✓ Successfully imported check_mbs_compatibility")
    print()
except Exception as e:
    print(f"✗ Import failed: {e}")
    print("\nTrying alternative import path...")
    # Try alternative path
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "compatibility_checker",
        os.path.join(project_root, "src/mbs_clarity/compatibility_checker.py")
    )
    module = importlib.util.module_from_spec(spec)
    # Need to set up the path in the module's namespace
    import sys
    sys.path.insert(0, project_root)
    spec.loader.exec_module(module)
    check_mbs_compatibility = module.check_mbs_compatibility
    print("✓ Successfully imported via alternative method")
    print()

def test_case(name, codes, expected_decision, expected_check=None):
    """Test a compatibility check case."""
    print(f"Test: {name}")
    print(f"  Codes: {codes}")
    try:
        result = check_mbs_compatibility(codes)
        decision = result.get("decision")
        failed_check = result.get("failed_check")
        reason = result.get("reason", "")[:80]
        
        print(f"  Result: decision={decision}, failed_check={failed_check}")
        print(f"  Reason: {reason}...")
        
        if decision == expected_decision:
            if expected_check is None or failed_check == expected_check:
                print(f"  ✓ PASS")
                return True
            else:
                print(f"  ✗ FAIL - Expected failed_check={expected_check}, got={failed_check}")
                return False
        else:
            print(f"  ✗ FAIL - Expected decision={expected_decision}, got={decision}")
            return False
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        print()

print("=" * 70)
print("Direct Compatibility Checker Tests")
print("=" * 70)
print()

passed = 0
failed = 0

# P1 Tests
print("Category P1: Invalid Item Numbers")
print("-" * 70)
if test_case("P1.1: Empty codes", [], "NAY", "P1"):
    passed += 1
else:
    failed += 1

if test_case("P1.2: Invalid code", ["X999"], "NAY", "P1"):
    passed += 1
else:
    failed += 1

if test_case("P1.3: Multiple invalid codes", ["INVALID1", "INVALID2"], "NAY", "P1"):
    passed += 1
else:
    failed += 1

# YAY Tests
print("Category YAY: Success Cases")
print("-" * 70)
# Test with code 3 (common MBS code)
if test_case("YAY.1: Single code (3)", ["3"], "YAY"):
    passed += 1
else:
    failed += 1

if test_case("YAY.2: Multiple codes", ["3", "23"], "YAY"):
    passed += 1
else:
    failed += 1

if test_case("YAY.3: Codes with whitespace", [" 3 ", " 23 "], "YAY"):
    passed += 1
else:
    failed += 1

# Summary
print("=" * 70)
print(f"Summary: {passed} passed, {failed} failed")
print("=" * 70)

if failed == 0:
    print("\n✓ All direct tests passed!")
    print("\nNote: Server endpoint tests require server restart to load new endpoint.")
    sys.exit(0)
else:
    print("\n✗ Some tests failed")
    sys.exit(1)

