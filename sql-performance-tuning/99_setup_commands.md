# PostgreSQL Setup Commands Sequence

## 1. GCP Setup Commands
```bash
# Login to GCP
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Enable Cloud SQL Admin API
gcloud services enable sqladmin.googleapis.com
```

## 2. Instance Creation
```bash
# Create PostgreSQL instance
gcloud sql instances create my-postgres-instance \
    --database-version=POSTGRES_15 \
    --cpu=1 \
    --memory=3840MB \
    --region=us-central1 \
    --storage-size=10GB \
    --storage-type=SSD \
    --storage-auto-increase

# Configure public IP
gcloud sql instances patch my-postgres-instance \
    --assign-ip \
    --authorized-networks=0.0.0.0/0 \
    --no-require-ssl

# Set password
gcloud sql users set-password postgres \
    --instance=my-postgres-instance \
    --password='YOUR_NEW_PASSWORD'
```

## 3. Database Connection
```bash
# Connect via Cloud Shell
gcloud sql connect my-postgres-instance --user=postgres

# Connect via psql (local)
psql --host=<PUBLIC_IP> --port=5432 --username=postgres --dbname=postgres
```

## 4. Initial Database Setup
```sql
-- Create database
CREATE DATABASE performance_tuning;

-- Connect to new database
\c performance_tuning

-- Create sample table
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE,
    amount DECIMAL(10,2)
);

-- Create test user
CREATE USER app_user WITH PASSWORD 'secure_password';
GRANT CONNECT ON DATABASE performance_tuning TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;
```

## 5. Performance Configuration
```sql
-- Check current settings
SHOW max_connections;
SHOW shared_buffers;
SHOW work_mem;

-- Enable performance monitoring
CREATE EXTENSION pg_stat_statements;

-- Create test index
CREATE INDEX idx_sales_date ON sales(sale_date);
```

## 6. Test Queries
```sql
-- Insert test data
INSERT INTO sales (sale_date, amount) 
VALUES 
    (CURRENT_DATE, 100.00),
    (CURRENT_DATE - 1, 200.00),
    (CURRENT_DATE - 2, 300.00);

-- Test query with EXPLAIN
EXPLAIN ANALYZE
SELECT * FROM sales 
WHERE sale_date >= CURRENT_DATE - 7;

-- Check index usage
SELECT schemaname, tablename, indexname, idx_scan
FROM pg_stat_user_indexes
WHERE tablename = 'sales';
```

## 7. Monitoring Queries
```sql
-- Check active queries
SELECT pid, query, state
FROM pg_stat_activity
WHERE state != 'idle';

-- Check query statistics
SELECT query, calls, total_time, rows
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 5;

-- Check table statistics
SELECT relname, seq_scan, idx_scan
FROM pg_stat_user_tables
WHERE relname = 'sales';
```

## 8. Maintenance Commands
```sql
-- Update statistics
ANALYZE sales;

-- Clean up table
VACUUM sales;

-- Rebuild indexes
REINDEX TABLE sales;

-- Clear query statistics
SELECT pg_stat_statements_reset();
```

## 9. Backup Commands
```sql
-- Check backup status
SELECT * FROM pg_stat_archiver;

-- Create manual backup (GCP)
gcloud sql backups create --instance=my-postgres-instance

-- List backups
gcloud sql backups list --instance=my-postgres-instance
```

## 10. Cleanup Commands
```sql
-- Remove test data
TRUNCATE TABLE sales;

-- Drop test database (if needed)
DROP DATABASE IF EXISTS performance_tuning;

-- Remove test user
DROP USER IF EXISTS app_user;
```

## 11. Instance Cleanup (if needed)
```bash
# Delete instance
gcloud sql instances delete my-postgres-instance
```

Note: Replace placeholders:
- `YOUR_PROJECT_ID` with your GCP project ID
- `<PUBLIC_IP>` with your instance's IP address
- Adjust memory, storage, and region values as needed
- Change passwords to secure values 