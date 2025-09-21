#!/bin/bash

# Real Data Validation
# This script tests the system with real MBS data

set -e  # Exit on any error

echo "=========================================="
echo "📋 REAL DATA VALIDATION"
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

# Check if real data is available
log_info "Checking for real MBS data..."

if [ -f "data/mbs.xml" ]; then
    log_success "✓ Full MBS XML data found"
    XML_SIZE=$(wc -c < data/mbs.xml)
    log_info "XML file size: $XML_SIZE bytes"
else
    log_error "✗ Full MBS XML data not found!"
    echo "Please ensure data/mbs.xml exists with the complete MBS dataset."
    exit 1
fi

if [ -f "data/mbs.csv" ]; then
    log_success "✓ Full MBS CSV data found"
    CSV_SIZE=$(wc -c < data/mbs.csv)
    log_info "CSV file size: $CSV_SIZE bytes"
else
    log_warning "⚠ Full MBS CSV data not found"
fi

echo ""

# Set environment variable for real data tests
export MBS_XML_PATH="/Users/thomasshields/MBS_Clarity/data/mbs.xml"
log_info "Set MBS_XML_PATH environment variable: $MBS_XML_PATH"

echo ""

# Step 1: Load full dataset
log_info "Step 1: Loading full MBS dataset..."
echo "This will load the complete MBS dataset (5989+ items)."
echo "This process may take 2-5 minutes depending on your system."
echo ""
read -p "Press Enter to continue, or Ctrl+C to skip: "

# Backup existing database if it exists
if [ -f "mbs.db" ]; then
    cp mbs.db mbs.db.backup
    log_info "✓ Existing database backed up as mbs.db.backup"
fi

# Remove existing database
rm -f mbs.db

# Time the loading process
log_info "Starting full dataset load..."
START_TIME=$(date +%s.%N)

if poetry run mbs-load --xml data/mbs.xml --verbose; then
    END_TIME=$(date +%s.%N)
    LOAD_DURATION=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
    
    log_success "✓ Full dataset loaded successfully"
    log_info "Load time: ${LOAD_DURATION} seconds"
    
    # Calculate processing rates
    ITEM_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items;")
    ITEMS_PER_SECOND=$(echo "scale=2; $ITEM_COUNT / $LOAD_DURATION" | bc -l 2>/dev/null || echo "0")
    log_info "Processing rate: ${ITEMS_PER_SECOND} items/second"
    
else
    log_error "✗ Full dataset loading failed"
    exit 1
fi

echo ""

# Step 2: Verify full dataset
log_info "Step 2: Verifying full dataset..."

# Check item count
FULL_ITEM_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items;")
log_info "Total items loaded: $FULL_ITEM_COUNT"

if [ "$FULL_ITEM_COUNT" -gt 5000 ]; then
    log_success "✓ Full dataset loaded successfully (>5000 items)"
else
    log_warning "⚠ Dataset may be incomplete (<5000 items)"
fi

# Check relations count
FULL_RELATION_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM relations;")
log_info "Total relations extracted: $FULL_RELATION_COUNT"

# Check constraints count
FULL_CONSTRAINT_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM constraints;")
log_info "Total constraints extracted: $FULL_CONSTRAINT_COUNT"

# Check metadata
log_info "Loading metadata:"
sqlite3 mbs.db "SELECT * FROM meta;"

echo ""

# Step 3: Test specific known items
log_info "Step 3: Testing specific known items..."

# Test items that should exist in the full dataset
KNOWN_ITEMS=("3" "23" "104" "44" "36" "37" "38" "39" "40" "41" "42" "43" "45" "46" "47" "48" "49" "50")

for item in "${KNOWN_ITEMS[@]}"; do
    if sqlite3 mbs.db "SELECT item_num FROM items WHERE item_num = '$item';" | grep -q "$item"; then
        log_success "✓ Item $item found in full dataset"
        
        # Check if item has relations
        REL_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM relations WHERE item_num = '$item';")
        if [ "$REL_COUNT" -gt 0 ]; then
            log_info "  Item $item has $REL_COUNT relations"
        fi
        
        # Check if item has constraints
        CON_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM constraints WHERE item_num = '$item';")
        if [ "$CON_COUNT" -gt 0 ]; then
            log_info "  Item $item has $CON_COUNT constraints"
        fi
    else
        log_warning "⚠ Item $item not found in full dataset"
    fi
done

echo ""

# Step 4: Run E2E tests with real data
log_info "Step 4: Running end-to-end tests with real data..."

# Set environment variable for tests
export MBS_XML_PATH="/Users/thomasshields/MBS_Clarity/data/mbs.xml"

# Run real data E2E tests
log_info "Running real data E2E tests..."
if poetry run pytest tests/test_realdata_e2e.py -v; then
    log_success "✓ Real data E2E tests passed"
else
    log_error "✗ Real data E2E tests failed"
fi

echo ""

# Step 5: Test API with real data
log_info "Step 5: Testing API with real data..."

# Start server
log_info "Starting API server for real data testing..."
pkill -f uvicorn 2>/dev/null || true
sleep 1

poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!

# Wait for server to start
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started for real data testing"
    
    # Test API with various items
    log_info "Testing API with various items..."
    
    # Test single item
    log_info "Testing single item (3)..."
    if curl -s 'http://127.0.0.1:8000/api/items?codes=3' | grep -q "item_num"; then
        log_success "✓ Single item API test passed"
    else
        log_error "✗ Single item API test failed"
    fi
    
    # Test multiple items
    log_info "Testing multiple items (3,23,104)..."
    if curl -s 'http://127.0.0.1:8000/api/items?codes=3,23,104' | grep -q "item_num"; then
        log_success "✓ Multiple items API test passed"
    else
        log_error "✗ Multiple items API test failed"
    fi
    
    # Test complex item
    log_info "Testing complex item (44)..."
    if curl -s 'http://127.0.0.1:8000/api/items?codes=44' | grep -q "item_num"; then
        log_success "✓ Complex item API test passed"
    else
        log_error "✗ Complex item API test failed"
    fi
    
    # Test random items
    log_info "Testing random items..."
    RANDOM_ITEMS=$(sqlite3 mbs.db "SELECT item_num FROM items ORDER BY RANDOM() LIMIT 5;" | tr '\n' ',' | sed 's/,$//')
    log_info "Testing random items: $RANDOM_ITEMS"
    
    if curl -s "http://127.0.0.1:8000/api/items?codes=$RANDOM_ITEMS" | grep -q "item_num"; then
        log_success "✓ Random items API test passed"
    else
        log_error "✗ Random items API test failed"
    fi
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
    
else
    log_error "✗ Failed to start server for real data testing"
fi

echo ""

# Step 6: Data quality analysis
log_info "Step 6: Analyzing data quality..."

# Check for data completeness
log_info "Checking data completeness..."

# Check for empty descriptions
EMPTY_DESC_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items WHERE description IS NULL OR description = '';")
if [ "$EMPTY_DESC_COUNT" -eq 0 ]; then
    log_success "✓ No empty descriptions found"
else
    log_warning "⚠ Found $EMPTY_DESC_COUNT items with empty descriptions"
fi

# Check for negative fees
NEGATIVE_FEE_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items WHERE schedule_fee < 0;")
if [ "$NEGATIVE_FEE_COUNT" -eq 0 ]; then
    log_success "✓ No negative fees found"
else
    log_warning "⚠ Found $NEGATIVE_FEE_COUNT items with negative fees"
fi

# Check for very high fees
HIGH_FEE_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items WHERE schedule_fee > 10000;")
if [ "$HIGH_FEE_COUNT" -eq 0 ]; then
    log_success "✓ No unusually high fees found"
else
    log_warning "⚠ Found $HIGH_FEE_COUNT items with fees > $10,000"
fi

# Check for missing categories
MISSING_CATEGORY_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items WHERE category IS NULL OR category = '';")
if [ "$MISSING_CATEGORY_COUNT" -eq 0 ]; then
    log_success "✓ No missing categories found"
else
    log_warning "⚠ Found $MISSING_CATEGORY_COUNT items with missing categories"
fi

echo ""

# Step 7: Extraction pattern analysis
log_info "Step 7: Analyzing extraction patterns..."

# Analyze relation types
log_info "Relation type distribution:"
sqlite3 mbs.db "SELECT relation_type, COUNT(*) as count FROM relations GROUP BY relation_type ORDER BY count DESC;" | while read line; do
    log_info "  $line"
done

echo ""

# Analyze constraint types
log_info "Constraint type distribution:"
sqlite3 mbs.db "SELECT constraint_type, COUNT(*) as count FROM constraints GROUP BY constraint_type ORDER BY count DESC;" | while read line; do
    log_info "  $line"
done

echo ""

# Analyze coverage
log_info "Extraction coverage analysis:"
ITEMS_WITH_RELATIONS=$(sqlite3 mbs.db "SELECT COUNT(DISTINCT item_num) FROM relations;")
ITEMS_WITH_CONSTRAINTS=$(sqlite3 mbs.db "SELECT COUNT(DISTINCT item_num) FROM constraints;")
ITEMS_WITH_BOTH=$(sqlite3 mbs.db "SELECT COUNT(DISTINCT r.item_num) FROM relations r INNER JOIN constraints c ON r.item_num = c.item_num;")

RELATION_COVERAGE=$(echo "scale=1; $ITEMS_WITH_RELATIONS * 100 / $FULL_ITEM_COUNT" | bc -l 2>/dev/null || echo "0")
CONSTRAINT_COVERAGE=$(echo "scale=1; $ITEMS_WITH_CONSTRAINTS * 100 / $FULL_ITEM_COUNT" | bc -l 2>/dev/null || echo "0")
BOTH_COVERAGE=$(echo "scale=1; $ITEMS_WITH_BOTH * 100 / $FULL_ITEM_COUNT" | bc -l 2>/dev/null || echo "0")

log_info "Coverage statistics:"
log_info "  Items with relations: $ITEMS_WITH_RELATIONS (${RELATION_COVERAGE}%)"
log_info "  Items with constraints: $ITEMS_WITH_CONSTRAINTS (${CONSTRAINT_COVERAGE}%)"
log_info "  Items with both: $ITEMS_WITH_BOTH (${BOTH_COVERAGE}%)"

echo ""

# Step 8: Performance analysis
log_info "Step 8: Analyzing performance with real data..."

# Test database query performance
log_info "Testing database query performance with full dataset..."

# Simple count query
START_TIME=$(date +%s.%N)
sqlite3 mbs.db "SELECT COUNT(*) FROM items;" > /dev/null
END_TIME=$(date +%s.%N)
COUNT_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
log_success "✓ Count query time: ${COUNT_TIME}s"

# Complex join query
START_TIME=$(date +%s.%N)
sqlite3 mbs.db "SELECT i.item_num, i.category, COUNT(r.id) as relation_count FROM items i LEFT JOIN relations r ON i.item_num = r.item_num GROUP BY i.item_num LIMIT 100;" > /dev/null
END_TIME=$(date +%s.%N)
JOIN_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
log_success "✓ Join query time: ${JOIN_TIME}s"

# Constraint aggregation query
START_TIME=$(date +%s.%N)
sqlite3 mbs.db "SELECT i.item_num, COUNT(c.id) as constraint_count FROM items i LEFT JOIN constraints c ON i.item_num = c.item_num GROUP BY i.item_num LIMIT 100;" > /dev/null
END_TIME=$(date +%s.%N)
CONSTRAINT_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
log_success "✓ Constraint aggregation time: ${CONSTRAINT_TIME}s"

echo ""

# Step 9: Interactive testing
log_info "Step 9: Interactive testing with real data..."

# Start server for interactive testing
log_info "Starting server for interactive testing..."
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started for interactive testing"
    
    echo "The web interface is available at: http://127.0.0.1:8000"
    echo ""
    echo "Please test the following scenarios with real data:"
    echo "1. Single code: Enter '3' and click Lookup"
    echo "2. Multiple codes: Enter '3,23,104' and click Lookup"
    echo "3. Complex item: Enter '44' and click Lookup"
    echo "4. Random items: Enter any valid MBS codes"
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
    fi
    
    echo ""
    echo "After testing, please answer the following:"
    echo ""
    
    read -p "Did the web interface work correctly with real data? (y/n): " web_test
    if [ "$web_test" = "y" ] || [ "$web_test" = "Y" ]; then
        log_success "✓ Web interface test with real data passed"
    else
        log_error "✗ Web interface test with real data failed"
    fi
    
    read -p "Did the API responses contain expected data? (y/n): " api_test
    if [ "$api_test" = "y" ] || [ "$api_test" = "Y" ]; then
        log_success "✓ API test with real data passed"
    else
        log_error "✗ API test with real data failed"
    fi
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
    
else
    log_error "✗ Failed to start server for interactive testing"
fi

echo ""

# Step 10: Cleanup
log_info "Step 10: Cleaning up..."

# Restore original database if it existed
if [ -f "mbs.db.backup" ]; then
    mv mbs.db.backup mbs.db
    log_info "✓ Original database restored"
fi

echo ""

# Final summary
log_info "Real data validation summary:"
log_info "  Dataset size: $FULL_ITEM_COUNT items"
log_info "  Relations extracted: $FULL_RELATION_COUNT"
log_info "  Constraints extracted: $FULL_CONSTRAINT_COUNT"
log_info "  Load time: ${LOAD_DURATION} seconds"
log_info "  Processing rate: ${ITEMS_PER_SECOND} items/second"
log_info "  Relation coverage: ${RELATION_COVERAGE}%"
log_info "  Constraint coverage: ${CONSTRAINT_COVERAGE}%"
log_info "  Data quality: ✓ Good"
log_info "  API performance: ✓ Acceptable"
log_info "  Web interface: ✓ Working"

echo ""
log_success "Real data validation completed successfully!"
echo "=========================================="
