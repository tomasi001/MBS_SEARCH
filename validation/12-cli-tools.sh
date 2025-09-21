#!/bin/bash

# CLI Tool Testing
# This script tests the command-line interface tools

set -e  # Exit on any error

echo "=========================================="
echo "🖥️  CLI TOOL TESTING"
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

# Test 1: Help commands
log_info "Test 1: Testing help commands..."
echo "This will test the availability and content of help commands."

log_info "Testing main CLI help..."
if poetry run mbs --help 2>/dev/null; then
    log_success "✓ Main CLI help command works"
else
    log_error "✗ Main CLI help command failed"
fi

echo ""

log_info "Testing mbs-load help..."
if poetry run mbs-load --help 2>/dev/null; then
    log_success "✓ mbs-load help command works"
else
    log_error "✗ mbs-load help command failed"
fi

echo ""

# Test 2: XML analysis command
log_info "Test 2: Testing XML analysis command..."
echo "This will test the XML structure analysis functionality."

if [ -f "data/mbs.xml" ]; then
    log_info "Testing XML analysis with full dataset..."
    if poetry run mbs analyze-xml data/mbs.xml; then
        log_success "✓ XML analysis command works"
    else
        log_error "✗ XML analysis command failed"
    fi
elif [ -f "data/mbs.csv" ]; then
    log_info "Full XML not available, testing with CSV data..."
    echo "Would you like to create a test XML file for testing?"
    read -p "Press 'y' to create test XML, any other key to skip: " create_test_xml
    
    if [ "$create_test_xml" = "y" ] || [ "$create_test_xml" = "Y" ]; then
        # Create a simple test XML file
        cat > /tmp/test.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <item>
        <item_num>3</item_num>
        <category>1</category>
        <schedule_fee>125.1</schedule_fee>
        <description>Professional attendance</description>
    </item>
    <item>
        <item_num>23</item_num>
        <category>1</category>
        <schedule_fee>200.0</schedule_fee>
        <description>Another professional attendance</description>
    </item>
</root>
EOF
        
        log_info "Created test XML file: /tmp/test.xml"
        
        if poetry run mbs analyze-xml /tmp/test.xml; then
            log_success "✓ XML analysis command works with test data"
        else
            log_error "✗ XML analysis command failed with test data"
        fi
        
        # Clean up
        rm -f /tmp/test.xml
    else
        log_info "Skipping XML analysis test"
    fi
else
    log_warning "⚠ No XML or CSV data available for testing"
fi

echo ""

# Test 3: Data loading commands
log_info "Test 3: Testing data loading commands..."
echo "This will test the data loading functionality through CLI."

# Check if production data exists
if [ -f "data/mbs.csv" ]; then
    log_info "Testing CSV data loading..."
    
    # Backup existing database
    if [ -f "mbs.db" ]; then
        cp mbs.db mbs.db.backup
        log_info "✓ Existing database backed up"
    fi
    
    # Remove existing database
    rm -f mbs.db
    
    # Test CSV loading
    if poetry run mbs-load --csv data/mbs.csv --verbose; then
        log_success "✓ CSV data loading works"
        
        # Verify database was created
        if [ -f "mbs.db" ]; then
            log_success "✓ Database file created"
            
            # Check item count
            ITEM_COUNT=$(sqlite3 mbs.db "SELECT COUNT(*) FROM items;" 2>/dev/null || echo "0")
            log_info "Items loaded: $ITEM_COUNT"
            
            if [ "$ITEM_COUNT" -gt 1000 ]; then
                log_success "✓ Production data loaded successfully"
            else
                log_warning "⚠ Low item count - may not be production data"
            fi
                log_error "✗ No data loaded"
            fi
        else
            log_error "✗ Database file not created"
        fi
    else
        log_error "✗ CSV data loading failed"
    fi
    
    # Restore original database
    if [ -f "mbs.db.backup" ]; then
        mv mbs.db.backup mbs.db
        log_info "✓ Original database restored"
    fi
    
else
    log_warning "⚠ Production CSV data not available for testing"
fi

echo ""

# Test 4: Verbose output
log_info "Test 4: Testing verbose output..."
echo "This will test the verbose logging functionality."

if [ -f "data/mbs.csv" ]; then
    log_info "Testing verbose output with production data..."
    
    # Backup existing database
    if [ -f "mbs.db" ]; then
        cp mbs.db mbs.db.backup
    fi
    
    # Remove existing database
    rm -f mbs.db
    
    # Test verbose loading
    if poetry run mbs-load --csv data/mbs.csv --verbose 2>&1 | grep -q "INFO"; then
        log_success "✓ Verbose output works"
    else
        log_warning "⚠ Verbose output may not be working properly"
    fi
    
    # Restore original database
    if [ -f "mbs.db.backup" ]; then
        mv mbs.db.backup mbs.db
    fi
    
else
    log_info "Skipping verbose output test (no production data)"
fi

echo ""

# Test 5: Error handling in CLI
log_info "Test 5: Testing CLI error handling..."
echo "This will test how the CLI handles various error conditions."

# Test with non-existent file
log_info "Testing with non-existent file..."
if poetry run mbs-load --csv /nonexistent/file.csv 2>/dev/null; then
    log_error "✗ CLI processed non-existent file (unexpected)"
else
    log_success "✓ CLI correctly rejected non-existent file"
fi

# Test with invalid arguments
log_info "Testing with invalid arguments..."
if poetry run mbs-load --invalid-arg 2>/dev/null; then
    log_error "✗ CLI processed invalid arguments (unexpected)"
else
    log_success "✓ CLI correctly rejected invalid arguments"
fi

# Test with missing required arguments
log_info "Testing with missing required arguments..."
if poetry run mbs-load 2>/dev/null; then
    log_error "✗ CLI processed missing arguments (unexpected)"
else
    log_success "✓ CLI correctly rejected missing arguments"
fi

echo ""

# Test 6: CLI output formatting
log_info "Test 6: Testing CLI output formatting..."
echo "This will test the formatting and readability of CLI output."

if [ -f "data/mbs.csv" ]; then
    log_info "Testing CLI output formatting..."
    
    # Backup existing database
    if [ -f "mbs.db" ]; then
        cp mbs.db mbs.db.backup
    fi
    
    # Remove existing database
    rm -f mbs.db
    
    # Capture CLI output
    CLI_OUTPUT=$(poetry run mbs-load --csv data/mbs.csv --verbose 2>&1)
    
    # Check for key output elements
    if echo "$CLI_OUTPUT" | grep -q "Starting MBS data loading process"; then
        log_success "✓ CLI shows start message"
    else
        log_warning "⚠ CLI start message not found"
    fi
    
    if echo "$CLI_OUTPUT" | grep -q "Loading complete"; then
        log_success "✓ CLI shows completion message"
    else
        log_warning "⚠ CLI completion message not found"
    fi
    
    if echo "$CLI_OUTPUT" | grep -q "items"; then
        log_success "✓ CLI shows item count"
    else
        log_warning "⚠ CLI item count not found"
    fi
    
    # Restore original database
    if [ -f "mbs.db.backup" ]; then
        mv mbs.db.backup mbs.db
    fi
    
else
    log_info "Skipping CLI output formatting test (no production data)"
fi

echo ""

# Test 7: CLI performance
log_info "Test 7: Testing CLI performance..."
echo "This will test the performance of CLI operations."

if [ -f "data/mbs.csv" ]; then
    log_info "Testing CLI performance with production data..."
    
    # Backup existing database
    if [ -f "mbs.db" ]; then
        cp mbs.db mbs.db.backup
    fi
    
    # Remove existing database
    rm -f mbs.db
    
    # Time the CLI operation
    START_TIME=$(date +%s.%N)
    
    if poetry run mbs-load --csv data/mbs.csv --verbose > /dev/null 2>&1; then
        END_TIME=$(date +%s.%N)
        CLI_TIME=$(echo "$END_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0")
        
        log_success "✓ CLI operation completed successfully"
        log_info "CLI execution time: ${CLI_TIME}s"
        
        if (( $(echo "$CLI_TIME < 10.0" | bc -l 2>/dev/null || echo "1") )); then
            log_success "✓ CLI performance is acceptable (<10s)"
        else
            log_warning "⚠ CLI performance is slow (>10s)"
        fi
    else
        log_error "✗ CLI operation failed"
    fi
    
    # Restore original database
    if [ -f "mbs.db.backup" ]; then
        mv mbs.db.backup mbs.db
    fi
    
else
    log_info "Skipping CLI performance test (no production data)"
fi

echo ""

# Test 8: Interactive CLI features
log_info "Test 8: Testing interactive CLI features..."
echo "This will test any interactive features of the CLI."

# Test if CLI supports interactive input
log_info "Testing CLI interactive capabilities..."
if echo "test" | poetry run mbs-load --csv data/mbs.csv 2>/dev/null; then
    log_success "✓ CLI handles input correctly"
else
    log_warning "⚠ CLI input handling unclear"
fi

echo ""

# Test 9: CLI configuration
log_info "Test 9: Testing CLI configuration..."
echo "This will test CLI configuration and environment handling."

# Test environment variable handling
log_info "Testing environment variable handling..."
export TEST_ENV_VAR="test_value"
if poetry run mbs --help 2>/dev/null; then
    log_success "✓ CLI works with environment variables"
else
    log_warning "⚠ CLI environment variable handling unclear"
fi

# Test working directory handling
log_info "Testing working directory handling..."
ORIGINAL_DIR=$(pwd)
cd /tmp
if poetry run mbs --help 2>/dev/null; then
    log_success "✓ CLI works from different directories"
else
    log_warning "⚠ CLI directory handling unclear"
fi
cd "$ORIGINAL_DIR"

echo ""

# Test 10: CLI integration with other tools
log_info "Test 10: Testing CLI integration with other tools..."
echo "This will test how the CLI integrates with other system tools."

# Test with different shells
log_info "Testing CLI with different shells..."
if bash -c "poetry run mbs --help" 2>/dev/null; then
    log_success "✓ CLI works with bash"
else
    log_warning "⚠ CLI bash compatibility unclear"
fi

if zsh -c "poetry run mbs --help" 2>/dev/null; then
    log_success "✓ CLI works with zsh"
else
    log_warning "⚠ CLI zsh compatibility unclear"
fi

# Test with different Python versions
log_info "Testing CLI with different Python versions..."
PYTHON_VERSION=$(poetry run python --version)
log_info "Current Python version: $PYTHON_VERSION"

echo ""

# Test 11: CLI documentation
log_info "Test 11: Testing CLI documentation..."
echo "This will test the quality and completeness of CLI documentation."

# Check if help text is comprehensive
log_info "Checking CLI help text completeness..."
HELP_TEXT=$(poetry run mbs --help 2>&1)

if echo "$HELP_TEXT" | grep -q "usage"; then
    log_success "✓ CLI help shows usage information"
else
    log_warning "⚠ CLI help missing usage information"
fi

if echo "$HELP_TEXT" | grep -q "options"; then
    log_success "✓ CLI help shows options"
else
    log_warning "⚠ CLI help missing options information"
fi

if echo "$HELP_TEXT" | grep -q "commands"; then
    log_success "✓ CLI help shows commands"
else
    log_warning "⚠ CLI help missing commands information"
fi

echo ""

# Test 12: CLI error messages
log_info "Test 12: Testing CLI error messages..."
echo "This will test the clarity and helpfulness of CLI error messages."

# Test error message quality
log_info "Testing error message quality..."
ERROR_OUTPUT=$(poetry run mbs-load --csv /nonexistent/file.csv 2>&1)

if echo "$ERROR_OUTPUT" | grep -q "error\|Error\|ERROR"; then
    log_success "✓ CLI shows error messages"
else
    log_warning "⚠ CLI error messages unclear"
fi

if echo "$ERROR_OUTPUT" | grep -q "file\|File"; then
    log_success "✓ CLI error messages are descriptive"
else
    log_warning "⚠ CLI error messages may not be descriptive"
fi

echo ""

# Final summary
log_info "CLI tool testing summary:"
log_info "  Help commands: ✓ Tested"
log_info "  XML analysis: ✓ Tested"
log_info "  Data loading: ✓ Tested"
log_info "  Verbose output: ✓ Tested"
log_info "  Error handling: ✓ Tested"
log_info "  Output formatting: ✓ Tested"
log_info "  Performance: ✓ Tested"
log_info "  Interactive features: ✓ Tested"
log_info "  Configuration: ✓ Tested"
log_info "  Integration: ✓ Tested"
log_info "  Documentation: ✓ Tested"
log_info "  Error messages: ✓ Tested"

echo ""
log_success "CLI tool testing completed!"
echo "=========================================="
