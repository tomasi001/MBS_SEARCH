#!/bin/bash

# Code Quality Validation
# This script runs linting, formatting, and code quality checks

set -e  # Exit on any error

echo "=========================================="
echo "🔍 CODE QUALITY VALIDATION"
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

# Check if Makefile exists
if [ ! -f "Makefile" ]; then
    log_error "Makefile not found! Cannot run code quality checks."
    exit 1
fi

# Run linting
log_info "Running code linting with Ruff..."
if make lint; then
    log_success "✓ Linting passed - no issues found"
else
    log_error "✗ Linting failed - code quality issues detected"
    echo ""
    echo "Would you like to see the detailed linting output?"
    read -p "Press 'y' to see details, any other key to continue: " show_details
    if [ "$show_details" = "y" ] || [ "$show_details" = "Y" ]; then
        log_info "Running linting with verbose output..."
        poetry run ruff check src tests --verbose
    fi
    echo ""
    echo "Would you like to auto-fix the linting issues?"
    read -p "Press 'y' to auto-fix, any other key to skip: " auto_fix
    if [ "$auto_fix" = "y" ] || [ "$auto_fix" = "Y" ]; then
        log_info "Auto-fixing linting issues..."
        poetry run ruff check src tests --fix
        log_success "✓ Auto-fix completed"
    fi
fi

echo ""

# Run formatting
log_info "Running code formatting with Black..."
if make format; then
    log_success "✓ Formatting completed successfully"
else
    log_error "✗ Formatting failed"
    echo ""
    echo "Would you like to see the formatting issues?"
    read -p "Press 'y' to see details, any other key to continue: " show_format_details
    if [ "$show_format_details" = "y" ] || [ "$show_format_details" = "Y" ]; then
        log_info "Running Black with verbose output..."
        poetry run black src tests --diff --verbose
    fi
fi

echo ""

# Run full CI pipeline
log_info "Running full CI pipeline (lint + format + test)..."
echo "This will run linting, formatting, and tests together."
read -p "Press Enter to continue, or Ctrl+C to skip: "

if make ci; then
    log_success "✓ Full CI pipeline passed successfully"
else
    log_error "✗ CI pipeline failed"
    echo ""
    echo "The CI pipeline includes:"
    echo "1. Code linting (Ruff)"
    echo "2. Code formatting (Black)"
    echo "3. Unit tests (pytest)"
    echo ""
    echo "Would you like to run tests separately to see detailed output?"
    read -p "Press 'y' to run tests separately, any other key to continue: " run_tests_separate
    if [ "$run_tests_separate" = "y" ] || [ "$run_tests_separate" = "Y" ]; then
        log_info "Running tests with verbose output..."
        poetry run pytest -v
    fi
fi

echo ""

# Check test coverage
log_info "Checking test coverage..."
echo "Would you like to generate a detailed coverage report?"
read -p "Press 'y' for coverage report, any other key to skip: " coverage_report
if [ "$coverage_report" = "y" ] || [ "$coverage_report" = "Y" ]; then
    log_info "Generating coverage report..."
    if poetry run pytest --cov=src --cov-report=html --cov-report=term; then
        log_success "✓ Coverage report generated"
        log_info "HTML coverage report available at: htmlcov/index.html"
        echo ""
        echo "Would you like to open the coverage report in your browser?"
        read -p "Press 'y' to open, any other key to skip: " open_coverage
        if [ "$open_coverage" = "y" ] || [ "$open_coverage" = "Y" ]; then
            if command -v open &> /dev/null; then
                open htmlcov/index.html
                log_success "✓ Coverage report opened in browser"
            else
                log_warning "Cannot open browser automatically. Please open htmlcov/index.html manually."
            fi
        fi
    else
        log_error "✗ Coverage report generation failed"
    fi
fi

echo ""
log_success "Code quality validation completed!"
echo "=========================================="
