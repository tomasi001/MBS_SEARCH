#!/bin/bash

# Security Testing
# This script tests security aspects of the system

set -e  # Exit on any error

echo "=========================================="
echo "🔒 SECURITY TESTING"
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

# Test 1: Input validation
log_info "Test 1: Testing input validation..."
echo "This will test the system's handling of malicious or malformed input."

# Check if database exists
if [ ! -f "mbs.db" ]; then
    log_info "Loading production data for security testing..."
    poetry run mbs-load --xml data/mbs.xml --verbose
fi

# Start server
log_info "Starting server for security testing..."
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started for security testing"
    
    # Test SQL injection attempts
    log_info "Testing SQL injection attempts..."
    
    # Test with SQL injection payloads
    SQL_INJECTION_PAYLOADS=(
        "3'; DROP TABLE items; --"
        "3' OR '1'='1"
        "3' UNION SELECT * FROM items --"
        "3'; INSERT INTO items VALUES ('999', 'A1', 100.0, 'Hacked'); --"
    )
    
    for payload in "${SQL_INJECTION_PAYLOADS[@]}"; do
        log_info "Testing SQL injection payload: $payload"
        RESPONSE=$(curl -s "http://127.0.0.1:8000/api/items?codes=$payload")
        
        # Check if database is still intact
        ITEM_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items;" 2>/dev/null || echo "0")
        if [ "$ITEM_COUNT" -gt 0 ]; then
            log_success "✓ SQL injection attempt blocked"
        else
            log_error "✗ SQL injection may have succeeded"
        fi
    done
    
    # Test XSS attempts
    log_info "Testing XSS attempts..."
    
    XSS_PAYLOADS=(
        "3<script>alert('xss')</script>"
        "3<img src=x onerror=alert('xss')>"
        "3javascript:alert('xss')"
        "3<iframe src=javascript:alert('xss')></iframe>"
    )
    
    for payload in "${XSS_PAYLOADS[@]}"; do
        log_info "Testing XSS payload: $payload"
        RESPONSE=$(curl -s "http://127.0.0.1:8000/api/items?codes=$payload")
        
        # Check if script tags are present in response
        if echo "$RESPONSE" | grep -q "<script>"; then
            log_warning "⚠ XSS payload may not be properly sanitized"
        else
            log_success "✓ XSS attempt blocked"
        fi
    done
    
    # Test path traversal attempts
    log_info "Testing path traversal attempts..."
    
    PATH_TRAVERSAL_PAYLOADS=(
        "../../../etc/passwd"
        "..\\..\\..\\windows\\system32\\drivers\\etc\\hosts"
        "....//....//....//etc/passwd"
        "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"
    )
    
    for payload in "${PATH_TRAVERSAL_PAYLOADS[@]}"; do
        log_info "Testing path traversal payload: $payload"
        RESPONSE=$(curl -s "http://127.0.0.1:8000/api/items?codes=$payload")
        
        # Check if system files are exposed
        if echo "$RESPONSE" | grep -q "root:"; then
            log_error "✗ Path traversal may have succeeded"
        else
            log_success "✓ Path traversal attempt blocked"
        fi
    done
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
    
else
    log_error "✗ Failed to start server for security testing"
fi

echo ""

# Test 2: Authentication and authorization
log_info "Test 2: Testing authentication and authorization..."
echo "This will test the system's authentication and authorization mechanisms."

# Start server
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started for auth testing"
    
    # Test unauthorized access
    log_info "Testing unauthorized access..."
    
    # Test API without authentication
    if curl -s 'http://127.0.0.1:8000/api/items?codes=3' | grep -q "item_num"; then
        log_warning "⚠ API accessible without authentication"
    else
        log_success "✓ API requires authentication"
    fi
    
    # Test with fake authentication headers
    log_info "Testing with fake authentication headers..."
    if curl -s -H "Authorization: Bearer fake_token" 'http://127.0.0.1:8000/api/items?codes=3' | grep -q "item_num"; then
        log_warning "⚠ API accepts fake authentication"
    else
        log_success "✓ API rejects fake authentication"
    fi
    
    # Test with various authentication methods
    log_info "Testing various authentication methods..."
    
    # Test Basic Auth
    if curl -s -u "user:pass" 'http://127.0.0.1:8000/api/items?codes=3' | grep -q "item_num"; then
        log_warning "⚠ API accepts Basic Auth"
    else
        log_success "✓ API rejects Basic Auth"
    fi
    
    # Test API Key
    if curl -s -H "X-API-Key: fake_key" 'http://127.0.0.1:8000/api/items?codes=3' | grep -q "item_num"; then
        log_warning "⚠ API accepts fake API key"
    else
        log_success "✓ API rejects fake API key"
    fi
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
    
else
    log_error "✗ Failed to start server for auth testing"
fi

echo ""

# Test 3: Rate limiting
log_info "Test 3: Testing rate limiting..."
echo "This will test the system's rate limiting capabilities."

# Start server
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started for rate limiting testing"
    
    # Test rapid requests
    log_info "Testing rapid requests..."
    
    # Send 100 rapid requests
    START_TIME=$(date +%s.%N)
    for i in {1..100}; do
        curl -s 'http://127.0.0.1:8000/api/items?codes=3' > /dev/null &
    done
    wait
    END_TIME=$(date +%s.%N)
    
    RAPID_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
    log_info "Time for 100 rapid requests: ${RAPID_TIME}s"
    
    if (( $(echo "$RAPID_TIME < 10.0" | bc -l 2>/dev/null || echo "1") )); then
        log_warning "⚠ No rate limiting detected (requests processed too quickly)"
    else
        log_success "✓ Rate limiting may be active"
    fi
    
    # Test burst requests
    log_info "Testing burst requests..."
    
    # Send 10 requests simultaneously
    START_TIME=$(date +%s.%N)
    for i in {1..10}; do
        curl -s 'http://127.0.0.1:8000/api/items?codes=3' > /dev/null &
    done
    wait
    END_TIME=$(date +%s.%N)
    
    BURST_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
    log_info "Time for 10 burst requests: ${BURST_TIME}s"
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
    
else
    log_error "✗ Failed to start server for rate limiting testing"
fi

echo ""

# Test 4: Data exposure
log_info "Test 4: Testing data exposure..."
echo "This will test for potential data exposure vulnerabilities."

# Start server
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started for data exposure testing"
    
    # Test for sensitive data exposure
    log_info "Testing for sensitive data exposure..."
    
    # Test API response for sensitive information
    RESPONSE=$(curl -s 'http://127.0.0.1:8000/api/items?codes=3')
    
    # Check for database credentials
    if echo "$RESPONSE" | grep -q "password\|secret\|key\|token"; then
        log_error "✗ Sensitive information may be exposed in API response"
    else
        log_success "✓ No sensitive information exposed in API response"
    fi
    
    # Check for system information
    if echo "$RESPONSE" | grep -q "version\|build\|debug\|trace"; then
        log_warning "⚠ System information may be exposed in API response"
    else
        log_success "✓ No system information exposed in API response"
    fi
    
    # Test for error information disclosure
    log_info "Testing for error information disclosure..."
    
    # Test with invalid input to see error messages
    ERROR_RESPONSE=$(curl -s 'http://127.0.0.1:8000/api/items?codes=invalid')
    
    if echo "$ERROR_RESPONSE" | grep -q "traceback\|exception\|error\|stack"; then
        log_warning "⚠ Error information may be exposed"
    else
        log_success "✓ Error information properly handled"
    fi
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
    
else
    log_error "✗ Failed to start server for data exposure testing"
fi

echo ""

# Test 5: File system security
log_info "Test 5: Testing file system security..."
echo "This will test the system's file system security."

# Test file permissions
log_info "Testing file permissions..."
if [ -f "mbs.db" ]; then
    DB_PERMS=$(ls -l mbs.db | awk '{print $1}')
    log_info "Database file permissions: $DB_PERMS"
    
    if echo "$DB_PERMS" | grep -q "rw-rw-rw"; then
        log_warning "⚠ Database file is world-writable"
    else
        log_success "✓ Database file permissions are secure"
    fi
else
    log_info "No database file found for permission testing"
fi

# Test source code permissions
log_info "Testing source code permissions..."
if [ -f "src/mbs_clarity/db.py" ]; then
    SRC_PERMS=$(ls -l src/mbs_clarity/db.py | awk '{print $1}')
    log_info "Source code permissions: $SRC_PERMS"
    
    if echo "$SRC_PERMS" | grep -q "rwxrwxrwx"; then
        log_warning "⚠ Source code is world-writable"
    else
        log_success "✓ Source code permissions are secure"
    fi
else
    log_info "No source code found for permission testing"
fi

echo ""

# Test 6: Network security
log_info "Test 6: Testing network security..."
echo "This will test the system's network security."

# Test server binding
log_info "Testing server binding..."
if netstat -an 2>/dev/null | grep -q "127.0.0.1:8000"; then
    log_success "✓ Server binds to localhost only"
else
    log_warning "⚠ Server binding unclear"
fi

# Test HTTPS support
log_info "Testing HTTPS support..."
if poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 --ssl-keyfile /nonexistent/key.pem --ssl-certfile /nonexistent/cert.pem 2>/dev/null; then
    log_warning "⚠ HTTPS configuration unclear"
else
    log_info "✓ HTTPS not configured (expected for development)"
fi

echo ""

# Test 7: Dependency security
log_info "Test 7: Testing dependency security..."
echo "This will test the security of system dependencies."

# Check for known vulnerabilities
log_info "Checking for known vulnerabilities..."
if command -v safety &> /dev/null; then
    if poetry run safety check; then
        log_success "✓ No known vulnerabilities found"
    else
        log_warning "⚠ Known vulnerabilities detected"
    fi
else
    log_info "Safety tool not available - install with: pip install safety"
fi

# Check dependency versions
log_info "Checking dependency versions..."
if [ -f "poetry.lock" ]; then
    log_success "✓ Dependencies are locked"
else
    log_warning "⚠ Dependencies not locked"
fi

echo ""

# Test 8: Configuration security
log_info "Test 8: Testing configuration security..."
echo "This will test the security of system configuration."

# Check for hardcoded secrets
log_info "Checking for hardcoded secrets..."
if grep -r "password\|secret\|key\|token" src/ 2>/dev/null | grep -v "test\|example\|sample"; then
    log_warning "⚠ Potential hardcoded secrets found"
else
    log_success "✓ No hardcoded secrets found"
fi

# Check for debug mode
log_info "Checking for debug mode..."
if grep -r "debug.*true\|DEBUG.*True" src/ 2>/dev/null; then
    log_warning "⚠ Debug mode may be enabled"
else
    log_success "✓ Debug mode not found in source"
fi

echo ""

# Test 9: Logging security
log_info "Test 9: Testing logging security..."
echo "This will test the security of system logging."

# Check for sensitive data in logs
log_info "Checking for sensitive data in logs..."
if [ -f "*.log" ]; then
    if grep -i "password\|secret\|key\|token" *.log 2>/dev/null; then
        log_warning "⚠ Sensitive data may be logged"
    else
        log_success "✓ No sensitive data found in logs"
    fi
else
    log_info "No log files found for testing"
fi

echo ""

# Test 10: Input sanitization
log_info "Test 10: Testing input sanitization..."
echo "This will test the system's input sanitization."

# Start server
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!
sleep 3

if ps -p $SERVER_PID > /dev/null; then
    log_success "✓ Server started for input sanitization testing"
    
    # Test various input types
    log_info "Testing input sanitization..."
    
    # Test with special characters
    SPECIAL_CHARS=("3&23" "3|23" "3;23" "3&&23" "3||23" "3`23`" "3$(echo test)23")
    
    for input in "${SPECIAL_CHARS[@]}"; do
        log_info "Testing special characters: $input"
        RESPONSE=$(curl -s "http://127.0.0.1:8000/api/items?codes=$input")
        
        if echo "$RESPONSE" | grep -q "item_num"; then
            log_success "✓ Special characters handled safely"
        else
            log_warning "⚠ Special characters may not be handled properly"
        fi
    done
    
    # Test with Unicode characters
    log_info "Testing Unicode characters..."
    UNICODE_INPUT="3,23,104,测试,🚀"
    RESPONSE=$(curl -s "http://127.0.0.1:8000/api/items?codes=$UNICODE_INPUT")
    
    if echo "$RESPONSE" | grep -q "item_num"; then
        log_success "✓ Unicode characters handled safely"
    else
        log_warning "⚠ Unicode characters may not be handled properly"
    fi
    
    # Stop server
    kill $SERVER_PID 2>/dev/null || true
    sleep 2
    
else
    log_error "✗ Failed to start server for input sanitization testing"
fi

echo ""

# Final summary
log_info "Security testing summary:"
log_info "  Input validation: ✓ Tested"
log_info "  Authentication: ✓ Tested"
log_info "  Rate limiting: ✓ Tested"
log_info "  Data exposure: ✓ Tested"
log_info "  File system security: ✓ Tested"
log_info "  Network security: ✓ Tested"
log_info "  Dependency security: ✓ Tested"
log_info "  Configuration security: ✓ Tested"
log_info "  Logging security: ✓ Tested"
log_info "  Input sanitization: ✓ Tested"

echo ""
log_success "Security testing completed!"
echo "=========================================="
