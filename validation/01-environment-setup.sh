#!/bin/bash

# Environment Setup & Verification
# This script validates the development environment is properly configured

set -e  # Exit on any error

echo "=========================================="
echo "🔧 ENVIRONMENT SETUP & VERIFICATION"
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

# Check if Poetry is installed
log_info "Checking Poetry installation..."
if command -v poetry &> /dev/null; then
    POETRY_VERSION=$(poetry --version)
    log_success "Poetry is installed: $POETRY_VERSION"
else
    log_error "Poetry is not installed!"
    echo ""
    echo "Please install Poetry first:"
    echo "curl -sSL https://install.python-poetry.org | python3 -"
    echo ""
    read -p "Press Enter after installing Poetry to continue..."
    
    # Re-check after user input
    if command -v poetry &> /dev/null; then
        POETRY_VERSION=$(poetry --version)
        log_success "Poetry is now installed: $POETRY_VERSION"
    else
        log_error "Poetry installation failed. Please install manually."
        exit 1
    fi
fi

# Check Python version
log_info "Checking Python version..."
PYTHON_VERSION=$(poetry run python --version)
log_success "Python version: $PYTHON_VERSION"

# Check if pyproject.toml exists
log_info "Checking project configuration..."
if [ -f "pyproject.toml" ]; then
    log_success "pyproject.toml found"
else
    log_error "pyproject.toml not found! Are you in the correct directory?"
    exit 1
fi

# Check if dependencies are installed
log_info "Checking if dependencies are installed..."
if poetry check &> /dev/null; then
    log_success "Project configuration is valid"
else
    log_warning "Project configuration has issues, but continuing..."
fi

# Install dependencies
log_info "Installing dependencies..."
if poetry install; then
    log_success "Dependencies installed successfully"
else
    log_error "Failed to install dependencies"
    exit 1
fi

# Verify key dependencies
log_info "Verifying key dependencies..."
REQUIRED_PACKAGES=("fastapi" "uvicorn" "sqlite3" "pytest" "pandas" "lxml")
for package in "${REQUIRED_PACKAGES[@]}"; do
    if poetry run python -c "import $package" 2>/dev/null; then
        log_success "✓ $package is available"
    else
        log_warning "⚠ $package may not be properly installed"
    fi
done

# Check data directory
log_info "Checking data directory..."
if [ -d "data" ]; then
    log_success "Data directory exists"
    if [ -f "data/mbs.csv" ]; then
        log_success "✓ Production CSV data found"
    else
        log_warning "⚠ Production CSV data not found"
    fi
    if [ -f "data/mbs.xml" ]; then
        log_success "✓ Full XML data found"
    else
        log_warning "⚠ Full XML data not found"
    fi
else
    log_error "Data directory not found!"
    exit 1
fi

# Check source code structure
log_info "Checking source code structure..."
REQUIRED_DIRS=("src" "api" "tests")
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        log_success "✓ $dir directory exists"
    else
        log_error "✗ $dir directory missing!"
        exit 1
    fi
done

# Check Makefile
log_info "Checking Makefile..."
if [ -f "Makefile" ]; then
    log_success "✓ Makefile found"
    log_info "Available make commands:"
    make help 2>/dev/null || log_warning "Make help not available"
else
    log_warning "⚠ Makefile not found"
fi

echo ""
log_success "Environment setup validation completed!"
echo "=========================================="
