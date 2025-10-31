#!/bin/bash
# Quick verification test for compatibility checker API

BASE_URL="${1:-http://localhost:8000}"
ENDPOINT="${BASE_URL}/api/compatibility/check"

echo "Testing MBS Compatibility Checker API"
echo "Endpoint: $ENDPOINT"
echo ""

# Test 1: Invalid code (should return NAY)
echo "Test 1: Invalid code (P1)"
response1=$(curl -s -X POST "$ENDPOINT" \
  -H "Content-Type: application/json" \
  -d '{"codes": ["X999"]}')
echo "Response: $response1"
if echo "$response1" | grep -q '"decision":"NAY"' && echo "$response1" | grep -q '"failed_check":"P1"'; then
    echo "✓ PASS"
else
    echo "✗ FAIL"
fi
echo ""

# Test 2: Single valid code (should return YAY)
echo "Test 2: Single valid code (YAY)"
response2=$(curl -s -X POST "$ENDPOINT" \
  -H "Content-Type: application/json" \
  -d '{"codes": ["3"]}')
echo "Response: $response2"
if echo "$response2" | grep -q '"decision":"YAY"'; then
    echo "✓ PASS"
else
    echo "✗ FAIL"
    echo "   Note: Code '3' might not exist in your database. Try another code."
fi
echo ""

# Test 3: Empty codes (should return NAY)
echo "Test 3: Empty codes array (P1)"
response3=$(curl -s -X POST "$ENDPOINT" \
  -H "Content-Type: application/json" \
  -d '{"codes": []}')
echo "Response: $response3"
if echo "$response3" | grep -q '"decision":"NAY"'; then
    echo "✓ PASS"
else
    echo "✗ FAIL"
fi
echo ""

echo "Quick test complete!"
echo "Run './find_test_codes.py' to find real codes for comprehensive testing."

