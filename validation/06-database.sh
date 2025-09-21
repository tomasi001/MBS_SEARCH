#!/bin/bash

# Database Validation
# This script validates database schema and data integrity

set -e  # Exit on any error

echo "=========================================="
echo "🗄️  DATABASE VALIDATION"
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

log_success "✓ Database file found: mbs.db"

echo ""

# Check database file size
log_info "Checking database file size..."
DB_SIZE=$(du -h mbs.db | cut -f1)
log_info "Database size: $DB_SIZE"

echo ""

# Schema Validation
log_info "Validating database schema..."

# Check if sqlite3 is available
if ! command -v sqlite3 &> /dev/null; then
    log_error "sqlite3 command not found! Please install SQLite."
    exit 1
fi

# Check all tables exist
log_info "Checking required tables..."
REQUIRED_TABLES=("items" "relations" "constraints" "meta")

for table in "${REQUIRED_TABLES[@]}"; do
    if sqlite3 mbs.db ".tables" | grep -q "$table"; then
        log_success "✓ Table '$table' exists"
    else
        log_error "✗ Table '$table' missing!"
        exit 1
    fi
done

echo ""

# Check table schemas
log_info "Validating table schemas..."

# Items table schema
log_info "Checking items table schema..."
ITEMS_SCHEMA=$(sqlite3 mbs.db ".schema items")
if echo "$ITEMS_SCHEMA" | grep -q "item_num.*PRIMARY KEY"; then
    log_success "✓ items table has correct primary key"
else
    log_error "✗ items table primary key issue"
fi

if echo "$ITEMS_SCHEMA" | grep -q "schedule_fee.*REAL"; then
    log_success "✓ items table has schedule_fee field"
else
    log_warning "⚠ items table schedule_fee field issue"
fi

# Relations table schema
log_info "Checking relations table schema..."
RELATIONS_SCHEMA=$(sqlite3 mbs.db ".schema relations")
if echo "$RELATIONS_SCHEMA" | grep -q "id.*PRIMARY KEY"; then
    log_success "✓ relations table has correct primary key"
else
    log_error "✗ relations table primary key issue"
fi

if echo "$RELATIONS_SCHEMA" | grep -q "item_num.*NOT NULL"; then
    log_success "✓ relations table has required item_num field"
else
    log_error "✗ relations table item_num field issue"
fi

# Constraints table schema
log_info "Checking constraints table schema..."
CONSTRAINTS_SCHEMA=$(sqlite3 mbs.db ".schema constraints")
if echo "$CONSTRAINTS_SCHEMA" | grep -q "id.*PRIMARY KEY"; then
    log_success "✓ constraints table has correct primary key"
else
    log_error "✗ constraints table primary key issue"
fi

if echo "$CONSTRAINTS_SCHEMA" | grep -q "item_num.*NOT NULL"; then
    log_success "✓ constraints table has required item_num field"
else
    log_error "✗ constraints table item_num field issue"
fi

# Meta table schema
log_info "Checking meta table schema..."
META_SCHEMA=$(sqlite3 mbs.db ".schema meta")
if echo "$META_SCHEMA" | grep -q "id.*PRIMARY KEY"; then
    log_success "✓ meta table has correct primary key"
else
    log_error "✗ meta table primary key issue"
fi

echo ""

# Data Integrity Checks
log_info "Performing data integrity checks..."

# Check item counts
log_info "Checking item counts..."
ITEM_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items;")
log_info "Total items: $ITEM_COUNT"

if [ "$ITEM_COUNT" -gt 0 ]; then
    log_success "✓ Items table has data"
else
    log_error "✗ Items table is empty"
    exit 1
fi

# Check for duplicate items
log_info "Checking for duplicate items..."
DUPLICATE_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM (SELECT item_num, COUNT(*) as cnt FROM items GROUP BY item_num HAVING cnt > 1);")
if [ "$DUPLICATE_COUNT" -eq 0 ]; then
    log_success "✓ No duplicate items found"
else
    log_error "✗ Found $DUPLICATE_COUNT duplicate items"
fi

# Check relation counts
log_info "Checking relation counts..."
RELATION_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM relations;")
log_info "Total relations: $RELATION_COUNT"

# Check constraint counts
log_info "Checking constraint counts..."
CONSTRAINT_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM constraints;")
log_info "Total constraints: $CONSTRAINT_COUNT"

echo ""

# Check for orphaned relations
log_info "Checking for orphaned relations..."
ORPHANED_RELATIONS=$(sqlite3 mbs.db "SELECT COUNT(*) FROM relations r LEFT JOIN items i ON r.item_num = i.item_num WHERE i.item_num IS NULL;")
if [ "$ORPHANED_RELATIONS" -eq 0 ]; then
    log_success "✓ No orphaned relations found"
else
    log_error "✗ Found $ORPHANED_RELATIONS orphaned relations"
fi

# Check for orphaned constraints
log_info "Checking for orphaned constraints..."
ORPHANED_CONSTRAINTS=$(sqlite3 mbs.db "SELECT COUNT(*) FROM constraints c LEFT JOIN items i ON c.item_num = i.item_num WHERE i.item_num IS NULL;")
if [ "$ORPHANED_CONSTRAINTS" -eq 0 ]; then
    log_success "✓ No orphaned constraints found"
else
    log_error "✗ Found $ORPHANED_CONSTRAINTS orphaned constraints"
fi

echo ""

# Check relation types
log_info "Checking relation types..."
log_info "Available relation types:"
sqlite3 mbs.db "SELECT DISTINCT relation_type, COUNT(*) as count FROM relations GROUP BY relation_type ORDER BY count DESC;" | while read line; do
    log_info "  $line"
done

echo ""

# Check constraint types
log_info "Checking constraint types..."
log_info "Available constraint types:"
sqlite3 mbs.db "SELECT DISTINCT constraint_type, COUNT(*) as count FROM constraints GROUP BY constraint_type ORDER BY count DESC;" | while read line; do
    log_info "  $line"
done

echo ""

# Check metadata
log_info "Checking metadata..."
log_info "Metadata entries:"
sqlite3 mbs.db "SELECT * FROM meta;" | while read line; do
    log_info "  $line"
done

echo ""

# Production data validation
log_info "Validating production data..."

# Check specific items exist
TEST_ITEMS=("3" "23" "104" "44")
for item in "${TEST_ITEMS[@]}"; do
    if sqlite3 mbs.db "SELECT item_num FROM items WHERE item_num = '$item';" | grep -q "$item"; then
        log_success "✓ Item $item found in database"
        
        # Check if item has relations
        REL_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM relations WHERE item_num = '$item';")
        log_info "  Item $item has $REL_COUNT relations"
        
        # Check if item has constraints
        CON_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM constraints WHERE item_num = '$item';")
        log_info "  Item $item has $CON_COUNT constraints"
    else
        log_warning "⚠ Item $item not found in database"
    fi
done

echo ""

# Data quality checks
log_info "Performing data quality checks..."

# Check for empty descriptions
log_info "Checking for empty descriptions..."
EMPTY_DESC_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items WHERE description IS NULL OR description = '';")
if [ "$EMPTY_DESC_COUNT" -eq 0 ]; then
    log_success "✓ No empty descriptions found"
else
    log_warning "⚠ Found $EMPTY_DESC_COUNT items with empty descriptions"
fi

# Check for negative fees
log_info "Checking for negative fees..."
NEGATIVE_FEE_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items WHERE schedule_fee < 0;")
if [ "$NEGATIVE_FEE_COUNT" -eq 0 ]; then
    log_success "✓ No negative fees found"
else
    log_warning "⚠ Found $NEGATIVE_FEE_COUNT items with negative fees"
fi

# Check for very high fees
log_info "Checking for unusually high fees..."
HIGH_FEE_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items WHERE schedule_fee > 10000;")
if [ "$HIGH_FEE_COUNT" -eq 0 ]; then
    log_success "✓ No unusually high fees found"
else
    log_warning "⚠ Found $HIGH_FEE_COUNT items with fees > $10,000"
fi

echo ""

# Performance checks
log_info "Performing performance checks..."

# Test query performance
log_info "Testing query performance..."
START_TIME=$(date +%s.%N)
sqlite3 mbs.db "SELECT COUNT(*) FROM items;" > /dev/null
END_TIME=$(date +%s.%N)
QUERY_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0.001")
log_success "✓ Basic query time: ${QUERY_TIME}s"

# Test complex query performance
log_info "Testing complex query performance..."
START_TIME=$(date +%s.%N)
sqlite3 mbs.db "SELECT i.item_num, i.category, COUNT(r.id) as relation_count FROM items i LEFT JOIN relations r ON i.item_num = r.item_num GROUP BY i.item_num LIMIT 100;" > /dev/null
END_TIME=$(date +%s.%N)
COMPLEX_QUERY_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0.001")
log_success "✓ Complex query time: ${COMPLEX_QUERY_TIME}s"

echo ""

# Database optimization suggestions
log_info "Database optimization analysis..."

# Check if indexes exist
log_info "Checking database indexes..."
INDEXES=$(sqlite3 mbs.db ".indexes")
if echo "$INDEXES" | grep -q "idx_"; then
    log_success "✓ Custom indexes found"
    echo "$INDEXES" | grep "idx_" | while read index; do
        log_info "  $index"
    done
else
    log_warning "⚠ No custom indexes found - consider adding indexes for better performance"
    echo ""
    echo "Would you like to add performance indexes?"
    read -p "Press 'y' to add indexes, any other key to skip: " add_indexes
    if [ "$add_indexes" = "y" ] || [ "$add_indexes" = "Y" ]; then
        log_info "Adding performance indexes..."
        sqlite3 mbs.db "CREATE INDEX IF NOT EXISTS idx_relations_item_num ON relations(item_num);"
        sqlite3 mbs.db "CREATE INDEX IF NOT EXISTS idx_constraints_item_num ON constraints(item_num);"
        sqlite3 mbs.db "CREATE INDEX IF NOT EXISTS idx_items_category ON items(category);"
        log_success "✓ Performance indexes added"
    fi
fi

echo ""

# Final summary
log_info "Database validation summary:"
log_info "  Items: $ITEM_COUNT"
log_info "  Relations: $RELATION_COUNT"
log_info "  Constraints: $CONSTRAINT_COUNT"
log_info "  Database size: $DB_SIZE"
log_info "  Query performance: ${QUERY_TIME}s"

echo ""
log_success "Database validation completed!"
echo "=========================================="
