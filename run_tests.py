#!/usr/bin/env python3
"""
Run compatibility checker tests and analyze results.
"""

import json
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from mbs_clarity.compatibility_checker import check_mbs_compatibility

# Load test cases
with open("compatibility_test_cases.json", "r") as f:
    TEST_CASES = json.load(f)


def run_tests():
    """Run all tests and collect results."""
    results = {"passed": [], "failed": [], "errors": [], "by_category": {}}

    print("Running 100 compatibility checker tests...\n")

    for test in TEST_CASES:
        category = test["category"]
        if category not in results["by_category"]:
            results["by_category"][category] = {"passed": 0, "failed": 0, "errors": 0}

        try:
            codes = test["codes"]
            expected = test["expected"]
            expected_check = test["expected_check"]

            # Run the compatibility check
            result = check_mbs_compatibility(codes)

            # Check decision
            decision_match = result["decision"] == expected
            check_match = result["failed_check"] == expected_check

            if decision_match and check_match:
                results["passed"].append(test)
                results["by_category"][category]["passed"] += 1
                print(f"✓ {test['test_id']:03d} {category} - {test['name'][:60]}")
            else:
                results["failed"].append({"test": test, "result": result, "issue": []})
                results["by_category"][category]["failed"] += 1

                if not decision_match:
                    results["failed"][-1]["issue"].append(
                        f"Decision mismatch: expected {expected}, got {result['decision']}"
                    )
                if not check_match:
                    results["failed"][-1]["issue"].append(
                        f"Check mismatch: expected {expected_check}, got {result['failed_check']}"
                    )

                print(f"✗ {test['test_id']:03d} {category} - {test['name'][:60]}")
                print(
                    f"    Expected: {expected}/{expected_check}, Got: {result['decision']}/{result['failed_check']}"
                )
                print(f"    Reason: {result['reason'][:80]}")

        except Exception as e:
            results["errors"].append({"test": test, "error": str(e)})
            results["by_category"][category]["errors"] += 1
            print(f"✗ {test['test_id']:03d} {category} - {test['name'][:60]}")
            print(f"    ERROR: {e}")

    return results


def print_summary(results):
    """Print test summary."""
    total = len(TEST_CASES)
    passed = len(results["passed"])
    failed = len(results["failed"])
    errors = len(results["errors"])

    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"Total Tests: {total}")
    print(f"✓ Passed: {passed} ({passed/total*100:.1f}%)")
    print(f"✗ Failed: {failed} ({failed/total*100:.1f}%)")
    print(f"⚠ Errors: {errors} ({errors/total*100:.1f}%)")
    print("\nBy Category:")
    for category in sorted(results["by_category"].keys()):
        cat_stats = results["by_category"][category]
        total_cat = cat_stats["passed"] + cat_stats["failed"] + cat_stats["errors"]
        pass_pct = (cat_stats["passed"] / total_cat * 100) if total_cat > 0 else 0
        print(
            f"  {category}: {cat_stats['passed']}/{total_cat} passed ({pass_pct:.1f}%)"
        )

    if results["failed"]:
        print("\n" + "=" * 80)
        print("FAILED TESTS ANALYSIS")
        print("=" * 80)

        # Group by issue type
        issue_types = {}
        for failure in results["failed"]:
            for issue in failure["issue"]:
                issue_type = issue.split(":")[0]
                if issue_type not in issue_types:
                    issue_types[issue_type] = []
                issue_types[issue_type].append(failure)

        for issue_type, failures in issue_types.items():
            print(f"\n{issue_type} ({len(failures)} tests):")
            for failure in failures[:10]:  # Show first 10
                test = failure["test"]
                print(f"  - Test {test['test_id']}: {test['name']}")
                print(f"    Codes: {test['codes']}")
                for issue in failure["issue"]:
                    print(f"    {issue}")
                print(f"    Actual reason: {failure['result']['reason'][:100]}")
            if len(failures) > 10:
                print(f"  ... and {len(failures) - 10} more")


if __name__ == "__main__":
    results = run_tests()
    print_summary(results)

    # Save detailed results
    with open("test_results.json", "w") as f:
        json.dump(
            {
                "total": len(TEST_CASES),
                "passed": len(results["passed"]),
                "failed": len(results["failed"]),
                "errors": len(results["errors"]),
                "failed_tests": results["failed"],
                "errors": results["errors"],
            },
            f,
            indent=2,
        )

    # Exit with error code if tests failed
    sys.exit(1 if (len(results["failed"]) > 0 or len(results["errors"]) > 0) else 0)
