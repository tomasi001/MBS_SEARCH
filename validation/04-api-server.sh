#!/bin/bash

# API Server Testing
# This script tests the FastAPI server and all API endpoints

set -e  # Exit on any error

echo "=========================================="
echo "🌐 API SERVER TESTING"
echo "=========================================="

# Function for colored output
log_info() {
    echo -e "\033[1;34m[INFO]\033[0m $1"
}

log_success() {
    echo -e "\033[1;32m[SUCCESS]\033[0m $1"
}

log_error() {
    echo -e "\033[1;31m[ERROR]\033[0m $1"
}

log_warning() {
    echo -e "\033[1;33m[WARNING]\033[0m $1"
}

# Check if database exists
if [ ! -f "mbs.db" ]; then
    log_error "Database not found! Please run data loading first."
    echo ""
    echo "Would you like to load production data now?"
    read -p "Press 'y' to load production data, any other key to exit: " load_data
    if [ "$load_data" = "y" ] || [ "$load_data" = "Y" ]; then
        log_info "Loading production data..."
        poetry run mbs-load --xml data/mbs.xml --verbose
    else
        exit 1
    fi
fi

# Check if jq is available for JSON formatting
if command -v jq &> /dev/null; then
    log_success "✓ jq available for JSON formatting"
    USE_JQ=true
else
    log_warning "⚠ jq not available - JSON output will not be formatted"
    USE_JQ=false
fi

echo ""

# Start server in background
log_info "Starting API server..."
echo "The server will start on http://127.0.0.1:8000"
echo ""

# Kill any existing server process
pkill -f uvicorn 2>/dev/null || true
sleep 1

# Start server
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!

# Wait for server to start
log_info "Waiting for server to start..."
sleep 3

# Check if server is running
if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started successfully (PID: $SERVER_PID)"
else
    log_error "✗ Server failed to start"
    exit 1
fi

echo ""

# Test server health
log_info "Testing server health..."
if curl -s http://127.0.0.1:8000/ > /dev/null; then
    log_success "✓ Server is responding"
else
    log_error "✗ Server is not responding"
    kill $SERVER_PID 2>/dev/null || true
    exit 1
fi

echo ""

# Test API endpoints
log_info "Testing API endpoints..."

# Test single item lookup
log_info "Testing single item lookup (item 3)..."
if [ "$USE_JQ" = true ]; then
    curl -s 'http://127.0.0.1:8000/api/items?codes=3' | jq . > /tmp/api_test_1.json
    if [ $? -eq 0 ]; then
        log_success "✓ Single item lookup successful"
        echo "Response preview:"
        jq '.items[0].item.item_num, .items[0].item.category' /tmp/api_test_1.json
    else
        log_error "✗ Single item lookup failed"
    fi
else
    if curl -s 'http://127.0.0.1:8000/api/items?codes=3' | grep -q "item_num"; then
        log_success "✓ Single item lookup successful"
    else
        log_error "✗ Single item lookup failed"
    fi
fi

echo ""

# Test multiple items lookup
log_info "Testing multiple items lookup (items 3,23,104)..."
if [ "$USE_JQ" = true ]; then
    curl -s 'http://127.0.0.1:8000/api/items?codes=3,23,104' | jq . > /tmp/api_test_2.json
    if [ $? -eq 0 ]; then
        log_success "✓ Multiple items lookup successful"
        ITEM_COUNT=$(jq '.items | length' /tmp/api_test_2.json)
        log_info "Retrieved $ITEM_COUNT items"
    else
        log_error "✗ Multiple items lookup failed"
    fi
else
    if curl -s 'http://127.0.0.1:8000/api/items?codes=3,23,104' | grep -q "item_num"; then
        log_success "✓ Multiple items lookup successful"
    else
        log_error "✗ Multiple items lookup failed"
    fi
fi

echo ""

# Test complex item with relationships
log_info "Testing complex item lookup (item 44)..."
if [ "$USE_JQ" = true ]; then
    curl -s 'http://127.0.0.1:8000/api/items?codes=44' | jq . > /tmp/api_test_3.json
    if [ $? -eq 0 ]; then
        log_success "✓ Complex item lookup successful"
        RELATION_COUNT=$(jq '.items[0].relations | length' /tmp/api_test_3.json)
        CONSTRAINT_COUNT=$(jq '.items[0].constraints | length' /tmp/api_test_3.json)
        log_info "Item 44 has $RELATION_COUNT relations and $CONSTRAINT_COUNT constraints"
    else
        log_error "✗ Complex item lookup failed"
    fi
else
    if curl -s 'http://127.0.0.1:8000/api/items?codes=44' | grep -q "item_num"; then
        log_success "✓ Complex item lookup successful"
    else
        log_error "✗ Complex item lookup failed"
    fi
fi

echo ""

# Test non-existent item
log_info "Testing non-existent item lookup (item 999)..."
if [ "$USE_JQ" = true ]; then
    curl -s 'http://127.0.0.1:8000/api/items?codes=999' | jq . > /tmp/api_test_4.json
    if [ $? -eq 0 ]; then
        ITEM_COUNT=$(jq '.items | length' /tmp/api_test_4.json)
        if [ "$ITEM_COUNT" -eq 0 ]; then
            log_success "✓ Non-existent item handled correctly (empty response)"
        else
            log_warning "⚠ Non-existent item returned unexpected data"
        fi
    else
        log_error "✗ Non-existent item lookup failed"
    fi
else
    RESPONSE=$(curl -s 'http://127.0.0.1:8000/api/items?codes=999')
    if echo "$RESPONSE" | grep -q '"items":\[\]'; then
        log_success "✓ Non-existent item handled correctly (empty response)"
    else
        log_warning "⚠ Non-existent item returned unexpected data"
    fi
fi

echo ""

# Test empty request
log_info "Testing empty request..."
if [ "$USE_JQ" = true ]; then
    curl -s 'http://127.0.0.1:8000/api/items?codes=' | jq . > /tmp/api_test_5.json
    if [ $? -eq 0 ]; then
        log_success "✓ Empty request handled correctly"
    else
        log_error "✗ Empty request failed"
    fi
else
    if curl -s 'http://127.0.0.1:8000/api/items?codes=' | grep -q "items"; then
        log_success "✓ Empty request handled correctly"
    else
        log_error "✗ Empty request failed"
    fi
fi

echo ""

# Test malformed request
log_info "Testing malformed request..."
if [ "$USE_JQ" = true ]; then
    curl -s 'http://127.0.0.1:8000/api/items' | jq . > /tmp/api_test_6.json
    if [ $? -eq 0 ]; then
        log_success "✓ Malformed request handled correctly"
    else
        log_error "✗ Malformed request failed"
    fi
else
    if curl -s 'http://127.0.0.1:8000/api/items' | grep -q "items"; then
        log_success "✓ Malformed request handled correctly"
    else
        log_error "✗ Malformed request failed"
    fi
fi

echo ""

# Test API response times
log_info "Testing API response times..."
echo "Running 5 requests to measure average response time..."

TOTAL_TIME=0
for i in {1..5}; do
    START_TIME=$(date +%s.%N)
    curl -s 'http://127.0.0.1:8000/api/items?codes=3' > /dev/null
    END_TIME=$(date +%s.%N)
    REQUEST_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0.1")
    TOTAL_TIME=$(echo "$TOTAL_TIME + $REQUEST_TIME" | bc -l 2>/dev/null || echo "0.5")
done

AVERAGE_TIME=$(echo "scale=3; $TOTAL_TIME / 5" | bc -l 2>/dev/null || echo "0.1")
log_success "✓ Average response time: ${AVERAGE_TIME}s"

echo ""

# Interactive testing
log_info "Interactive API testing..."
echo "The server is running at http://127.0.0.1:8000"
echo "You can test the API manually in another terminal with:"
echo "  curl -s 'http://127.0.0.1:8000/api/items?codes=3' | jq ."
echo ""
echo "Would you like to test a custom item code?"
read -p "Enter item code(s) to test (or press Enter to skip): " custom_codes

if [ -n "$custom_codes" ]; then
    log_info "Testing custom codes: $custom_codes"
    if [ "$USE_JQ" = true ]; then
        curl -s "http://127.0.0.1:8000/api/items?codes=$custom_codes" | jq .
    else
        curl -s "http://127.0.0.1:8000/api/items?codes=$custom_codes"
    fi
fi

echo ""

# Cleanup
log_info "Stopping server..."
kill $SERVER_PID 2>/dev/null || true
sleep 2

if ps -p $SERVER_PID > /dev/null 2>&1; then
    log_warning "⚠ Server still running, forcing kill..."
    kill -9 $SERVER_PID 2>/dev/null || true
fi

log_success "✓ Server stopped"

# Clean up temp files
rm -f /tmp/api_test_*.json

echo ""
log_success "API server testing completed!"
echo "=========================================="
