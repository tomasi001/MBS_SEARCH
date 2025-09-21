#!/bin/bash

# Extraction Pattern Testing
# This script tests the relationship and constraint extraction patterns

set -e  # Exit on any error

echo "=========================================="
echo "🔍 EXTRACTION PATTERN TESTING"
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

echo ""

# Test duration extraction patterns
log_info "Testing duration extraction patterns..."
log_info "Items with duration constraints:"

DURATION_ITEMS=$(sqlite3 mbs.db "SELECT item_num, constraint_type, value FROM constraints WHERE constraint_type LIKE '%duration%' ORDER BY item_num;")
if [ -n "$DURATION_ITEMS" ]; then
    echo "$DURATION_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    DURATION_COUNT=$(echo "$DURATION_ITEMS" | wc -l)
    log_info "Total duration constraints: $DURATION_COUNT"
else
    log_warning "⚠ No duration constraints found"
fi

echo ""

# Test location extraction patterns
log_info "Testing location extraction patterns..."
log_info "Items with location constraints:"

LOCATION_ITEMS=$(sqlite3 mbs.db "SELECT item_num, constraint_type, value FROM constraints WHERE constraint_type = 'location' ORDER BY item_num;")
if [ -n "$LOCATION_ITEMS" ]; then
    echo "$LOCATION_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    LOCATION_COUNT=$(echo "$LOCATION_ITEMS" | wc -l)
    log_info "Total location constraints: $LOCATION_COUNT"
    
    # Show unique locations
    log_info "Unique locations found:"
    sqlite3 mbs.db "SELECT DISTINCT value FROM constraints WHERE constraint_type = 'location' ORDER BY value;" | while read location; do
        log_info "  - $location"
    done
else
    log_warning "⚠ No location constraints found"
fi

echo ""

# Test provider extraction patterns
log_info "Testing provider extraction patterns..."
log_info "Items with provider constraints:"

PROVIDER_ITEMS=$(sqlite3 mbs.db "SELECT item_num, constraint_type, value FROM constraints WHERE constraint_type = 'provider' ORDER BY item_num;")
if [ -n "$PROVIDER_ITEMS" ]; then
    echo "$PROVIDER_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    PROVIDER_COUNT=$(echo "$PROVIDER_ITEMS" | wc -l)
    log_info "Total provider constraints: $PROVIDER_COUNT"
    
    # Show unique providers
    log_info "Unique providers found:"
    sqlite3 mbs.db "SELECT DISTINCT value FROM constraints WHERE constraint_type = 'provider' ORDER BY value;" | while read provider; do
        log_info "  - $provider"
    done
else
    log_warning "⚠ No provider constraints found"
fi

echo ""

# Test frequency extraction patterns
log_info "Testing frequency extraction patterns..."
log_info "Items with frequency constraints:"

FREQUENCY_ITEMS=$(sqlite3 mbs.db "SELECT item_num, constraint_type, value FROM constraints WHERE constraint_type LIKE '%per_window%' OR constraint_type LIKE '%cooldown%' ORDER BY item_num;")
if [ -n "$FREQUENCY_ITEMS" ]; then
    echo "$FREQUENCY_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    FREQUENCY_COUNT=$(echo "$FREQUENCY_ITEMS" | wc -l)
    log_info "Total frequency constraints: $FREQUENCY_COUNT"
else
    log_warning "⚠ No frequency constraints found"
fi

echo ""

# Test age extraction patterns
log_info "Testing age extraction patterns..."
log_info "Items with age constraints:"

AGE_ITEMS=$(sqlite3 mbs.db "SELECT item_num, constraint_type, value FROM constraints WHERE constraint_type LIKE '%age%' ORDER BY item_num;")
if [ -n "$AGE_ITEMS" ]; then
    echo "$AGE_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    AGE_COUNT=$(echo "$AGE_ITEMS" | wc -l)
    log_info "Total age constraints: $AGE_COUNT"
else
    log_warning "⚠ No age constraints found"
fi

echo ""

# Test requirement extraction patterns
log_info "Testing requirement extraction patterns..."
log_info "Items with requirement constraints:"

REQUIREMENT_ITEMS=$(sqlite3 mbs.db "SELECT item_num, constraint_type, value FROM constraints WHERE constraint_type = 'requirement' ORDER BY item_num;")
if [ -n "$REQUIREMENT_ITEMS" ]; then
    echo "$REQUIREMENT_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    REQUIREMENT_COUNT=$(echo "$REQUIREMENT_ITEMS" | wc -l)
    log_info "Total requirement constraints: $REQUIREMENT_COUNT"
else
    log_warning "⚠ No requirement constraints found"
fi

echo ""

# Test referral extraction patterns
log_info "Testing referral extraction patterns..."
log_info "Items with referral constraints:"

REFERRAL_ITEMS=$(sqlite3 mbs.db "SELECT item_num, constraint_type, value FROM constraints WHERE constraint_type LIKE '%referral%' OR constraint_type LIKE '%attendance%' ORDER BY item_num;")
if [ -n "$REFERRAL_ITEMS" ]; then
    echo "$REFERRAL_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    REFERRAL_COUNT=$(echo "$REFERRAL_ITEMS" | wc -l)
    log_info "Total referral constraints: $REFERRAL_COUNT"
else
    log_warning "⚠ No referral constraints found"
fi

echo ""

# Test exclusion patterns
log_info "Testing exclusion patterns..."
log_info "Items with exclusion relations:"

EXCLUSION_ITEMS=$(sqlite3 mbs.db "SELECT item_num, relation_type, target_item_num FROM relations WHERE relation_type LIKE '%exclude%' ORDER BY item_num;")
if [ -n "$EXCLUSION_ITEMS" ]; then
    echo "$EXCLUSION_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    EXCLUSION_COUNT=$(echo "$EXCLUSION_ITEMS" | wc -l)
    log_info "Total exclusion relations: $EXCLUSION_COUNT"
else
    log_warning "⚠ No exclusion relations found"
fi

echo ""

# Test same-day patterns
log_info "Testing same-day patterns..."
log_info "Items with same-day relations:"

SAME_DAY_ITEMS=$(sqlite3 mbs.db "SELECT item_num, relation_type, target_item_num FROM relations WHERE relation_type LIKE '%same_day%' ORDER BY item_num;")
if [ -n "$SAME_DAY_ITEMS" ]; then
    echo "$SAME_DAY_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    SAME_DAY_COUNT=$(echo "$SAME_DAY_ITEMS" | wc -l)
    log_info "Total same-day relations: $SAME_DAY_COUNT"
else
    log_warning "⚠ No same-day relations found"
fi

echo ""

# Test prerequisite patterns
log_info "Testing prerequisite patterns..."
log_info "Items with prerequisite relations:"

PREREQUISITE_ITEMS=$(sqlite3 mbs.db "SELECT item_num, relation_type, target_item_num FROM relations WHERE relation_type = 'prerequisite' ORDER BY item_num;")
if [ -n "$PREREQUISITE_ITEMS" ]; then
    echo "$PREREQUISITE_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    PREREQUISITE_COUNT=$(echo "$PREREQUISITE_ITEMS" | wc -l)
    log_info "Total prerequisite relations: $PREREQUISITE_COUNT"
else
    log_warning "⚠ No prerequisite relations found"
fi

echo ""

# Test derived fee patterns
log_info "Testing derived fee patterns..."
log_info "Items with derived fee relations:"

DERIVED_FEE_ITEMS=$(sqlite3 mbs.db "SELECT item_num, relation_type, target_item_num FROM relations WHERE relation_type = 'derived_fee_ref' ORDER BY item_num;")
if [ -n "$DERIVED_FEE_ITEMS" ]; then
    echo "$DERIVED_FEE_ITEMS" | while read line; do
        log_success "  $line"
    done
    
    DERIVED_FEE_COUNT=$(echo "$DERIVED_FEE_ITEMS" | wc -l)
    log_info "Total derived fee relations: $DERIVED_FEE_COUNT"
else
    log_warning "⚠ No derived fee relations found"
fi

echo ""

# Pattern coverage analysis
log_info "Performing pattern coverage analysis..."

# Calculate coverage statistics
TOTAL_ITEMS=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items;")
ITEMS_WITH_RELATIONS=$(sqlite3 mbs.db "SELECT COUNT(DISTINCT item_num) FROM relations;")
ITEMS_WITH_CONSTRAINTS=$(sqlite3 mbs.db "SELECT COUNT(DISTINCT item_num) FROM constraints;")
ITEMS_WITH_BOTH=$(sqlite3 mbs.db "SELECT COUNT(DISTINCT r.item_num) FROM relations r INNER JOIN constraints c ON r.item_num = c.item_num;")

RELATION_COVERAGE=$(echo "scale=1; $ITEMS_WITH_RELATIONS * 100 / $TOTAL_ITEMS" | bc -l 2>/dev/null || echo "0")
CONSTRAINT_COVERAGE=$(echo "scale=1; $ITEMS_WITH_CONSTRAINTS * 100 / $TOTAL_ITEMS" | bc -l 2>/dev/null || echo "0")
BOTH_COVERAGE=$(echo "scale=1; $ITEMS_WITH_BOTH * 100 / $TOTAL_ITEMS" | bc -l 2>/dev/null || echo "0")

log_info "Pattern coverage statistics:"
log_info "  Total items: $TOTAL_ITEMS"
log_info "  Items with relations: $ITEMS_WITH_RELATIONS (${RELATION_COVERAGE}%)"
log_info "  Items with constraints: $ITEMS_WITH_CONSTRAINTS (${CONSTRAINT_COVERAGE}%)"
log_info "  Items with both: $ITEMS_WITH_BOTH (${BOTH_COVERAGE}%)"

echo ""

# Test specific complex items
log_info "Testing specific complex items..."

# Test item 44 (known to have complex patterns)
log_info "Analyzing item 44 (complex item):"
ITEM_44_RELATIONS=$(sqlite3 mbs.db "SELECT relation_type, target_item_num, detail FROM relations WHERE item_num = '44';")
ITEM_44_CONSTRAINTS=$(sqlite3 mbs.db "SELECT constraint_type, value FROM constraints WHERE item_num = '44';")

if [ -n "$ITEM_44_RELATIONS" ]; then
    log_success "Item 44 relations:"
    echo "$ITEM_44_RELATIONS" | while read line; do
        log_info "  $line"
    done
else
    log_warning "Item 44 has no relations"
fi

if [ -n "$ITEM_44_CONSTRAINTS" ]; then
    log_success "Item 44 constraints:"
    echo "$ITEM_44_CONSTRAINTS" | while read line; do
        log_info "  $line"
    done
else
    log_warning "Item 44 has no constraints"
fi

echo ""

# Pattern quality assessment
log_info "Performing pattern quality assessment..."

# Check for patterns that might be too broad
log_info "Checking for potentially over-broad patterns..."

# Check for very common constraint values
COMMON_CONSTRAINTS=$(sqlite3 mbs.db "SELECT constraint_type, value, COUNT(*) as count FROM constraints GROUP BY constraint_type, value HAVING count > 10 ORDER BY count DESC LIMIT 5;")
if [ -n "$COMMON_CONSTRAINTS" ]; then
    log_warning "Common constraint patterns (may need refinement):"
    echo "$COMMON_CONSTRAINTS" | while read line; do
        log_warning "  $line"
    done
fi

# Check for very common relation types
COMMON_RELATIONS=$(sqlite3 mbs.db "SELECT relation_type, COUNT(*) as count FROM relations GROUP BY relation_type ORDER BY count DESC LIMIT 5;")
if [ -n "$COMMON_RELATIONS" ]; then
    log_info "Most common relation types:"
    echo "$COMMON_RELATIONS" | while read line; do
        log_info "  $line"
    done
fi

echo ""

# Interactive pattern testing
log_info "Interactive pattern testing..."
echo "Would you like to test extraction patterns on a specific item?"
read -p "Enter item number to analyze (or press Enter to skip): " test_item

if [ -n "$test_item" ]; then
    log_info "Analyzing item $test_item..."
    
    # Check if item exists
    if sqlite3 mbs.db "SELECT item_num FROM items WHERE item_num = '$test_item';" | grep -q "$test_item"; then
        log_success "Item $test_item found"
        
        # Show item details
        log_info "Item details:"
        sqlite3 mbs.db "SELECT item_num, category, schedule_fee, description FROM items WHERE item_num = '$test_item';" | while read line; do
            log_info "  $line"
        done
        
        # Show relations
        log_info "Relations:"
        sqlite3 mbs.db "SELECT relation_type, target_item_num, detail FROM relations WHERE item_num = '$test_item';" | while read line; do
            log_success "  $line"
        done
        
        # Show constraints
        log_info "Constraints:"
        sqlite3 mbs.db "SELECT constraint_type, value FROM constraints WHERE item_num = '$test_item';" | while read line; do
            log_success "  $line"
        done
    else
        log_error "Item $test_item not found in database"
    fi
fi

echo ""
log_success "Extraction pattern testing completed!"
echo "=========================================="
