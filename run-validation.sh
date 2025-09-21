#!/bin/bash

# MBS Clarity MVP - Master Validation Script
# This script runs all validation tests with clear logging and user prompts

set -e  # Exit on any error

echo "=========================================="
echo "🚀 MBS CLARITY MVP - MASTER VALIDATION"
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

# Function to make scripts executable
make_executable() {
    local script="$1"
    if [ -f "$script" ]; then
        chmod +x "$script"
        log_success "✓ Made $script executable"
    else
        log_error "✗ Script not found: $script"
    fi
}

echo ""

# Check if we're in the correct directory
if [ ! -f "pyproject.toml" ]; then
    log_error "Not in MBS Clarity project directory!"
    echo "Please run this script from the project root directory."
    exit 1
fi

log_success "✓ Running from correct directory"

echo ""

# Create validation directory if it doesn't exist
if [ ! -d "validation" ]; then
    log_info "Creating validation directory..."
    mkdir -p validation
    log_success "✓ Validation directory created"
fi

echo ""

# Make all validation scripts executable
log_info "Making validation scripts executable..."
for script in validation/*.sh; do
    if [ -f "$script" ]; then
        make_executable "$script"
    fi
done

echo ""

# Production state management
PRODUCTION_BACKUP_CREATED=false
TEST_ENVIRONMENT_SETUP=false

# Function to ensure production readiness
ensure_production_readiness() {
    log_info "Ensuring production readiness before validation..."
    
    # Run production state management
    if ./validation/00-production-state.sh ensure-ready; then
        PRODUCTION_BACKUP_CREATED=true
        log_success "Production state ready"
    else
        log_error "Failed to ensure production readiness"
        return 1
    fi
}

# Function to setup test environment
setup_test_environment() {
    log_info "Setting up test environment..."
    
    if ./validation/00-production-state.sh setup-test; then
        TEST_ENVIRONMENT_SETUP=true
        log_success "Test environment ready"
    else
        log_warning "Test environment setup failed - using production database"
    fi
}

# Function to cleanup and restore production state
cleanup_and_restore() {
    log_info "Cleaning up and restoring production state..."
    
    # Cleanup test environment
    if [ "$TEST_ENVIRONMENT_SETUP" = true ]; then
        ./validation/00-production-state.sh cleanup-test
    fi
    
    # Restore production database if backup was created
    if [ "$PRODUCTION_BACKUP_CREATED" = true ]; then
        log_info "Restoring production database from backup..."
        ./validation/00-production-state.sh restore
    fi
    
    # Ensure performance indexes are in place
    log_info "Ensuring performance indexes..."
    ./validation/00-production-state.sh indexes
    
    log_success "Production state restored"
}

# Trap to ensure cleanup on exit
trap cleanup_and_restore EXIT INT TERM

# Check if all required scripts exist
log_info "Checking validation scripts..."
REQUIRED_SCRIPTS=(
    "validation/00-production-state.sh"
    "validation/01-environment-setup.sh"
    "validation/02-code-quality.sh"
    "validation/03-data-loading.sh"
    "validation/04-api-server.sh"
    "validation/05-web-interface.sh"
    "validation/06-database.sh"
    "validation/07-extraction-patterns.sh"
    "validation/08-performance.sh"
    "validation/09-end-to-end.sh"
    "validation/10-real-data.sh"
    "validation/11-error-handling.sh"
    "validation/12-cli-tools.sh"
    "validation/13-security.sh"
    "validation/14-final-validation.sh"
)

MISSING_SCRIPTS=0
for script in "${REQUIRED_SCRIPTS[@]}"; do
    if [ -f "$script" ]; then
        log_success "✓ $script"
    else
        log_error "✗ $script missing"
        MISSING_SCRIPTS=$((MISSING_SCRIPTS + 1))
    fi
done

if [ "$MISSING_SCRIPTS" -gt 0 ]; then
    log_error "Missing $MISSING_SCRIPTS validation scripts!"
    echo "Please ensure all validation scripts are present."
    exit 1
fi

echo ""

# Ensure production readiness before validation
log_info "Preparing for validation..."
ensure_production_readiness

echo ""

# Display validation options
log_info "MBS Clarity MVP Validation Options:"
echo ""
echo "1. 🚀 Quick Validation (5-10 minutes)"
echo "   - Environment setup"
echo "   - Code quality"
echo "   - Basic data loading"
echo "   - API server"
echo "   - End-to-end test"
echo ""
echo "2. 🔍 Standard Validation (15-20 minutes)"
echo "   - All quick validation tests"
echo "   - Web interface"
echo "   - Database validation"
echo "   - Extraction patterns"
echo "   - Error handling"
echo ""
echo "3. 🎯 Comprehensive Validation (30-45 minutes)"
echo "   - All standard validation tests"
echo "   - Performance testing"
echo "   - Real data validation"
echo "   - CLI tools"
echo "   - Security testing"
echo "   - Final comprehensive report"
echo ""
echo "4. 🛠️  Custom Validation"
echo "   - Select specific tests to run"
echo ""
echo "5. 📊 Generate Report Only"
echo "   - Generate validation report without running tests"
echo ""

read -p "Select validation option (1-5): " validation_option

case $validation_option in
    1)
        log_info "Running Quick Validation..."
        echo "This will take approximately 5-10 minutes."
        echo ""
        read -p "Press Enter to continue, or Ctrl+C to cancel: "
        
        log_info "Starting Quick Validation..."
        echo ""
        
        setup_test_environment
        echo ""
        
        ./validation/01-environment-setup.sh
        echo ""
        ./validation/02-code-quality.sh
        echo ""
        ./validation/03-data-loading.sh
        echo ""
        ./validation/04-api-server.sh
        echo ""
        ./validation/09-end-to-end.sh
        echo ""
        
        log_success "🎉 Quick Validation completed!"
        ;;
    2)
        log_info "Running Standard Validation..."
        echo "This will take approximately 15-20 minutes."
        echo ""
        read -p "Press Enter to continue, or Ctrl+C to cancel: "
        
        log_info "Starting Standard Validation..."
        echo ""
        
        setup_test_environment
        echo ""
        
        ./validation/01-environment-setup.sh
        echo ""
        ./validation/02-code-quality.sh
        echo ""
        ./validation/03-data-loading.sh
        echo ""
        ./validation/04-api-server.sh
        echo ""
        ./validation/05-web-interface.sh
        echo ""
        ./validation/06-database.sh
        echo ""
        ./validation/07-extraction-patterns.sh
        echo ""
        ./validation/11-error-handling.sh
        echo ""
        ./validation/09-end-to-end.sh
        echo ""
        
        log_success "🎉 Standard Validation completed!"
        ;;
    3)
        log_info "Running Comprehensive Validation..."
        echo "This will take approximately 30-45 minutes."
        echo ""
        read -p "Press Enter to continue, or Ctrl+C to cancel: "
        
        log_info "Starting Comprehensive Validation..."
        echo ""
        
        setup_test_environment
        echo ""
        
        ./validation/01-environment-setup.sh
        echo ""
        ./validation/02-code-quality.sh
        echo ""
        ./validation/03-data-loading.sh
        echo ""
        ./validation/04-api-server.sh
        echo ""
        ./validation/05-web-interface.sh
        echo ""
        ./validation/06-database.sh
        echo ""
        ./validation/07-extraction-patterns.sh
        echo ""
        ./validation/08-performance.sh
        echo ""
        ./validation/09-end-to-end.sh
        echo ""
        ./validation/10-real-data.sh
        echo ""
        ./validation/11-error-handling.sh
        echo ""
        ./validation/12-cli-tools.sh
        echo ""
        ./validation/13-security.sh
        echo ""
        ./validation/14-final-validation.sh
        echo ""
        
        log_success "🎉 Comprehensive Validation completed!"
        ;;
    4)
        log_info "Custom Validation Selection:"
        echo ""
        echo "Available validation tests:"
        echo "1.  Environment Setup"
        echo "2.  Code Quality"
        echo "3.  Data Loading"
        echo "4.  API Server"
        echo "5.  Web Interface"
        echo "6.  Database"
        echo "7.  Extraction Patterns"
        echo "8.  Performance"
        echo "9.  End-to-End"
        echo "10. Real Data"
        echo "11. Error Handling"
        echo "12. CLI Tools"
        echo "13. Security"
        echo "14. Final Validation"
        echo ""
        read -p "Enter test numbers (comma-separated, e.g., 1,2,3): " custom_tests
        
        IFS=',' read -ra TEST_NUMBERS <<< "$custom_tests"
        for num in "${TEST_NUMBERS[@]}"; do
            case $num in
                1) ./validation/01-environment-setup.sh ;;
                2) ./validation/02-code-quality.sh ;;
                3) ./validation/03-data-loading.sh ;;
                4) ./validation/04-api-server.sh ;;
                5) ./validation/05-web-interface.sh ;;
                6) ./validation/06-database.sh ;;
                7) ./validation/07-extraction-patterns.sh ;;
                8) ./validation/08-performance.sh ;;
                9) ./validation/09-end-to-end.sh ;;
                10) ./validation/10-real-data.sh ;;
                11) ./validation/11-error-handling.sh ;;
                12) ./validation/12-cli-tools.sh ;;
                13) ./validation/13-security.sh ;;
                14) ./validation/14-final-validation.sh ;;
                *) log_warning "⚠ Invalid test number: $num" ;;
            esac
            echo ""
        done
        
        log_success "🎉 Custom Validation completed!"
        ;;
    5)
        log_info "Generating validation report only..."
        ./validation/14-final-validation.sh
        ;;
    *)
        log_error "Invalid option selected"
        exit 1
        ;;
esac

echo ""

# Final summary
log_info "Validation Summary:"
echo "  Validation option: $validation_option"
echo "  Completed at: $(date)"
echo "  Project directory: $(pwd)"
echo ""

# Check if validation report was generated
if [ -f "validation-report-*.txt" ]; then
    REPORT_FILE=$(ls validation-report-*.txt | tail -1)
    log_info "Validation report generated: $REPORT_FILE"
    echo "  View report: cat $REPORT_FILE"
fi

echo ""

# Provide next steps
log_info "Next Steps:"
echo "1. Review any failed tests or warnings"
echo "2. Fix any issues found during validation"
echo "3. Re-run validation if needed"
echo "4. Deploy to production when ready"
echo ""

# Check if system is ready
if [ "$validation_option" -eq 3 ]; then
    log_success "🎉 Comprehensive validation completed!"
    echo "Your MBS Clarity MVP system has been thoroughly tested."
    echo "Check the validation report for detailed results."
else
    log_info "💡 Consider running comprehensive validation for production readiness."
fi

echo ""
log_success "Master validation script completed!"
echo "=========================================="
