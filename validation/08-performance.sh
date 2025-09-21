#!/bin/bash

# Performance Testing
# This script tests system performance and optimization

set -e  # Exit on any error

echo "=========================================="
echo "⚡ PERFORMANCE TESTING"
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

# Load Performance Testing
log_info "Testing data loading performance..."

# Check if full dataset is available
if [ -f "data/mbs.xml" ]; then
    log_info "Full dataset available - testing load performance"
    echo "This will measure the time to load the complete MBS dataset."
    echo "Warning: This will overwrite the current database!"
    echo ""
    read -p "Press 'y' to proceed with full dataset load test, any other key to skip: " load_test
    
    if [ "$load_test" = "y" ] || [ "$load_test" = "Y" ]; then
        # Backup current database
        if [ -f "mbs.db" ]; then
            cp mbs.db mbs.db.backup
            log_info "✓ Current database backed up as mbs.db.backup"
        fi
        
        # Remove existing database
        rm -f mbs.db
        
        # Time the loading process
        log_info "Starting full dataset load test..."
        START_TIME=$(date +%s.%N)
        
        if poetry run mbs-load --xml data/mbs.xml --verbose; then
            END_TIME=$(date +%s.%N)
            LOAD_DURATION=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
            
            log_success "✓ Full dataset loaded successfully"
            log_info "Load time: ${LOAD_DURATION} seconds"
            
            # Calculate items per second
            ITEM_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items;")
            ITEMS_PER_SECOND=$(echo "scale=2; $ITEM_COUNT / $LOAD_DURATION" | bc -l 2>/dev/null || echo "0")
            log_info "Processing rate: ${ITEMS_PER_SECOND} items/second"
            
            # Calculate relations per second
            RELATION_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM relations;")
            RELATIONS_PER_SECOND=$(echo "scale=2; $RELATION_COUNT / $LOAD_DURATION" | bc -l 2>/dev/null || echo "0")
            log_info "Relation extraction rate: ${RELATIONS_PER_SECOND} relations/second"
            
            # Calculate constraints per second
            CONSTRAINT_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM constraints;")
            CONSTRAINTS_PER_SECOND=$(echo "scale=2; $CONSTRAINT_COUNT / $LOAD_DURATION" | bc -l 2>/dev/null || echo "0")
            log_info "Constraint extraction rate: ${CONSTRAINTS_PER_SECOND} constraints/second"
            
        else
            log_error "✗ Full dataset load test failed"
            # Restore backup
            if [ -f "mbs.db.backup" ]; then
                mv mbs.db.backup mbs.db
                log_info "✓ Database restored from backup"
            fi
        fi
    else
        log_info "Skipping full dataset load test"
    fi
else
    log_info "Full dataset not available - cannot test load performance"
    log_warning "⚠ Full MBS XML dataset required for performance testing"
fi

echo ""

# Database Query Performance Testing
log_info "Testing database query performance..."

# Test basic queries
log_info "Testing basic query performance..."

# Simple count query
START_TIME=$(date +%s.%N)
sqlite3 mbs.db "SELECT COUNT(*) FROM items;" > /dev/null
END_TIME=$(date +%s.%N)
COUNT_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
log_success "✓ Count query time: ${COUNT_TIME}s"

# Simple select query
START_TIME=$(date +%s.%N)
sqlite3 mbs.db "SELECT item_num, category FROM items LIMIT 100;" > /dev/null
END_TIME=$(date +%s.%N)
SELECT_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
log_success "✓ Select query time: ${SELECT_TIME}s"

# Complex join query
log_info "Testing complex query performance..."
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

# API Performance Testing
log_info "Testing API performance..."

# Start server in background
log_info "Starting API server for performance testing..."
pkill -f uvicorn 2>/dev/null || true
sleep 1

poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!

# Wait for server to start with timeout
log_info "Waiting for server to start..."
for i in {1..10}; do
    if curl -s 'http://127.0.0.1:8000/api/items?codes=3' > /dev/null 2>&1; then
        log_success "✓ Server is responding"
        break
    fi
    sleep 1
    if [ $i -eq 10 ]; then
        log_error "✗ Server failed to start within 10 seconds"
        kill $SERVER_PID 2>/dev/null || true
        exit 1
    fi
done

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started for performance testing"
    
    # Test API response times
    log_info "Testing API response times..."
    
    # Single item request
    log_info "Testing single item API request..."
    START_TIME=$(date +%s.%N)
    curl -s 'http://127.0.0.1:8000/api/items?codes=3' > /dev/null
    END_TIME=$(date +%s.%N)
    SINGLE_API_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
    log_success "✓ Single item API time: ${SINGLE_API_TIME}s"
    
    # Multiple items request
    log_info "Testing multiple items API request..."
    START_TIME=$(date +%s.%N)
    curl -s 'http://127.0.0.1:8000/api/items?codes=3,23,104' > /dev/null
    END_TIME=$(date +%s.%N)
    MULTIPLE_API_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
    log_success "✓ Multiple items API time: ${MULTIPLE_API_TIME}s"
    
    # Complex item request
    log_info "Testing complex item API request..."
    START_TIME=$(date +%s.%N)
    curl -s 'http://127.0.0.1:8000/api/items?codes=44' > /dev/null
    END_TIME=$(date +%s.%N)
    COMPLEX_API_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
    log_success "✓ Complex item API time: ${COMPLEX_API_TIME}s"
    
    # Load testing
    log_info "Running load test (10 concurrent requests)..."
    START_TIME=$(date +%s.%N)
    
    # Use a more robust approach with timeout
    (
        for i in {1..10}; do
            curl -s 'http://127.0.0.1:8000/api/items?codes=3' > /dev/null &
        done
        wait
    ) &
    
    LOAD_TEST_PID=$!
    
    # Wait with timeout (max 30 seconds)
    for i in {1..30}; do
        if ! kill -0 $LOAD_TEST_PID 2>/dev/null; then
            break
        fi
        sleep 1
    done
    
    # Kill the load test if it's still running
    kill $LOAD_TEST_PID 2>/dev/null || true
    
    END_TIME=$(date +%s.%N)
    LOAD_TEST_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
    log_success "✓ Load test time (10 requests): ${LOAD_TEST_TIME}s"
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
    
else
    log_error "✗ Failed to start server for performance testing"
fi

echo ""

# Memory Usage Testing
log_info "Testing memory usage..."

# Check if psutil is available for memory monitoring
if poetry run python -c "import psutil" 2>/dev/null; then
    log_info "Monitoring memory usage during operations..."
    
    # Get initial memory usage
    INITIAL_MEMORY=$(poetry run python -c "import psutil; print(psutil.virtual_memory().percent)")
    log_info "Initial memory usage: ${INITIAL_MEMORY}%"
    
    # Test memory usage during database operations
    log_info "Testing memory usage during database operations..."
    
    # Start server and measure memory
    poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
    SERVER_PID=$!
    
    # Wait for server to start with timeout
    log_info "Waiting for server to start for memory testing..."
    for i in {1..10}; do
        if curl -s 'http://127.0.0.1:8000/api/items?codes=3' > /dev/null 2>&1; then
            log_success "✓ Server is responding for memory testing"
            break
        fi
        sleep 1
        if [ $i -eq 10 ]; then
            log_error "✗ Server failed to start for memory testing"
            kill $SERVER_PID 2>/dev/null || true
            break
        fi
    done
    
    if ps -p $SERVER_PID > /dev/null; then
        SERVER_MEMORY=$(poetry run python -c "import psutil; print(psutil.virtual_memory().percent)")
        log_info "Memory usage with server running: ${SERVER_MEMORY}%"
        
        # Test memory during API calls
        for i in {1..5}; do
            curl -s 'http://127.0.0.1:8000/api/items?codes=3' > /dev/null
        done
        
        API_MEMORY=$(poetry run python -c "import psutil; print(psutil.virtual_memory().percent)")
        log_info "Memory usage after API calls: ${API_MEMORY}%"
        
        kill $SERVER_PID 2>/dev/null || true
    fi
    
else
    log_warning "⚠ psutil not available - cannot monitor memory usage"
fi

echo ""

# Database Optimization Testing
log_info "Testing database optimization..."

# Check current indexes
log_info "Checking current database indexes..."
CURRENT_INDEXES=$(sqlite3 mbs.db ".indexes")
if echo "$CURRENT_INDEXES" | grep -q "idx_"; then
    log_success "✓ Custom indexes found"
    echo "$CURRENT_INDEXES" | grep "idx_" | while read index; do
        log_info "  $index"
    done
else
    log_warning "⚠ No custom indexes found"
    
    echo "Would you like to add performance indexes?"
    read -p "Press 'y' to add indexes, any other key to skip: " add_indexes
    if [ "$add_indexes" = "y" ] || [ "$add_indexes" = "Y" ]; then
        log_info "Adding performance indexes..."
        
        # Time index creation
        START_TIME=$(date +%s.%N)
        
        sqlite3 mbs.db "CREATE INDEX IF NOT EXISTS idx_relations_item_num ON relations(item_num);"
        sqlite3 mbs.db "CREATE INDEX IF NOT EXISTS idx_constraints_item_num ON constraints(item_num);"
        sqlite3 mbs.db "CREATE INDEX IF NOT EXISTS idx_items_category ON items(category);"
        sqlite3 mbs.db "CREATE INDEX IF NOT EXISTS idx_items_schedule_fee ON items(schedule_fee);"
        
        END_TIME=$(date +%s.%N)
        INDEX_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
        
        log_success "✓ Performance indexes added in ${INDEX_TIME}s"
        
        # Test performance improvement
        log_info "Testing performance improvement with indexes..."
        
        START_TIME=$(date +%s.%N)
        sqlite3 mbs.db "SELECT i.item_num, COUNT(r.id) as relation_count FROM items i LEFT JOIN relations r ON i.item_num = r.item_num GROUP BY i.item_num LIMIT 100;" > /dev/null
        END_TIME=$(date +%s.%N)
        INDEXED_QUERY_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
        
        log_success "✓ Indexed query time: ${INDEXED_QUERY_TIME}s"
        
        # Compare with previous time
        if (( $(echo "$INDEXED_QUERY_TIME < $JOIN_TIME" | bc -l 2>/dev/null || echo "0") )); then
            IMPROVEMENT=$(echo "scale=2; ($JOIN_TIME - $INDEXED_QUERY_TIME) / $JOIN_TIME * 100" | bc -l 2>/dev/null || echo "0")
            log_success "✓ Performance improved by ${IMPROVEMENT}%"
        else
            log_warning "⚠ No significant performance improvement detected"
        fi
    fi
fi

echo ""

# Performance Summary
log_info "Performance testing summary:"
log_info "  Database queries:"
log_info "    Count query: ${COUNT_TIME}s"
log_info "    Select query: ${SELECT_TIME}s"
log_info "    Join query: ${JOIN_TIME}s"
log_info "    Constraint aggregation: ${CONSTRAINT_TIME}s"
log_info "  API responses:"
log_info "    Single item: ${SINGLE_API_TIME}s"
log_info "    Multiple items: ${MULTIPLE_API_TIME}s"
log_info "    Complex item: ${COMPLEX_API_TIME}s"
log_info "    Load test: ${LOAD_TEST_TIME}s"

if [ -n "$LOAD_DURATION" ]; then
    log_info "  Data loading:"
    log_info "    Load time: ${LOAD_DURATION}s"
    log_info "    Items/second: ${ITEMS_PER_SECOND}"
    log_info "    Relations/second: ${RELATIONS_PER_SECOND}"
    log_info "    Constraints/second: ${CONSTRAINTS_PER_SECOND}"
fi

echo ""

# Performance Recommendations
log_info "Performance recommendations:"

# Check if queries are fast enough
if (( $(echo "$SINGLE_API_TIME > 0.1" | bc -l 2>/dev/null || echo "0") )); then
    log_warning "⚠ API response time is slow (>0.1s) - consider optimization"
else
    log_success "✓ API response time is acceptable (<0.1s)"
fi

if (( $(echo "$JOIN_TIME > 0.01" | bc -l 2>/dev/null || echo "0") )); then
    log_warning "⚠ Database query time is slow (>0.01s) - consider adding indexes"
else
    log_success "✓ Database query time is acceptable (<0.01s)"
fi

if [ -n "$LOAD_DURATION" ] && (( $(echo "$LOAD_DURATION > 60" | bc -l 2>/dev/null || echo "0") )); then
    log_warning "⚠ Data loading time is slow (>60s) - consider optimization"
else
    log_success "✓ Data loading time is acceptable"
fi

echo ""
log_success "Performance testing completed!"
echo "=========================================="
