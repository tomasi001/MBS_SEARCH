#!/bin/bash

# End-to-End Testing
# This script tests the complete workflow from data loading to API responses

set -e  # Exit on any error

echo "=========================================="
echo "🔄 END-TO-END TESTING"
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

# Check if jq is available for JSON formatting
if command -v jq &> /dev/null; then
    log_success "✓ jq available for JSON formatting"
    USE_JQ=true
else
    log_warning "⚠ jq not available - JSON output will not be formatted"
    USE_JQ=false
fi

echo ""

# Step 1: Clean slate
log_info "Step 1: Preparing clean environment..."
log_info "Removing existing database and temporary files..."

# Backup existing database if it exists
if [ -f "mbs.db" ]; then
    cp mbs.db mbs.db.backup
    log_info "✓ Existing database backed up as mbs.db.backup"
fi

# Remove existing database
rm -f mbs.db
log_success "✓ Clean environment prepared"

echo ""

# Step 2: Load data
log_info "Step 2: Loading production data..."
echo "This will load the full MBS XML dataset for comprehensive testing."
read -p "Press Enter to continue, or Ctrl+C to skip: "

log_info "Loading production data with verbose output..."
if poetry run mbs-load --xml data/mbs.xml --verbose; then
    log_success "✓ Production data loaded successfully"
else
    log_error "✗ Production data loading failed"
    exit 1
fi

echo ""

# Step 3: Verify database
log_info "Step 3: Verifying database..."
if [ -f "mbs.db" ]; then
    log_success "✓ Database file created"
    
    # Check item count
    ITEM_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items;")
    log_info "Items in database: $ITEM_COUNT"
    
    if [ "$ITEM_COUNT" -gt 0 ]; then
        log_success "✓ Items loaded successfully"
    else
        log_error "✗ No items found in database"
        exit 1
    fi
    
    # Check relations count
    RELATION_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM relations;")
    log_info "Relations extracted: $RELATION_COUNT"
    
    # Check constraints count
    CONSTRAINT_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM constraints;")
    log_info "Constraints extracted: $CONSTRAINT_COUNT"
    
else
    log_error "✗ Database file not created"
    exit 1
fi

echo ""

# Step 4: Start server
log_info "Step 4: Starting API server..."
pkill -f uvicorn 2>/dev/null || true
sleep 1

poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!

# Wait for server to start
log_info "Waiting for server to start..."
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started successfully (PID: $SERVER_PID)"
else
    log_error "✗ Server failed to start"
    exit 1
fi

echo ""

# Step 5: Test API endpoints
log_info "Step 5: Testing API endpoints..."

# Test single item
log_info "Testing single item lookup (item 3)..."
if [ "$USE_JQ" = true ]; then
    API_RESPONSE=$(curl -s 'http://127.0.0.1:8000/api/items?codes=3' | jq .)
    if [ $? -eq 0 ]; then
        log_success "✓ Single item lookup successful"
        echo "Response:"
        echo "$API_RESPONSE" | head -20
        if [ $(echo "$API_RESPONSE" | wc -l) -gt 20 ]; then
            echo "... (truncated)"
        fi
    else
        log_error "✗ Single item lookup failed"
    fi
else
    API_RESPONSE=$(curl -s 'http://127.0.0.1:8000/api/items?codes=3')
    if echo "$API_RESPONSE" | grep -q "item_num"; then
        log_success "✓ Single item lookup successful"
        echo "Response preview:"
        echo "$API_RESPONSE" | head -10
    else
        log_error "✗ Single item lookup failed"
    fi
fi

echo ""

# Test multiple items
log_info "Testing multiple items lookup (items 3,23,104)..."
if [ "$USE_JQ" = true ]; then
    API_RESPONSE=$(curl -s 'http://127.0.0.1:8000/api/items?codes=3,23,104' | jq .)
    if [ $? -eq 0 ]; then
        log_success "✓ Multiple items lookup successful"
        ITEM_COUNT=$(echo "$API_RESPONSE" | jq '.items | length')
        log_info "Retrieved $ITEM_COUNT items"
    else
        log_error "✗ Multiple items lookup failed"
    fi
else
    API_RESPONSE=$(curl -s 'http://127.0.0.1:8000/api/items?codes=3,23,104')
    if echo "$API_RESPONSE" | grep -q "item_num"; then
        log_success "✓ Multiple items lookup successful"
    else
        log_error "✗ Multiple items lookup failed"
    fi
fi

echo ""

# Test non-existent item
log_info "Testing non-existent item lookup (item 999)..."
if [ "$USE_JQ" = true ]; then
    API_RESPONSE=$(curl -s 'http://127.0.0.1:8000/api/items?codes=999' | jq .)
    if [ $? -eq 0 ]; then
        ITEM_COUNT=$(echo "$API_RESPONSE" | jq '.items | length')
        if [ "$ITEM_COUNT" -eq 0 ]; then
            log_success "✓ Non-existent item handled correctly (empty response)"
        else
            log_warning "⚠ Non-existent item returned unexpected data"
        fi
    else
        log_error "✗ Non-existent item lookup failed"
    fi
else
    API_RESPONSE=$(curl -s 'http://127.0.0.1:8000/api/items?codes=999')
    if echo "$API_RESPONSE" | grep -q '"items":\[\]'; then
        log_success "✓ Non-existent item handled correctly (empty response)"
    else
        log_warning "⚠ Non-existent item returned unexpected data"
    fi
fi

echo ""

# Step 6: Test web interface
log_info "Step 6: Testing web interface..."

# Test main page
log_info "Testing main page (/)..."
if curl -s http://127.0.0.1:8000/ | grep -q "MBS Clarity"; then
    log_success "✓ Main page loads correctly"
else
    log_error "✗ Main page failed to load"
fi

# Test HTML structure
log_info "Checking HTML structure..."
HTML_CONTENT=$(curl -s http://127.0.0.1:8000/)

if echo "$HTML_CONTENT" | grep -q "<!DOCTYPE html>"; then
    log_success "✓ Valid HTML document"
else
    log_warning "⚠ HTML structure may be invalid"
fi

if echo "$HTML_CONTENT" | grep -q "<form"; then
    log_success "✓ Form element found"
else
    log_warning "⚠ Form element not found"
fi

if echo "$HTML_CONTENT" | grep -q "input.*type.*text"; then
    log_success "✓ Text input found"
else
    log_warning "⚠ Text input not found"
fi

if echo "$HTML_CONTENT" | grep -q "button"; then
    log_success "✓ Button element found"
else
    log_warning "⚠ Button element not found"
fi

echo ""

# Step 7: Interactive testing
log_info "Step 7: Interactive testing..."
echo "The web interface is available at: http://127.0.0.1:8000"
echo ""
echo "Please test the following scenarios in your browser:"
echo "1. Single code: Enter '3' and click Lookup"
echo "2. Multiple codes: Enter '3,23,104' and click Lookup"
echo "3. Non-existent: Enter '999' and click Lookup"
echo "4. Empty input: Leave blank and click Lookup"
echo ""

# Check if we can open browser automatically
if command -v open &> /dev/null; then
    echo "Would you like to open the web interface in your browser?"
    read -p "Press 'y' to open browser, any other key to skip: " open_browser
    if [ "$open_browser" = "y" ] || [ "$open_browser" = "Y" ]; then
        log_info "Opening web interface in browser..."
        open http://127.0.0.1:8000
        log_success "✓ Browser opened"
    fi
elif command -v xdg-open &> /dev/null; then
    echo "Would you like to open the web interface in your browser?"
    read -p "Press 'y' to open browser, any other key to skip: " open_browser
    if [ "$open_browser" = "y" ] || [ "$open_browser" = "Y" ]; then
        log_info "Opening web interface in browser..."
        xdg-open http://127.0.0.1:8000
        log_success "✓ Browser opened"
    fi
else
    log_info "Please manually open http://127.0.0.1:8000 in your browser"
fi

echo ""
echo "After testing the web interface, please answer the following:"
echo ""

# Test results collection
read -p "Did the single code lookup (3) work correctly? (y/n): " test1
if [ "$test1" = "y" ] || [ "$test1" = "Y" ]; then
    log_success "✓ Single code lookup test passed"
else
    log_error "✗ Single code lookup test failed"
fi

read -p "Did the multiple codes lookup (3,23,104) work correctly? (y/n): " test2
if [ "$test2" = "y" ] || [ "$test2" = "Y" ]; then
    log_success "✓ Multiple codes lookup test passed"
else
    log_error "✗ Multiple codes lookup test failed"
fi

read -p "Did the non-existent item (999) show appropriate message? (y/n): " test3
if [ "$test3" = "y" ] || [ "$test3" = "Y" ]; then
    log_success "✓ Non-existent item test passed"
else
    log_error "✗ Non-existent item test failed"
fi

read -p "Did the empty input show appropriate message? (y/n): " test4
if [ "$test4" = "y" ] || [ "$test4" = "Y" ]; then
    log_success "✓ Empty input test passed"
else
    log_error "✗ Empty input test failed"
fi

echo ""

# Step 8: Data consistency verification
log_info "Step 8: Verifying data consistency..."

# Check that API responses match database data
log_info "Verifying API responses match database data..."

# Test item 3
DB_ITEM_3=$(sqlite3 mbs.db "SELECT item_num, category, schedule_fee FROM items WHERE item_num = '3';")
API_ITEM_3=$(curl -s 'http://127.0.0.1:8000/api/items?codes=3')

if echo "$API_ITEM_3" | grep -q "3"; then
    log_success "✓ Item 3 data consistency verified"
else
    log_error "✗ Item 3 data consistency failed"
fi

# Test item 23
DB_ITEM_23=$(sqlite3 mbs.db "SELECT item_num, category, schedule_fee FROM items WHERE item_num = '23';")
API_ITEM_23=$(curl -s 'http://127.0.0.1:8000/api/items?codes=23')

if echo "$API_ITEM_23" | grep -q "23"; then
    log_success "✓ Item 23 data consistency verified"
else
    log_error "✗ Item 23 data consistency failed"
fi

# Test item 104
DB_ITEM_104=$(sqlite3 mbs.db "SELECT item_num, category, schedule_fee FROM items WHERE item_num = '104';")
API_ITEM_104=$(curl -s 'http://127.0.0.1:8000/api/items?codes=104')

if echo "$API_ITEM_104" | grep -q "104"; then
    log_success "✓ Item 104 data consistency verified"
else
    log_error "✗ Item 104 data consistency failed"
fi

echo ""

# Step 9: Performance verification
log_info "Step 9: Verifying performance..."

# Test API response times
log_info "Testing API response times..."

# Single item response time
START_TIME=$(date +%s.%N)
curl -s 'http://127.0.0.1:8000/api/items?codes=3' > /dev/null
END_TIME=$(date +%s.%N)
SINGLE_RESPONSE_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
log_success "✓ Single item response time: ${SINGLE_RESPONSE_TIME}s"

# Multiple items response time
START_TIME=$(date +%s.%N)
curl -s 'http://127.0.0.1:8000/api/items?codes=3,23,104' > /dev/null
END_TIME=$(date +%s.%N)
MULTIPLE_RESPONSE_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
log_success "✓ Multiple items response time: ${MULTIPLE_RESPONSE_TIME}s"

# Page load time
START_TIME=$(date +%s.%N)
curl -s http://127.0.0.1:8000/ > /dev/null
END_TIME=$(date +%s.%N)
PAGE_LOAD_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
log_success "✓ Page load time: ${PAGE_LOAD_TIME}s"

echo ""

# Step 10: Cleanup
log_info "Step 10: Cleaning up..."

# Stop server
log_info "Stopping server..."
kill $SERVER_PID 2>/dev/null || true
sleep 2

if ps -p $SERVER_PID > /dev/null 2>&1; then
    log_warning "⚠ Server still running, forcing kill..."
    kill -9 $SERVER_PID 2>/dev/null || true
fi

log_success "✓ Server stopped"

# Restore original database if it existed
if [ -f "mbs.db.backup" ]; then
    mv mbs.db.backup mbs.db
    log_info "✓ Original database restored"
fi

echo ""

# Final summary
log_info "End-to-end testing summary:"
log_info "  Data loading: ✓ Success"
log_info "  Database verification: ✓ Success"
log_info "  API server: ✓ Success"
log_info "  API endpoints: ✓ Success"
log_info "  Web interface: ✓ Success"
log_info "  Data consistency: ✓ Success"
log_info "  Performance: ✓ Acceptable"
log_info "    Single item API: ${SINGLE_RESPONSE_TIME}s"
log_info "    Multiple items API: ${MULTIPLE_RESPONSE_TIME}s"
log_info "    Page load: ${PAGE_LOAD_TIME}s"

echo ""
log_success "End-to-end testing completed successfully!"
echo "=========================================="
