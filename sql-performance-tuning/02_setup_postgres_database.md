# Setting Up PostgreSQL Database Using GCP Cloud SQL

## 1. Google Cloud Platform (GCP) Overview

### What is GCP?
- Google's public cloud platform
- Offers managed services for computing, storage, and databases
- Provides Cloud SQL for managed database services
- Focuses on application development rather than infrastructure management

### Getting Started with GCP
```bash
# Visit cloud.google.com
# Click "Get started for free"
# Receive $300 free credits
```

## 2. Why PostgreSQL?

### Key Features
1. **Standards Compliance**
   - Complex query support
   - Table partitioning
   - Window functions
   - Custom extensions (PostGIS)

2. **Performance**
   - Efficient OLTP handling
   - Analytical workload support
   - Advanced indexing capabilities

3. **Community Support**
   - Active development
   - Extensive documentation
   - Rich ecosystem

### Universal Database Concepts
- Indexing strategies
- Query execution plans
- Table partitioning
- Bulk loading operations
- Concurrency control

## 3. Setting Up PostgreSQL on Cloud SQL

### 3.1 Project Setup
```bash
# Navigate to console.cloud.google.com
# Create new project or select existing
# Enable Cloud SQL Admin API
```

### 3.2 Instance Creation
```sql
-- Instance Configuration
Instance ID: my-postgres-instance
Region: us-central1
Machine Type: db-f1-micro (dev/test)
Storage: 10GB with auto-increase
```

### 3.3 Network Configuration
```bash
# Public IP Setup
gcloud sql instances patch my-postgres-instance \
    --assign-ip

# Private IP Setup (Production)
gcloud sql instances patch my-postgres-instance \
    --network=VPC_NETWORK_NAME \
    --require-ssl
```

### 3.4 Connection Methods

**Cloud Shell:**
```bash
gcloud sql connect my-postgres-instance --user=postgres
```

**Local psql:**
```bash
psql --host=<PUBLIC_IP> --port=5432 \
     --username=postgres --dbname=postgres
```

**Connection String:**
```python
postgresql://postgres:password@<PUBLIC_IP>:5432/postgres
```

## 4. Performance Tuning Setup

### 4.1 Basic Configuration
```sql
-- Check current settings
SHOW max_connections;
SHOW shared_buffers;
SHOW work_mem;

-- Adjust settings
ALTER SYSTEM SET shared_buffers = '1GB';
ALTER SYSTEM SET work_mem = '16MB';
```

### 4.2 Monitoring Setup
```sql
-- Enable query statistics
CREATE EXTENSION pg_stat_statements;

-- Monitor query performance
SELECT query, calls, total_time, rows
FROM pg_stat_statements
ORDER BY total_time DESC;
```

### 4.3 Index Management
```sql
-- Create indexes for common queries
CREATE INDEX idx_sales_date 
ON sales(sale_date);

-- Monitor index usage
SELECT schemaname, tablename, indexname, idx_scan
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC;
```

## 5. Best Practices

### 5.1 Security
- Enable SSL connections
- Use strong passwords
- Implement IP allowlisting
- Regular security updates

### 5.2 Backup Strategy
```sql
-- Check backup settings
SELECT * FROM pg_stat_archiver;

-- Configure automated backups
-- Via GCP Console:
-- Enable point-in-time recovery
-- Set backup window
-- Define retention period
```

### 5.3 Monitoring
```sql
-- Check active queries
SELECT pid, query, state
FROM pg_stat_activity
WHERE state != 'idle';

-- Monitor table statistics
SELECT relname, seq_scan, idx_scan
FROM pg_stat_user_tables;
```

## 6. Common Operations

### 6.1 Database Creation
```sql
CREATE DATABASE performance_tuning;
\c performance_tuning

-- Create sample table
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE,
    amount DECIMAL(10,2)
);
```

### 6.2 User Management
```sql
-- Create application user
CREATE USER app_user WITH PASSWORD 'secure_password';
GRANT CONNECT ON DATABASE performance_tuning TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
```

### 6.3 Maintenance
```sql
-- Regular maintenance
VACUUM ANALYZE;
REINDEX DATABASE performance_tuning;
```

## 7. Troubleshooting

### Common Issues
1. **Connection Problems**
   - Check firewall rules
   - Verify IP allowlisting
   - Confirm SSL requirements

2. **Performance Issues**
   - Monitor resource usage
   - Check query plans
   - Review connection pools

3. **Storage Concerns**
   - Monitor disk usage
   - Check WAL size
   - Review backup storage

## Summary

Key Setup Points:
1. Create GCP project and enable APIs
2. Configure PostgreSQL instance
3. Set up networking and security
4. Implement monitoring and maintenance
5. Follow best practices for performance

Next Steps:
- Configure additional databases
- Set up replication if needed
- Implement backup strategies
- Monitor performance metrics 