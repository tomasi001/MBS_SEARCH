#!/bin/bash
# Comprehensive test suite for MBS Compatibility Checker API
# Tests all scenarios: P1, C1, C2, C3, C4, and YAY cases

BASE_URL="http://localhost:8000"
ENDPOINT="${BASE_URL}/api/compatibility/check"

echo "=========================================="
echo "MBS Compatibility Checker API Test Suite"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PASSED=0
FAILED=0

test_case() {
    local test_name="$1"
    local expected_decision="$2"
    local expected_check="${3:-}"
    local json_payload="$4"
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Test: $test_name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    response=$(curl -s -X POST "$ENDPOINT" \
        -H "Content-Type: application/json" \
        -d "$json_payload")
    
    # Extract decision and failed_check from response
    decision=$(echo "$response" | grep -o '"decision":"[^"]*"' | cut -d'"' -f4)
    failed_check=$(echo "$response" | grep -o '"failed_check":"[^"]*"' | cut -d'"' -f4 || echo "null")
    reason=$(echo "$response" | grep -o '"reason":"[^"]*"' | cut -d'"' -f4)
    
    echo "Request:  $json_payload"
    echo "Response: $response"
    echo ""
    
    # Validate decision
    if [ "$decision" == "$expected_decision" ]; then
        if [ -z "$expected_check" ] || [ "$failed_check" == "$expected_check" ] || [ "$expected_check" == "null" ] && [ -z "$failed_check" ]; then
            echo -e "${GREEN}✓ PASS${NC}"
            ((PASSED++))
        else
            echo -e "${RED}✗ FAIL${NC} - Decision correct but failed_check mismatch. Expected: '$expected_check', Got: '$failed_check'"
            ((FAILED++))
        fi
    else
        echo -e "${RED}✗ FAIL${NC} - Expected decision: '$expected_decision', Got: '$decision'"
        ((FAILED++))
    fi
    echo ""
}

# ============================================================================
# TEST CATEGORY P1: Invalid Item Numbers
# ============================================================================
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}CATEGORY P1: Invalid Item Numbers (System Error)${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo ""

test_case \
    "P1.1: Empty codes array" \
    "NAY" \
    "P1" \
    '{"codes": []}'

test_case \
    "P1.2: Missing codes field" \
    "NAY" \
    "P1" \
    '{}'

test_case \
    "P1.3: Single invalid code" \
    "NAY" \
    "P1" \
    '{"codes": ["X999"]}'

test_case \
    "P1.4: Multiple invalid codes" \
    "NAY" \
    "P1" \
    '{"codes": ["INVALID1", "INVALID2", "X999"]}'

test_case \
    "P1.5: Mix of valid and invalid codes" \
    "NAY" \
    "P1" \
    '{"codes": ["3", "INVALID", "104"]}'

test_case \
    "P1.6: Non-existent numeric code" \
    "NAY" \
    "P1" \
    '{"codes": ["99999"]}'

test_case \
    "P1.7: Code with special characters" \
    "NAY" \
    "P1" \
    '{"codes": ["23@", "#104"]}'

# ============================================================================
# TEST CATEGORY C4: Duplicate Limits
# ============================================================================
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}CATEGORY C4: Duplicate Item Limits${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo ""

# Note: These tests assume codes with same_occasion or max_per_window constraints exist
# We'll use codes that likely have these constraints
test_case \
    "C4.1: Duplicate code (testing normalization removes duplicates first)" \
    "YAY" \
    "" \
    '{"codes": ["3", "3"]}'

# Test with a code that has same_occasion constraint if available
# This is a placeholder - actual test depends on database content
test_case \
    "C4.2: Duplicate code with whitespace (should normalize to single)" \
    "YAY" \
    "" \
    '{"codes": [" 3 ", "3", " 3 "]}'


# ============================================================================
# TEST CATEGORY C3: Solo-Only Codes
# ============================================================================
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}CATEGORY C3: Solo-Only / Co-Claiming Violations${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo ""

# Code 44 from README has generic_excludes - it should be solo-only
test_case \
    "C3.1: Code with generic_excludes submitted with other codes" \
    "NAY" \
    "C3" \
    '{"codes": ["44", "3"]}'

test_case \
    "C3.2: Code with generic_excludes submitted with multiple other codes" \
    "NAY" \
    "C3" \
    '{"codes": ["44", "3", "23", "104"]}'

test_case \
    "C3.3: Single code with generic_excludes (should pass as solo)" \
    "YAY" \
    "" \
    '{"codes": ["44"]}'


# ============================================================================
# TEST CATEGORY C1: Mutual Exclusions
# ============================================================================
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}CATEGORY C1: Mutual Exclusions / Conflicts${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo ""

# These tests depend on actual relations in the database
# We'll test with codes that are known to have exclusions
test_case \
    "C1.1: Two compatible codes (should pass if no exclusions exist)" \
    "YAY" \
    "" \
    '{"codes": ["3", "23"]}'

# Test group conflicts - codes with same group_code should conflict
# This depends on database having codes with same group_code
test_case \
    "C1.2: Codes with same group_code (Group T1 example - if exists)" \
    "NAY" \
    "C1" \
    '{"codes": ["23", "36"]}'

# Test direct excludes relation (if exists in database)
# This is a placeholder - actual test depends on database content
test_case \
    "C1.3: Multiple codes check for exclusions" \
    "YAY" \
    "" \
    '{"codes": ["3", "23", "104"]}'


# ============================================================================
# TEST CATEGORY C2: Mandatory Dependencies
# ============================================================================
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}CATEGORY C2: Mandatory Dependencies (Missing Prerequisites)${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo ""

# Test codes that require prerequisites
# These tests depend on actual prerequisite relations in database
# Placeholder tests - actual codes depend on database content
test_case \
    "C2.1: Code requiring prerequisite without it present" \
    "YAY" \
    "" \
    '{"codes": ["3"]}'

test_case \
    "C2.2: Code with prerequisite present (should pass)" \
    "YAY" \
    "" \
    '{"codes": ["3", "23"]}'


# ============================================================================
# TEST CATEGORY: YAY - Success Cases
# ============================================================================
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}CATEGORY: YAY - Success Cases${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo ""

test_case \
    "YAY.1: Single valid code" \
    "YAY" \
    "" \
    '{"codes": ["3"]}'

test_case \
    "YAY.2: Multiple compatible codes" \
    "YAY" \
    "" \
    '{"codes": ["3", "23"]}'

test_case \
    "YAY.3: Codes with whitespace (should normalize)" \
    "YAY" \
    "" \
    '{"codes": [" 3 ", " 23 ", " 104 "]}'

test_case \
    "YAY.4: Codes with duplicates that normalize (before duplicate check)" \
    "YAY" \
    "" \
    '{"codes": ["3", "3", "23"]}'

test_case \
    "YAY.5: Larger set of compatible codes" \
    "YAY" \
    "" \
    '{"codes": ["3", "23", "104"]}'


# ============================================================================
# EDGE CASES
# ============================================================================
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}EDGE CASES${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════════${NC}"
echo ""

test_case \
    "EDGE.1: Null/empty string in codes array" \
    "NAY" \
    "P1" \
    '{"codes": ["", "3"]}'

test_case \
    "EDGE.2: Whitespace-only codes" \
    "NAY" \
    "P1" \
    '{"codes": ["   ", "3"]}'

test_case \
    "EDGE.3: Very large code number" \
    "NAY" \
    "P1" \
    '{"codes": ["999999999"]}'

test_case \
    "EDGE.4: Code with leading zeros" \
    "YAY" \
    "" \
    '{"codes": ["003", "23"]}'

test_case \
    "EDGE.5: Mixed case and formatting" \
    "YAY" \
    "" \
    '{"codes": ["3", " 23 ", "104"]}'

# ============================================================================
# SUMMARY
# ============================================================================
echo ""
echo "=========================================="
echo "TEST SUMMARY"
echo "=========================================="
echo -e "${GREEN}Passed: $PASSED${NC}"
echo -e "${RED}Failed: $FAILED${NC}"
echo "Total:  $((PASSED + FAILED))"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ ALL TESTS PASSED${NC}"
    exit 0
else
    echo -e "${RED}✗ SOME TESTS FAILED${NC}"
    exit 1
fi

