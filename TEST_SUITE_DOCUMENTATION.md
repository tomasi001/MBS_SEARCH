# MBS Compatibility Checker - Comprehensive Test Suite

## Overview

This test suite contains **100 comprehensive test cases** derived from real MBS data. The tests are designed to thoroughly validate all compatibility gates (P1, C1, C2, C3, C4) and success scenarios.

## Test Distribution

| Category  | Count   | Description                                                                 |
| --------- | ------- | --------------------------------------------------------------------------- |
| **P1**    | 14      | Invalid Item Numbers                                                        |
| **C1**    | 25      | Mutual Exclusions (Group conflicts, direct exclusions, same-day exclusions) |
| **C2**    | 15      | Mandatory Dependencies (Missing prerequisites)                              |
| **C3**    | 10      | Solo-Only Codes                                                             |
| **C4**    | 15      | Duplicate Limits (same_occasion constraints)                                |
| **YAY**   | 21      | Success Cases (Compatible codes)                                            |
| **TOTAL** | **100** |                                                                             |

## Test Categories

### P1: Invalid Item Numbers (14 tests)

Tests validation of input codes:

- Single invalid code
- Multiple invalid codes
- Invalid codes mixed with valid codes
- Empty input
- Whitespace-only codes
- Invalid numeric codes (non-existent item numbers)

**Example Test:**

```python
test_p1_001_single_invalid_code
  Codes: ['X999']
  Expected: NAY, failed_check: P1
```

### C1: Mutual Exclusions (25 tests)

Tests detection of conflicts between codes:

- **Group conflicts**: Multiple codes from the same exclusion group (e.g., Group A1)
- **Direct exclusions**: One code explicitly excludes another
- **Same-day exclusions**: Codes that cannot be used on the same day
- **Multiple conflicts**: 3+ codes from the same group

**Example Tests:**

```python
# Group conflict
test_c1_015_group_conflict_a1_3_and_4
  Codes: ['3', '4']  # Both in Group A1
  Expected: NAY, failed_check: C1

# Direct exclusion
test_c1_025_direct_exclusion_104_excludes_106
  Codes: ['104', '106']  # 104 excludes 106
  Expected: NAY, failed_check: C1
```

### C2: Mandatory Dependencies (15 tests)

Tests detection of missing prerequisites:

- Codes that require another code to be present
- Prerequisites may reference codes that don't exist in database (like "45" for "45 minutes")
- Tests validate that C2 logic correctly identifies missing dependencies

**Example Test:**

```python
test_c2_040_missing_prerequisite_127_requires_45
  Codes: ['127']  # Requires code 45
  Expected: NAY, failed_check: C2
```

### C3: Solo-Only Codes (10 tests)

Tests codes that must be billed alone:

- Solo-only code by itself (should pass)
- Solo-only code with other codes (should fail)
- Tests use codes with `generic_excludes` relation

**Example Tests:**

```python
# Solo code alone - PASS
test_c3_055_solo_only_code_alone_36
  Codes: ['36']
  Expected: YAY

# Solo code with other - FAIL
test_c3_060_solo_only_code_with_other_36_with_3
  Codes: ['36', '3']
  Expected: NAY, failed_check: C3
```

### C4: Duplicate Limits (15 tests)

Tests detection of duplicate codes when quantity limits apply:

- Codes with `same_occasion` constraint (limited to 1 per occasion)
- Duplicate submissions (same code twice)
- Multiple duplicates (same code 3+ times)

**Example Test:**

```python
test_c4_070_duplicate_same_occasion_code_11729_x2
  Codes: ['11729', '11729']  # same_occasion constraint
  Expected: NAY, failed_check: C4
```

### YAY: Success Cases (21 tests)

Tests compatible code combinations:

- Single valid codes
- Multiple compatible codes (different groups, no exclusions)
- Valid combinations that should pass all checks

**Example Test:**

```python
test_yay_085_single_valid_code_104
  Codes: ['104']
  Expected: YAY, failed_check: None
```

## Test Data Source

All test cases are derived from **real MBS data** extracted from:

- `mbs.db` SQLite database
- Actual item numbers, relationships, and constraints
- Real exclusion groups, prerequisites, and constraints

## Running the Tests

### Prerequisites

```bash
pip install pytest
```

### Run All Tests

```bash
pytest test_compatibility_comprehensive.py -v
```

### Run Specific Category

```bash
# Run only P1 tests
pytest test_compatibility_comprehensive.py -k "p1" -v

# Run only C1 tests
pytest test_compatibility_comprehensive.py -k "c1" -v
```

### Run with Coverage

```bash
pytest test_compatibility_comprehensive.py --cov=src.mbs_clarity.compatibility_checker --cov-report=html
```

## Test File Structure

### JSON Test Cases

`compatibility_test_cases.json` contains all 100 test cases in JSON format:

```json
{
  "test_id": 1,
  "category": "P1",
  "name": "Single invalid code",
  "codes": ["X999"],
  "expected": "NAY",
  "expected_check": "P1",
  "difficulty": "basic"
}
```

### Python Test File

`test_compatibility_comprehensive.py` contains pytest test cases generated from the JSON file.

## Test Difficulty Levels

- **Basic**: Simple, straightforward test cases
- **Moderate**: Tests with some complexity (e.g., group conflicts, prerequisites)
- **Advanced**: Complex edge cases (e.g., bidirectional exclusions, multiple duplicates)
- **Edge Case**: Boundary conditions and unusual inputs

## Validation Strategy

Each test validates:

1. **Decision**: `YAY` or `NAY`
2. **Failed Check**: Which gate failed (P1, C1, C2, C3, C4) or `None` for success
3. **Reason**: Human-readable explanation (optional validation)
4. **Details**: Additional context about the failure (optional validation)

## Regenerating Tests

To regenerate test cases from the database:

```bash
python3 generate_compatibility_tests.py
```

This will:

1. Extract real data from `mbs.db`
2. Generate 100 test cases
3. Create `compatibility_test_cases.json`
4. Generate `test_compatibility_comprehensive.py`

## Notes

- Prerequisites in the database may reference codes that don't exist (like "45" meaning "45 minutes" not code "45"). This is intentional - the tests validate that C2 logic correctly identifies missing dependencies even when the target code doesn't exist.

- Some test cases may fail if the database structure changes or if codes are added/removed. The test generator can be re-run to update test cases.

- All tests use real MBS item numbers and relationships, ensuring realistic validation of the compatibility checker.

## Expected Results

When all tests pass, you should see:

```
test_compatibility_comprehensive.py::TestCompatibilityChecker::test_p1_001_... PASSED
test_compatibility_comprehensive.py::TestCompatibilityChecker::test_c1_015_... PASSED
...
======================== 100 passed in X.XXs ========================
```

## Maintenance

- Review test results regularly
- Update tests if MBS data structure changes
- Add new test cases for edge cases discovered in production
- Document any test failures and their resolutions
