#!/bin/bash

# Data Loading Pipeline Testing
# This script tests the data loading functionality with production datasets

set -e  # Exit on any error

echo "=========================================="
echo "📊 DATA LOADING PIPELINE TESTING"
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

# Check if data files exist
log_info "Checking data files..."
if [ -f "data/mbs.xml" ]; then
    log_success "✓ Full XML data found"
    XML_SIZE=$(wc -c < data/mbs.xml)
    log_info "Full XML data size: $XML_SIZE bytes"
else
    log_error "✗ Full XML data not found!"
    exit 1
fi

echo ""

# Test Production Data Loading
log_info "Testing production data loading..."
log_info "This will load the full MBS XML dataset for comprehensive testing."
echo ""
read -p "Press Enter to continue, or Ctrl+C to skip: "

log_info "Loading production data with verbose output..."
if poetry run python -m mbs_clarity._loader --xml data/mbs.xml --verbose; then
    log_success "✓ Production data loaded successfully"
else
    log_error "✗ Production data loading failed"
    exit 1
fi

echo ""

# Verify production database
log_info "Verifying production database..."
if [ -f "mbs.db" ]; then
    log_success "✓ Database file created"
    
    # Check item count
    ITEM_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items;")
    log_info "Items in database: $ITEM_COUNT"
    
    if [ "$ITEM_COUNT" -gt 1000 ]; then
        log_success "✓ Production dataset loaded successfully (${ITEM_COUNT} items)"
        
        # Show production items
        log_info "Production items loaded:"
        sqlite3 mbs.db "SELECT item_num, category, schedule_fee FROM items ORDER BY CAST(item_num AS INTEGER) LIMIT 10;"
    else
        log_warning "⚠ Low item count - may not be production data"
    fi
    
    # Check relations count
    RELATION_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM relations;")
    log_info "Relations extracted: $RELATION_COUNT"
    
    # Check constraints count
    CONSTRAINT_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM constraints;")
    log_info "Constraints extracted: $CONSTRAINT_COUNT"
    
    # Show metadata
    log_info "Loading metadata:"
    sqlite3 mbs.db "SELECT * FROM meta;"
    
else
    log_error "✗ Database file not created"
    exit 1
fi

echo ""

# Test specific items exist
log_info "Testing specific item lookups..."
TEST_ITEMS=("3" "23" "104" "44" "600" "800" "900")
for item in "${TEST_ITEMS[@]}"; do
    if sqlite3 mbs.db "SELECT item_num FROM items WHERE item_num = '$item';" | grep -q "$item"; then
        log_success "✓ Item $item found in database"
    else
        log_warning "⚠ Item $item not found in database"
    fi
done

echo ""

# Test relationship extraction
log_info "Testing relationship extraction..."
RELATION_TYPES=$(sqlite3 mbs.db "SELECT DISTINCT relation_type FROM relations LIMIT 5;")
log_info "Relation types found:"
echo "$RELATION_TYPES"

CONSTRAINT_TYPES=$(sqlite3 mbs.db "SELECT DISTINCT constraint_type FROM constraints LIMIT 10;")
log_info "Constraint types found:"
echo "$CONSTRAINT_TYPES"

echo ""
log_success "Production data loading pipeline testing completed!"
echo "=========================================="