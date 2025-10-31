# MBS Compatibility Checker API Test Guide

## Quick Start

### Base URL

```
http://localhost:8000/api/compatibility/check
```

### Endpoint

**POST** `/api/compatibility/check`

### Request Format

```json
{
  "codes": ["23", "36", "104"]
}
```

### Response Format

```json
{
  "decision": "YAY" or "NAY",
  "reason": "Human-readable explanation",
  "failed_check": "P1|C1|C2|C3|C4" or null,
  "details": {...}
}
```

---

## Test Categories

### P1: Invalid Item Numbers (System Error)

```bash
# Empty codes
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": []}'

# Invalid code
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["X999"]}'

# Multiple invalid codes
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["INVALID1", "INVALID2"]}'

# Mix of valid and invalid
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["3", "INVALID", "104"]}'
```

**Expected**: `"decision": "NAY"`, `"failed_check": "P1"`

---

### C1: Mutual Exclusions (Conflict)

```bash
# Test group conflict (codes with same group_code)
# Example: Codes 23 and 36 might be in same exclusion group
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["23", "36"]}'

# Test direct exclusion (if code 3 excludes code 104)
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["3", "104"]}'
```

**Expected**: `"decision": "NAY"`, `"failed_check": "C1"`

---

### C2: Mandatory Dependencies (Missing)

```bash
# Test code requiring prerequisite without it
# Replace CODE_WITH_PREREQ with actual code that has prerequisite relation
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["CODE_WITH_PREREQ"]}'

# Test with prerequisite present
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["CODE_WITH_PREREQ", "REQUIRED_CODE"]}'
```

**Expected**: First returns `"NAY"` with `"failed_check": "C2"`, second returns `"YAY"`

---

### C3: Solo-Only Codes (Co-Claiming Violation)

```bash
# Code 44 has generic_excludes - test with other codes
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["44", "3"]}'

# Code 44 alone should pass
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["44"]}'
```

**Expected**: First returns `"NAY"` with `"failed_check": "C3"`, second returns `"YAY"`

---

### C4: Duplicate Limits

```bash
# Test duplicate code (normalized, so this should pass unless code has same_occasion constraint)
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["3", "3"]}'

# Test with whitespace duplicates
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": [" 3 ", "3", " 3 "]}'
```

**Expected**: Should normalize to single code and pass, unless code has `same_occasion` constraint

---

### YAY: Success Cases

```bash
# Single valid code
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["3"]}'

# Multiple compatible codes
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["3", "23"]}'

# Codes with whitespace (normalized)
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": [" 3 ", " 23 ", " 104 "]}'

# Larger set
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["3", "23", "104"]}'
```

**Expected**: All return `"decision": "YAY"`, `"failed_check": null`

---

## Edge Cases

```bash
# Empty strings in array
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["", "3"]}'

# Whitespace-only codes
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["   ", "3"]}'

# Non-existent numeric code
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["99999"]}'

# Mixed formatting
curl -X POST http://localhost:8000/api/compatibility/check \
  -H "Content-Type: application/json" \
  -d '{"codes": ["3", " 23 ", "104"]}'
```

---

## Running the Test Suite

### Automated Test Suite

```bash
./test_compatibility_api.sh
```

### Manual Testing

Use the curl commands above or use a tool like Postman/Insomnia.

---

## Finding Real Test Cases

To find actual codes with specific relations for testing:

```bash
# Find codes with generic_excludes (solo-only)
sqlite3 mbs.db "SELECT DISTINCT item_num FROM relations WHERE relation_type = 'generic_excludes';"

# Find codes with prerequisites
sqlite3 mbs.db "SELECT item_num, target_item_num FROM relations WHERE relation_type = 'prerequisite' LIMIT 5;"

# Find codes with same group_code (potential conflicts)
sqlite3 mbs.db "SELECT group_code, GROUP_CONCAT(item_num) as codes FROM items WHERE group_code IS NOT NULL GROUP BY group_code HAVING COUNT(*) > 1 LIMIT 5;"

# Find codes with excludes relations
sqlite3 mbs.db "SELECT item_num, target_item_num FROM relations WHERE relation_type = 'excludes' LIMIT 5;"

# Find codes with same_occasion constraint
sqlite3 mbs.db "SELECT item_num FROM constraints WHERE constraint_type = 'same_occasion' LIMIT 5;"
```

---

## Response Examples

### NAY Response (Invalid Code)

```json
{
  "decision": "NAY",
  "reason": "System Error: The code X999 is not a recognised MBS item number.",
  "failed_check": "P1",
  "details": {
    "invalid_codes": ["X999"]
  }
}
```

### NAY Response (Conflict)

```json
{
  "decision": "NAY",
  "reason": "Conflict: Only one Group T1 attendance item is payable. You have submitted both 23 and 36 which are in the same exclusion group.",
  "failed_check": "C1",
  "details": {
    "violations": [
      {
        "code1": "23",
        "code2": "36",
        "type": "group_conflict",
        "detail": "Both codes are in Group T1"
      }
    ]
  }
}
```

### YAY Response

```json
{
  "decision": "YAY",
  "reason": "Compatibility Passed: Based on MBS code rules, the submitted items are compatible for claiming together. (Note: External factors like patient history or provider type are not checked).",
  "failed_check": null,
  "details": null
}
```
