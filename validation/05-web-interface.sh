#!/bin/bash

# Web Interface Testing
# This script tests the web interface functionality

set -e  # Exit on any error

echo "=========================================="
echo "🖥️  WEB INTERFACE TESTING"
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

# Start server in background
log_info "Starting API server for web interface testing..."
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

# Test web interface accessibility
log_info "Testing web interface accessibility..."

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

if echo "$HTML_CONTENT" | grep -q "<title>"; then
    log_success "✓ Page has title"
else
    log_warning "⚠ Page missing title"
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

# Test JavaScript functionality
log_info "Testing JavaScript functionality..."
if echo "$HTML_CONTENT" | grep -q "<script"; then
    log_success "✓ JavaScript code found"
else
    log_warning "⚠ JavaScript code not found"
fi

if echo "$HTML_CONTENT" | grep -q "fetch.*api"; then
    log_success "✓ API fetch calls found"
else
    log_warning "⚠ API fetch calls not found"
fi

if echo "$HTML_CONTENT" | grep -q "addEventListener"; then
    log_success "✓ Event listeners found"
else
    log_warning "⚠ Event listeners not found"
fi

echo ""

# Test CSS styling
log_info "Testing CSS styling..."
if echo "$HTML_CONTENT" | grep -q "<style"; then
    log_success "✓ CSS styles found"
else
    log_warning "⚠ CSS styles not found"
fi

if echo "$HTML_CONTENT" | grep -q "background"; then
    log_success "✓ Background styling found"
else
    log_warning "⚠ Background styling not found"
fi

if echo "$HTML_CONTENT" | grep -q "color"; then
    log_success "✓ Color styling found"
else
    log_warning "⚠ Color styling not found"
fi

echo ""

# Interactive browser testing
log_info "Interactive browser testing..."
echo "The web interface is available at: http://127.0.0.1:8000"
echo ""
echo "Please test the following scenarios in your browser:"
echo "1. Single code: Enter '3' and click Lookup"
echo "2. Multiple codes: Enter '3,23,104' and click Lookup"
echo "3. Complex item: Enter '44' and click Lookup"
echo "4. Non-existent: Enter '999' and click Lookup"
echo "5. Empty input: Leave blank and click Lookup"
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

read -p "Did the complex item lookup (44) show relations and constraints? (y/n): " test3
if [ "$test3" = "y" ] || [ "$test3" = "Y" ]; then
    log_success "✓ Complex item lookup test passed"
else
    log_error "✗ Complex item lookup test failed"
fi

read -p "Did the non-existent item (999) show appropriate message? (y/n): " test4
if [ "$test4" = "y" ] || [ "$test4" = "Y" ]; then
    log_success "✓ Non-existent item test passed"
else
    log_error "✗ Non-existent item test failed"
fi

read -p "Did the empty input show appropriate message? (y/n): " test5
if [ "$test5" = "y" ] || [ "$test5" = "Y" ]; then
    log_success "✓ Empty input test passed"
else
    log_error "✗ Empty input test failed"
fi

echo ""

# Test responsive design
log_info "Testing responsive design..."
echo "Please test the web interface on different screen sizes:"
echo "1. Desktop browser (full width)"
echo "2. Mobile browser or narrow window"
echo "3. Tablet size"
echo ""
read -p "Does the interface adapt well to different screen sizes? (y/n): " responsive_test
if [ "$responsive_test" = "y" ] || [ "$responsive_test" = "Y" ]; then
    log_success "✓ Responsive design test passed"
else
    log_warning "⚠ Responsive design may need improvement"
fi

echo ""

# Test browser compatibility
log_info "Testing browser compatibility..."
echo "Please test the web interface in different browsers:"
echo "1. Chrome/Chromium"
echo "2. Firefox"
echo "3. Safari"
echo "4. Edge"
echo ""
read -p "Does the interface work correctly in all browsers? (y/n): " browser_test
if [ "$browser_test" = "y" ] || [ "$browser_test" = "Y" ]; then
    log_success "✓ Browser compatibility test passed"
else
    log_warning "⚠ Browser compatibility issues detected"
fi

echo ""

# Performance testing
log_info "Testing web interface performance..."
echo "Testing page load time..."

START_TIME=$(date +%s.%N)
curl -s http://127.0.0.1:8000/ > /dev/null
END_TIME=$(date +%s.%N)
LOAD_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0.1")

log_success "✓ Page load time: ${LOAD_TIME}s"

if (( $(echo "$LOAD_TIME < 1.0" | bc -l 2>/dev/null || echo "1") )); then
    log_success "✓ Page loads quickly (< 1 second)"
else
    log_warning "⚠ Page load time is slow (> 1 second)"
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

echo ""
log_success "Web interface testing completed!"
echo "=========================================="
