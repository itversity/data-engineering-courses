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
# Login to GCP
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Enable Cloud SQL Admin API
gcloud services enable sqladmin.googleapis.com
```

### 3.2 Instance Creation
```bash
# Instance Configuration
# Instance ID: my-postgres-instance
# Region: us-central1
# Machine Type: db-f1-micro (dev/test)
# Storage: 10GB with auto-increase

# Create PostgreSQL instance
gcloud sql instances create my-postgres-instance \
    --database-version=POSTGRES_15 \
    --cpu=1 \
    --memory=3840MB \
    --region=us-central1 \
    --storage-size=10GB \
    --storage-type=SSD \
    --storage-auto-increase

# Set password
gcloud sql users set-password postgres \
    --instance=my-postgres-instance \
    --password='YOUR_NEW_PASSWORD'
```

### 3.3 Network Configuration
```bash
# Configure public IP
gcloud sql instances patch my-postgres-instance \
    --assign-ip \
    --authorized-networks=0.0.0.0/0 \
    --no-require-ssl
```

### 3.4 Connection Methods
There are multiple ways to connect to the database. We will use psql in this workshop. You can also use other tools like pgAdmin, DBeaver, etc. To use psql, you need to have it installed on your machine.

**Cloud Shell:**
```bash
gcloud sql connect my-postgres-instance --user=postgres
```

**Local psql:**
```bash
psql --host=<PUBLIC_IP> --port=5432 \
     --username=postgres \
     --dbname=postgres
```

**Connection String:**
```python
postgresql://postgres:password@<PUBLIC_IP>:5432/postgres
```

## 4. Performance Tuning Setup

### 4.1 Basic Configuration
The following are the basic settings that you can adjust to improve the performance of your database. These settings are not the best settings for production but they are good enough for this workshop. 
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
The following commands help monitor database performance by tracking query statistics.

```sql
-- Enable query statistics
CREATE EXTENSION pg_stat_statements;

-- Monitor query performance
SELECT query, calls, total_time, rows
FROM pg_stat_statements
ORDER BY total_time DESC;
```

### 4.3 Index Management
The following commands help monitor index usage and create indexes for common queries.
```sql
-- Create sample table
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE,
    amount DECIMAL(10,2)
);

-- Create indexes for common queries
CREATE INDEX idx_sales_date 
ON sales(sale_date);

-- Monitor index usage
SELECT schemaname, tablename, indexname, idx_scan
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC;
```

### 4.4. Add Additional Tables
The following commands help create additional tables and load data into them. The scripts are available in the [setup](https://github.com/itversity/data-engineering-courses/tree/main/sql-performance-tuning/setup) folder.

```sql
-- Create tables
\i setup/01_create_tables.sql

-- Load data
\i setup/02_load_data.sql
```

## 5. Best Practices

### 5.1 Security
- Enable SSL connections
- Use strong passwords
- Implement IP allowlisting
- Regular security updates

### 5.2 Backup Strategy
The following commands help configure automated backups and enable point-in-time recovery. These are not relevant for this workshop.
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
The following commands help monitor database performance by tracking active queries and table statistics.
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
The following commands help create a new database and a sample table. These are already done in the setup section.
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
The following commands help create a new user and grant necessary permissions. These are not relevant for this workshop.
```sql
-- Create application user
CREATE USER app_user WITH PASSWORD 'secure_password';
GRANT CONNECT ON DATABASE performance_tuning TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
```

### 6.3 Maintenance
The following commands help perform regular maintenance tasks like vacuuming and reindexing. These are not relevant for this workshop.
```sql
-- Regular maintenance
VACUUM ANALYZE;
REINDEX DATABASE performance_tuning;
```

## 7. Troubleshooting
The following are the common issues that you may face and how to troubleshoot them and not necessarily related to performance tuning.

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