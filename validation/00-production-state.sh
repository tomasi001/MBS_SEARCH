#!/bin/bash

# Production State Management
# This script manages production-ready state, data backups, and performance indexes

set -e

echo "=========================================="
echo "🏭 PRODUCTION STATE MANAGEMENT"
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

# Configuration
PROD_DB="mbs.db"
BACKUP_DIR="backups"
FULL_DB="mbs_full.db"
INDEXES_SCRIPT="create_indexes.sql"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Function to create database backup
create_backup() {
    local db_file="$1"
    local backup_name="$2"
    
    if [ -f "$db_file" ]; then
        local timestamp=$(date +%Y%m%d-%H%M%S)
        local backup_file="$BACKUP_DIR/${backup_name}_${timestamp}.db"
        
        log_info "Creating backup: $backup_file"
        cp "$db_file" "$backup_file"
        
        # Also create a latest symlink with absolute path
        ln -sf "$(pwd)/$backup_file" "$BACKUP_DIR/${backup_name}_latest.db"
        
        log_success "Backup created: $backup_file"
        return 0
    else
        log_warning "Database file not found: $db_file"
        return 1
    fi
}

# Function to restore database from backup
restore_backup() {
    local backup_name="$1"
    local target_db="$2"
    
    local backup_file="$BACKUP_DIR/${backup_name}_latest.db"
    
    # Check if symlink exists and resolve it
    if [ -L "$backup_file" ]; then
        backup_file=$(readlink "$backup_file")
        # If it's a relative path, make it absolute
        if [[ "$backup_file" != /* ]]; then
            backup_file="$(pwd)/$backup_file"
        fi
    fi
    
    if [ -f "$backup_file" ]; then
        log_info "Restoring from backup: $backup_file"
        cp "$backup_file" "$target_db"
        log_success "Restored: $target_db"
        return 0
    else
        log_error "Backup not found: $backup_file"
        return 1
    fi
}

# Function to create performance indexes
create_performance_indexes() {
    local db_file="$1"
    
    log_info "Creating performance indexes for: $db_file"
    
    cat > "$INDEXES_SCRIPT" << 'EOF'
-- Performance indexes for MBS Clarity database

-- Items table indexes
CREATE INDEX IF NOT EXISTS idx_items_item_num ON items(item_num);
CREATE INDEX IF NOT EXISTS idx_items_category ON items(category);
CREATE INDEX IF NOT EXISTS idx_items_schedule_fee ON items(schedule_fee);

-- Relations table indexes
CREATE INDEX IF NOT EXISTS idx_relations_item_num ON relations(item_num);
CREATE INDEX IF NOT EXISTS idx_relations_target_item_num ON relations(target_item_num);
CREATE INDEX IF NOT EXISTS idx_relations_relation_type ON relations(relation_type);
CREATE INDEX IF NOT EXISTS idx_relations_item_target ON relations(item_num, target_item_num);

-- Constraints table indexes
CREATE INDEX IF NOT EXISTS idx_constraints_item_num ON constraints(item_num);
CREATE INDEX IF NOT EXISTS idx_constraints_constraint_type ON constraints(constraint_type);
CREATE INDEX IF NOT EXISTS idx_constraints_value ON constraints(value);

-- Meta table indexes
CREATE INDEX IF NOT EXISTS idx_meta_source_path ON meta(source_path);
CREATE INDEX IF NOT EXISTS idx_meta_loaded_at ON meta(loaded_at);

-- Composite indexes for common queries
CREATE INDEX IF NOT EXISTS idx_relations_type_item ON relations(relation_type, item_num);
CREATE INDEX IF NOT EXISTS idx_constraints_type_item ON constraints(constraint_type, item_num);

-- Analyze tables for query optimization
ANALYZE;
EOF

    if sqlite3 "$db_file" < "$INDEXES_SCRIPT"; then
        log_success "Performance indexes created successfully"
        rm -f "$INDEXES_SCRIPT"
        return 0
    else
        log_error "Failed to create performance indexes"
        rm -f "$INDEXES_SCRIPT"
        return 1
    fi
}

# Function to verify production state
verify_production_state() {
    local db_file="$1"
    
    log_info "Verifying production state for: $db_file"
    
    if [ ! -f "$db_file" ]; then
        log_error "Production database not found: $db_file"
        return 1
    fi
    
    # Check if database has data
    local item_count=$(sqlite3 "$db_file" "SELECT COUNT(*) FROM items;" 2>/dev/null || echo "0")
    local relation_count=$(sqlite3 "$db_file" "SELECT COUNT(*) FROM relations;" 2>/dev/null || echo "0")
    local constraint_count=$(sqlite3 "$db_file" "SELECT COUNT(*) FROM constraints;" 2>/dev/null || echo "0")
    
    log_info "Database contents:"
    log_info "  Items: $item_count"
    log_info "  Relations: $relation_count"
    log_info "  Constraints: $constraint_count"
    
    # Check if indexes exist
    local index_count=$(sqlite3 "$db_file" "SELECT COUNT(*) FROM sqlite_master WHERE type='index' AND name LIKE 'idx_%';" 2>/dev/null || echo "0")
    log_info "  Performance indexes: $index_count"
    
    # Verify minimum data requirements
    if [ "$item_count" -lt 100 ]; then
        log_warning "Low item count - may be sample data"
        return 1
    fi
    
    if [ "$index_count" -lt 5 ]; then
        log_warning "Missing performance indexes"
        return 1
    fi
    
    log_success "Production state verified"
    return 0
}

# Function to load production data
load_production_data() {
    local data_source="$1"
    
    log_info "Loading production data from: $data_source"
    
    if [ ! -f "$data_source" ]; then
        log_error "Data source not found: $data_source"
        return 1
    fi
    
    # Reset database
    log_info "Resetting database..."
    poetry run python -c "
from mbs_clarity.db import reset_db, init_schema
reset_db()
init_schema()
print('Database reset and schema initialized')
"
    
    # Load data
    log_info "Loading data..."
    if [[ "$data_source" == *.xml ]]; then
        poetry run python -m mbs_clarity._loader --xml "$data_source" --verbose
    elif [[ "$data_source" == *.csv ]]; then
        poetry run python -m mbs_clarity._loader --csv "$data_source" --verbose
    else
        log_error "Unsupported data format: $data_source"
        return 1
    fi
    
    # Create performance indexes
    create_performance_indexes "$PROD_DB"
    
    # Verify production state
    verify_production_state "$PROD_DB"
    
    log_success "Production data loaded successfully"
    return 0
}

# Function to setup test environment
setup_test_environment() {
    log_info "Setting up test environment..."
    
    # Since we have production data loaded, we don't need separate test environment
    # The production database will be used for all testing
    log_info "Using production database for testing (no separate test environment needed)"
    log_success "Test environment ready"
}

# Function to cleanup test environment
cleanup_test_environment() {
    log_info "Cleaning up test environment..."
    
    # Since we're using production database for testing, no cleanup needed
    log_info "No test environment cleanup needed (using production database)"
    log_success "Test environment cleaned up"
}

# Function to ensure production readiness
ensure_production_readiness() {
    log_info "Ensuring production readiness..."
    
    # Check if production database exists and is valid
    if ! verify_production_state "$PROD_DB"; then
        log_warning "Production database not ready"
        
        # Ask user what to do
        echo ""
        echo "Production database is not ready. Options:"
        echo "1. Load from full MBS XML dataset"
        echo "2. Load from CSV dataset"
        echo "3. Restore from backup"
        echo "4. Skip (not recommended for production)"
        echo ""
        
        read -p "Select option (1-4): " option
        
        case $option in
            1)
                if [ -f "data/mbs.xml" ]; then
                    load_production_data "data/mbs.xml"
                else
                    log_error "Full MBS XML dataset not found at data/mbs.xml"
                    return 1
                fi
                ;;
            2)
                if [ -f "data/mbs.csv" ]; then
                    load_production_data "data/mbs.csv"
                else
                    log_error "CSV dataset not found at data/mbs.csv"
                    return 1
                fi
                ;;
            3)
                restore_backup "production" "$PROD_DB"
                ;;
            4)
                log_warning "Skipping production readiness check"
                return 0
                ;;
            *)
                log_error "Invalid option"
                return 1
                ;;
        esac
    fi
    
    # Create backup of current production state
    create_backup "$PROD_DB" "production"
    
    log_success "Production readiness ensured"
    return 0
}

# Main execution
case "${1:-help}" in
    "backup")
        log_info "Creating production backup..."
        create_backup "$PROD_DB" "production"
        ;;
    "restore")
        log_info "Restoring production database..."
        restore_backup "production" "$PROD_DB"
        ;;
    "indexes")
        log_info "Creating performance indexes..."
        create_performance_indexes "$PROD_DB"
        ;;
    "verify")
        log_info "Verifying production state..."
        verify_production_state "$PROD_DB"
        ;;
    "load")
        if [ -z "$2" ]; then
            log_error "Please specify data source: ./validation/00-production-state.sh load <path_to_data>"
            exit 1
        fi
        load_production_data "$2"
        ;;
    "setup-test")
        setup_test_environment
        ;;
    "cleanup-test")
        cleanup_test_environment
        ;;
    "ensure-ready")
        ensure_production_readiness
        ;;
    "help"|*)
        echo "Production State Management Commands:"
        echo "  backup          - Create backup of production database"
        echo "  restore         - Restore production database from backup"
        echo "  indexes         - Create performance indexes"
        echo "  verify          - Verify production state"
        echo "  load <path>     - Load production data from file"
        echo "  setup-test      - Setup test environment"
        echo "  cleanup-test    - Cleanup test environment"
        echo "  ensure-ready    - Ensure production readiness"
        echo "  help            - Show this help"
        ;;
esac

echo ""
log_success "Production state management completed!"
echo "=========================================="
