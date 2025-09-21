#!/bin/bash

# Final Comprehensive Validation
# This script runs all validation tests and provides a comprehensive report

set -e  # Exit on any error

echo "=========================================="
echo "🎯 FINAL COMPREHENSIVE VALIDATION"
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

# Initialize counters
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0
WARNING_TESTS=0

# Function to run a validation script and track results
run_validation() {
    local script_name="$1"
    local script_path="validation/$script_name"
    
    if [ -f "$script_path" ]; then
        log_info "Running $script_name..."
        TOTAL_TESTS=$((TOTAL_TESTS + 1))
        
        if bash "$script_path"; then
            log_success "✓ $script_name completed successfully"
            PASSED_TESTS=$((PASSED_TESTS + 1))
        else
            log_error "✗ $script_name failed"
            FAILED_TESTS=$((FAILED_TESTS + 1))
        fi
    else
        log_error "✗ $script_name not found at $script_path"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    
    echo ""
}

echo ""

# Check if validation directory exists
if [ ! -d "validation" ]; then
    log_error "Validation directory not found!"
    echo "Please ensure all validation scripts are in the validation/ directory."
    exit 1
fi

# Check if all validation scripts exist
log_info "Checking validation scripts..."
REQUIRED_SCRIPTS=(
    "01-environment-setup.sh"
    "02-code-quality.sh"
    "03-data-loading.sh"
    "04-api-server.sh"
    "05-web-interface.sh"
    "06-database.sh"
    "07-extraction-patterns.sh"
    "08-performance.sh"
    "09-end-to-end.sh"
    "10-real-data.sh"
    "11-error-handling.sh"
    "12-cli-tools.sh"
    "13-security.sh"
)

for script in "${REQUIRED_SCRIPTS[@]}"; do
    if [ -f "validation/$script" ]; then
        log_success "✓ $script found"
    else
        log_error "✗ $script missing"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
done

echo ""

# Ask user which tests to run
log_info "Comprehensive validation options:"
echo "1. Run all validation tests (recommended)"
echo "2. Run core functionality tests only"
echo "3. Run performance and security tests only"
echo "4. Run custom selection"
echo "5. Generate validation report only"
echo ""

read -p "Select option (1-5): " validation_option

case $validation_option in
    1)
        log_info "Running all validation tests..."
        echo "This will take approximately 15-30 minutes depending on your system."
        echo ""
        read -p "Press Enter to continue, or Ctrl+C to cancel: "
        
        # Run all validation tests
        run_validation "01-environment-setup.sh"
        run_validation "02-code-quality.sh"
        run_validation "03-data-loading.sh"
        run_validation "04-api-server.sh"
        run_validation "05-web-interface.sh"
        run_validation "06-database.sh"
        run_validation "07-extraction-patterns.sh"
        run_validation "08-performance.sh"
        run_validation "09-end-to-end.sh"
        run_validation "10-real-data.sh"
        run_validation "11-error-handling.sh"
        run_validation "12-cli-tools.sh"
        run_validation "13-security.sh"
        ;;
    2)
        log_info "Running core functionality tests..."
        run_validation "01-environment-setup.sh"
        run_validation "02-code-quality.sh"
        run_validation "03-data-loading.sh"
        run_validation "04-api-server.sh"
        run_validation "05-web-interface.sh"
        run_validation "06-database.sh"
        run_validation "09-end-to-end.sh"
        ;;
    3)
        log_info "Running performance and security tests..."
        run_validation "08-performance.sh"
        run_validation "13-security.sh"
        run_validation "11-error-handling.sh"
        ;;
    4)
        log_info "Custom validation selection:"
        echo "Available tests:"
        for i in "${!REQUIRED_SCRIPTS[@]}"; do
            echo "$((i+1)). ${REQUIRED_SCRIPTS[i]}"
        done
        echo ""
        read -p "Enter test numbers (comma-separated, e.g., 1,2,3): " custom_tests
        
        IFS=',' read -ra TEST_NUMBERS <<< "$custom_tests"
        for num in "${TEST_NUMBERS[@]}"; do
            if [ "$num" -ge 1 ] && [ "$num" -le "${#REQUIRED_SCRIPTS[@]}" ]; then
                script_index=$((num-1))
                run_validation "${REQUIRED_SCRIPTS[script_index]}"
            else
                log_warning "⚠ Invalid test number: $num"
            fi
        done
        ;;
    5)
        log_info "Generating validation report only..."
        ;;
    *)
        log_error "Invalid option selected"
        exit 1
        ;;
esac

echo ""

# Generate comprehensive report
log_info "Generating comprehensive validation report..."

# Create report file
REPORT_FILE="validation-report-$(date +%Y%m%d-%H%M%S).txt"
log_info "Report will be saved to: $REPORT_FILE"

# Write report header
cat > "$REPORT_FILE" << EOF
MBS Clarity MVP - Comprehensive Validation Report
Generated: $(date)
System: $(uname -a)
Python: $(poetry run python --version)
Poetry: $(poetry --version)

==========================================
VALIDATION SUMMARY
==========================================

Total Tests: $TOTAL_TESTS
Passed: $PASSED_TESTS
Failed: $FAILED_TESTS
Warnings: $WARNING_TESTS

Success Rate: $((PASSED_TESTS * 100 / TOTAL_TESTS))%

EOF

# Add detailed results
echo "==========================================" >> "$REPORT_FILE"
echo "DETAILED RESULTS" >> "$REPORT_FILE"
echo "==========================================" >> "$REPORT_FILE"

# Check system status
echo "" >> "$REPORT_FILE"
echo "System Status:" >> "$REPORT_FILE"
echo "  Database: $(if [ -f "mbs.db" ]; then echo "Present"; else echo "Missing"; fi)" >> "$REPORT_FILE"
echo "  Production Data: $(if [ -f "data/mbs.csv" ]; then echo "Present"; else echo "Missing"; fi)" >> "$REPORT_FILE"
echo "  Full Data: $(if [ -f "data/mbs.xml" ]; then echo "Present"; else echo "Missing"; fi)" >> "$REPORT_FILE"
echo "  Production Backup: $(if [ -f "backups/production_latest.db" ]; then echo "Present"; else echo "Missing"; fi)" >> "$REPORT_FILE"

# Check production state
echo "" >> "$REPORT_FILE"
echo "Production State:" >> "$REPORT_FILE"
if ./validation/00-production-state.sh verify 2>/dev/null; then
    echo "  Status: Ready" >> "$REPORT_FILE"
else
    echo "  Status: Not Ready" >> "$REPORT_FILE"
fi

# Check database contents
if [ -f "mbs.db" ]; then
    echo "" >> "$REPORT_FILE"
    echo "Database Contents:" >> "$REPORT_FILE"
    echo "  Items: $(sqlite3 mbs.db "SELECT COUNT(*) FROM items;" 2>/dev/null || echo "Error")" >> "$REPORT_FILE"
    echo "  Relations: $(sqlite3 mbs.db "SELECT COUNT(*) FROM relations;" 2>/dev/null || echo "Error")" >> "$REPORT_FILE"
    echo "  Constraints: $(sqlite3 mbs.db "SELECT COUNT(*) FROM constraints;" 2>/dev/null || echo "Error")" >> "$REPORT_FILE"
fi

# Check API status
echo "" >> "$REPORT_FILE"
echo "API Status:" >> "$REPORT_FILE"
poetry run uvicorn api.main:app --host 127.0.0.1 --port 8000 &
API_PID=$!
sleep 3

if ps -p $API_PID > /dev/null; then
    echo "  Server: Running" >> "$REPORT_FILE"
    
    # Test API endpoint
    if curl -s 'http://127.0.0.1:8000/api/items?codes=3' | grep -q "item_num"; then
        echo "  Endpoint: Working" >> "$REPORT_FILE"
    else
        echo "  Endpoint: Not responding" >> "$REPORT_FILE"
    fi
    
    kill $API_PID 2>/dev/null || true
else
    echo "  Server: Not running" >> "$REPORT_FILE"
fi

# Check test coverage
echo "" >> "$REPORT_FILE"
echo "Test Coverage:" >> "$REPORT_FILE"
if poetry run pytest --cov=src --cov-report=term-missing 2>/dev/null | grep -q "TOTAL"; then
    poetry run pytest --cov=src --cov-report=term-missing 2>/dev/null | grep "TOTAL" >> "$REPORT_FILE"
else
    echo "  Coverage: Not available" >> "$REPORT_FILE"
fi

# Add recommendations
echo "" >> "$REPORT_FILE"
echo "==========================================" >> "$REPORT_FILE"
echo "RECOMMENDATIONS" >> "$REPORT_FILE"
echo "==========================================" >> "$REPORT_FILE"

if [ "$FAILED_TESTS" -gt 0 ]; then
    echo "1. Address failed tests before deployment" >> "$REPORT_FILE"
fi

if [ "$WARNING_TESTS" -gt 0 ]; then
    echo "2. Review warnings for potential improvements" >> "$REPORT_FILE"
fi

if [ ! -f "data/mbs.xml" ]; then
    echo "3. Load full MBS dataset for complete testing" >> "$REPORT_FILE"
fi

if [ "$PASSED_TESTS" -eq "$TOTAL_TESTS" ]; then
    echo "4. System is ready for production deployment" >> "$REPORT_FILE"
else
    echo "4. System needs additional testing before production" >> "$REPORT_FILE"
fi

echo "" >> "$REPORT_FILE"
echo "==========================================" >> "$REPORT_FILE"
echo "NEXT STEPS" >> "$REPORT_FILE"
echo "==========================================" >> "$REPORT_FILE"

if [ "$PASSED_TESTS" -eq "$TOTAL_TESTS" ]; then
    echo "1. Deploy to production environment" >> "$REPORT_FILE"
    echo "2. Set up monitoring and logging" >> "$REPORT_FILE"
    echo "3. Configure backup and recovery" >> "$REPORT_FILE"
    echo "4. Set up CI/CD pipeline" >> "$REPORT_FILE"
else
    echo "1. Fix failed tests" >> "$REPORT_FILE"
    echo "2. Address warnings" >> "$REPORT_FILE"
    echo "3. Re-run validation tests" >> "$REPORT_FILE"
    echo "4. Review system configuration" >> "$REPORT_FILE"
fi

# Display report summary
echo ""
log_info "Validation Report Summary:"
echo "  Total Tests: $TOTAL_TESTS"
echo "  Passed: $PASSED_TESTS"
echo "  Failed: $FAILED_TESTS"
echo "  Warnings: $WARNING_TESTS"
echo "  Success Rate: $((PASSED_TESTS * 100 / TOTAL_TESTS))%"
echo ""
echo "  Report saved to: $REPORT_FILE"

# Final status
echo ""
if [ "$FAILED_TESTS" -eq 0 ]; then
    log_success "🎉 All validation tests passed! System is ready for production."
else
    log_error "❌ Some validation tests failed. Please review the report and fix issues."
fi

echo ""
log_info "Validation report saved to: $REPORT_FILE"
echo "You can view the full report with: cat $REPORT_FILE"

echo ""
log_success "Final comprehensive validation completed!"
echo "=========================================="
