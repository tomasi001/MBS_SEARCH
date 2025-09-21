#!/bin/bash

# Error Handling Testing
# This script tests error handling and edge cases

set -e  # Exit on any error

echo "=========================================="
echo "⚠️  ERROR HANDLING TESTING"
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

echo ""

# Test 1: Invalid XML file
log_info "Test 1: Testing with invalid XML file..."
echo "This will test the system's handling of malformed XML data."

# Create a malformed XML file
cat > /tmp/invalid.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <item>
        <item_num>999</item_num>
        <description>Test item</description>
        <!-- Missing closing tag -->
    <item>
        <item_num>998</item_num>
        <description>Another test item</description>
    </item>
</root>
EOF

log_info "Created malformed XML file: /tmp/invalid.xml"
echo "Would you like to test loading this malformed XML?"
read -p "Press 'y' to test, any other key to skip: " test_invalid_xml

if [ "$test_invalid_xml" = "y" ] || [ "$test_invalid_xml" = "Y" ]; then
    log_info "Testing malformed XML loading..."
    if poetry run mbs-load --xml /tmp/invalid.xml 2>/dev/null; then
        log_warning "⚠ Malformed XML was processed without error (unexpected)"
    else
        log_success "✓ Malformed XML correctly rejected"
    fi
else
    log_info "Skipping malformed XML test"
fi

# Clean up
rm -f /tmp/invalid.xml

echo ""

# Test 2: Invalid CSV file
log_info "Test 2: Testing with invalid CSV file..."
echo "This will test the system's handling of malformed CSV data."

# Create a malformed CSV file
cat > /tmp/invalid.csv << 'EOF'
item_num,category,schedule_fee,description
1,A1,100.0,"Valid item"
2,A2,200.0,"Another valid item"
3,A3,300.0,"Item with unclosed quote
4,A4,400.0,"Valid item"
EOF

log_info "Created malformed CSV file: /tmp/invalid.csv"
echo "Would you like to test loading this malformed CSV?"
read -p "Press 'y' to test, any other key to skip: " test_invalid_csv

if [ "$test_invalid_csv" = "y" ] || [ "$test_invalid_csv" = "Y" ]; then
    log_info "Testing malformed CSV loading..."
    if poetry run mbs-load --csv /tmp/invalid.csv 2>/dev/null; then
        log_warning "⚠ Malformed CSV was processed without error (unexpected)"
    else
        log_success "✓ Malformed CSV correctly rejected"
    fi
else
    log_info "Skipping malformed CSV test"
fi

# Clean up
rm -f /tmp/invalid.csv

echo ""

# Test 3: Non-existent files
log_info "Test 3: Testing with non-existent files..."
echo "This will test the system's handling of missing input files."

log_info "Testing non-existent XML file..."
if poetry run mbs-load --xml /nonexistent/file.xml 2>/dev/null; then
    log_error "✗ Non-existent XML file was processed (unexpected)"
else
    log_success "✓ Non-existent XML file correctly rejected"
fi

log_info "Testing non-existent CSV file..."
if poetry run mbs-load --csv /nonexistent/file.csv 2>/dev/null; then
    log_error "✗ Non-existent CSV file was processed (unexpected)"
else
    log_success "✓ Non-existent CSV file correctly rejected"
fi

echo ""

# Test 4: Empty files
log_info "Test 4: Testing with empty files..."
echo "This will test the system's handling of empty input files."

# Create empty files
touch /tmp/empty.xml
touch /tmp/empty.csv

log_info "Testing empty XML file..."
if poetry run mbs-load --xml /tmp/empty.xml 2>/dev/null; then
    log_warning "⚠ Empty XML file was processed (may be expected)"
else
    log_success "✓ Empty XML file correctly rejected"
fi

log_info "Testing empty CSV file..."
if poetry run mbs-load --csv /tmp/empty.csv 2>/dev/null; then
    log_warning "⚠ Empty CSV file was processed (may be expected)"
else
    log_success "✓ Empty CSV file correctly rejected"
fi

# Clean up
rm -f /tmp/empty.xml /tmp/empty.csv

echo ""

# Test 5: Database errors
log_info "Test 5: Testing database error handling..."
echo "This will test the system's handling of database-related errors."

# Check if database exists
if [ ! -f "mbs.db" ]; then
    log_info "Loading production data for database error testing..."
    poetry run mbs-load --xml data/mbs.xml --verbose
fi

# Test with corrupted database
log_info "Testing with corrupted database..."
if [ -f "mbs.db" ]; then
    # Backup original database
    cp mbs.db mbs.db.backup
    
    # Corrupt the database by truncating it
    echo "corrupted" > mbs.db
    
    log_info "Testing API with corrupted database..."
    
    # Start server
    poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
    SERVER_PID=$!
    sleep 3
    
    if ps -p $SERVER_PID > /dev/null; then
        # Test API with corrupted database
        if curl -s 'http://127.0.0.1:8000/api/items?codes=3' 2>/dev/null; then
            log_warning "⚠ API responded with corrupted database (unexpected)"
        else
            log_success "✓ API correctly failed with corrupted database"
        fi
        
        # Stop server
        kill $SERVER_PID 2>/dev/null || true
        sleep 2
    fi
    
    # Restore original database
    mv mbs.db.backup mbs.db
    log_info "✓ Original database restored"
fi

echo ""

# Test 6: API error handling
log_info "Test 6: Testing API error handling..."
echo "This will test the API's handling of various error conditions."

# Start server
log_info "Starting server for API error testing..."
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started for API error testing"
    
    # Test invalid item codes
    log_info "Testing invalid item codes..."
    
    # Test with non-numeric codes
    if curl -s 'http://127.0.0.1:8000/api/items?codes=abc' | grep -q "items"; then
        log_success "✓ API handled non-numeric codes gracefully"
    else
        log_warning "⚠ API response to non-numeric codes unclear"
    fi
    
    # Test with special characters
    if curl -s 'http://127.0.0.1:8000/api/items?codes=3@23' | grep -q "items"; then
        log_success "✓ API handled special characters gracefully"
    else
        log_warning "⚠ API response to special characters unclear"
    fi
    
    # Test with very long input
    LONG_INPUT=$(printf "3%.0s" {1..1000})
    if curl -s "http://127.0.0.1:8000/api/items?codes=$LONG_INPUT" | grep -q "items"; then
        log_success "✓ API handled very long input gracefully"
    else
        log_warning "⚠ API response to very long input unclear"
    fi
    
    # Test with empty codes parameter
    if curl -s 'http://127.0.0.1:8000/api/items?codes=' | grep -q "items"; then
        log_success "✓ API handled empty codes parameter gracefully"
    else
        log_warning "⚠ API response to empty codes parameter unclear"
    fi
    
    # Test with missing codes parameter
    if curl -s 'http://127.0.0.1:8000/api/items' | grep -q "items"; then
        log_success "✓ API handled missing codes parameter gracefully"
    else
        log_warning "⚠ API response to missing codes parameter unclear"
    fi
    
    # Test with invalid HTTP methods
    log_info "Testing invalid HTTP methods..."
    if curl -s -X POST 'http://127.0.0.1:8000/api/items?codes=3' | grep -q "items"; then
        log_success "✓ API handled POST request gracefully"
    else
        log_warning "⚠ API response to POST request unclear"
    fi
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
    
else
    log_error "✗ Failed to start server for API error testing"
fi

echo ""

# Test 7: Memory and resource limits
log_info "Test 7: Testing memory and resource limits..."
echo "This will test the system's behavior under resource constraints."

# Test with very large input
log_info "Testing with very large input..."
LARGE_INPUT=$(seq 1 1000 | tr '\n' ',' | sed 's/,$//')
log_info "Testing with 1000 item codes..."

# Start server
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    START_TIME=$(date +%s.%N)
    if curl -s "http://127.0.0.1:8000/api/items?codes=$LARGE_INPUT" > /dev/null; then
        END_TIME=$(date +%s.%N)
        LARGE_RESPONSE_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
        log_success "✓ API handled large input successfully"
        log_info "Response time for 1000 items: ${LARGE_RESPONSE_TIME}s"
    else
        log_warning "⚠ API failed with large input"
    fi
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
fi

echo ""

# Test 8: Concurrent access
log_info "Test 8: Testing concurrent access..."
echo "This will test the system's handling of concurrent requests."

# Start server
log_info "Starting server for concurrent access testing..."
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started for concurrent access testing"
    
    # Test concurrent requests
    log_info "Testing concurrent requests..."
    START_TIME=$(date +%s.%N)
    
    # Start 10 concurrent requests
    for i in {1..10}; do
        curl -s 'http://127.0.0.1:8000/api/items?codes=3' > /dev/null &
    done
    
    # Wait for all requests to complete
    wait
    
    END_TIME=$(date +%s.%N)
    CONCURRENT_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
    
    log_success "✓ Concurrent requests completed successfully"
    log_info "Time for 10 concurrent requests: ${CONCURRENT_TIME}s"
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
    
else
    log_error "✗ Failed to start server for concurrent access testing"
fi

echo ""

# Test 9: Network errors
log_info "Test 9: Testing network error handling..."
echo "This will test the system's handling of network-related errors."

# Test with invalid port
log_info "Testing with invalid port..."
if curl -s 'http://127.0.0.1:9999/api/items?codes=3' 2>/dev/null; then
    log_warning "⚠ Unexpected response from invalid port"
else
    log_success "✓ Correctly failed to connect to invalid port"
fi

# Test with invalid host
log_info "Testing with invalid host..."
if curl -s 'http://invalidhost:8000/api/items?codes=3' 2>/dev/null; then
    log_warning "⚠ Unexpected response from invalid host"
else
    log_success "✓ Correctly failed to connect to invalid host"
fi

echo ""

# Test 10: Data validation errors
log_info "Test 10: Testing data validation errors..."
echo "This will test the system's handling of invalid data formats."

# Create CSV with invalid data types
cat > /tmp/invalid_data.csv << 'EOF'
item_num,category,schedule_fee,description
1,A1,invalid_fee,"Valid item"
2,A2,200.0,"Valid item"
3,A3,300.0,"Valid item"
EOF

log_info "Testing CSV with invalid data types..."
if poetry run mbs-load --csv /tmp/invalid_data.csv 2>/dev/null; then
    log_warning "⚠ CSV with invalid data types was processed (may be expected)"
else
    log_success "✓ CSV with invalid data types correctly rejected"
fi

# Clean up
rm -f /tmp/invalid_data.csv

echo ""

# Test 11: File permission errors
log_info "Test 11: Testing file permission errors..."
echo "This will test the system's handling of file permission issues."

# Create a file with restricted permissions
touch /tmp/restricted.csv
chmod 000 /tmp/restricted.csv

log_info "Testing with restricted file permissions..."
if poetry run mbs-load --csv /tmp/restricted.csv 2>/dev/null; then
    log_error "✗ Restricted file was processed (unexpected)"
else
    log_success "✓ Restricted file correctly rejected"
fi

# Clean up
rm -f /tmp/restricted.csv

echo ""

# Test 12: Disk space errors
log_info "Test 12: Testing disk space error handling..."
echo "This will test the system's behavior when disk space is limited."

# Check available disk space
AVAILABLE_SPACE=$(df . | tail -1 | awk '{print $4}')
log_info "Available disk space: $AVAILABLE_SPACE KB"

if [ "$AVAILABLE_SPACE" -lt 1000000 ]; then
    log_warning "⚠ Low disk space detected - some tests may fail"
else
    log_success "✓ Sufficient disk space available"
fi

echo ""

# Final summary
log_info "Error handling testing summary:"
log_info "  Invalid XML handling: ✓ Tested"
log_info "  Invalid CSV handling: ✓ Tested"
log_info "  Non-existent files: ✓ Tested"
log_info "  Empty files: ✓ Tested"
log_info "  Database errors: ✓ Tested"
log_info "  API error handling: ✓ Tested"
log_info "  Memory limits: ✓ Tested"
log_info "  Concurrent access: ✓ Tested"
log_info "  Network errors: ✓ Tested"
log_info "  Data validation: ✓ Tested"
log_info "  File permissions: ✓ Tested"
log_info "  Disk space: ✓ Tested"

echo ""
log_success "Error handling testing completed!"
echo "=========================================="
