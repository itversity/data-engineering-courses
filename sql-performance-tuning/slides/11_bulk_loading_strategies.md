---
theme: black
transition: slide
---

# Bulk Loading Strategies
### SQL Performance Tuning Scenario #9

---

### Key Optimization Techniques

#### Transaction Management
```sql
-- Inefficient (Auto-commit)
INSERT INTO sales_data VALUES (...);
INSERT INTO sales_data VALUES (...);

-- Optimized (Single transaction)
BEGIN;
INSERT INTO sales_data VALUES 
    (...),
    (...);
COMMIT;
```

---

### Bulk Loading Commands

#### PostgreSQL
```sql
COPY sales_data (
    sale_id, sale_rep_id, sale_date, car_model,
    sale_amount, commission_pct, sale_status
)
FROM '/path/to/data.csv'
DELIMITER ',' CSV HEADER;
```

#### MySQL
```sql
LOAD DATA INFILE '/path/to/data.csv'
INTO TABLE sales_data
FIELDS TERMINATED BY ',';
```

---

### More Bulk Loading Commands

#### SQL Server
```sql
BULK INSERT sales_data
FROM 'C:\data.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n'
);
```

---

### Performance Optimization Steps

#### 1. Disable Indexes
```sql
-- Drop indexes before load
DROP INDEX IF EXISTS idx_sales_car_model;

-- Perform bulk load
COPY sales_data FROM '/path/to/data.csv' CSV;

-- Recreate indexes
CREATE INDEX idx_sales_car_model ON sales_data(car_model);
```

---

### More Optimization Steps

#### 2. Disable Constraints
```sql
-- Disable constraints
ALTER TABLE sales_data DISABLE TRIGGER ALL;

-- Load data
COPY sales_data FROM '/path/to/data.csv' CSV;

-- Re-enable constraints
ALTER TABLE sales_data ENABLE TRIGGER ALL;
```

---

### Configuration Optimization

```sql
-- Increase memory for maintenance
SET maintenance_work_mem = '1GB';

-- Increase WAL size
SET max_wal_size = '4GB';

-- After load, reset to default
SET maintenance_work_mem = '64MB';
```

---

### Using Unlogged Tables

```sql
-- Create unlogged staging table
CREATE UNLOGGED TABLE sales_staging (
    sale_id SERIAL PRIMARY KEY,
    sale_rep_id INTEGER,
    sale_amount DECIMAL(10,2)
);

-- Load data into staging
COPY sales_staging FROM '/path/to/data.csv' CSV;

-- Transfer to permanent table
INSERT INTO sales_data 
SELECT * FROM sales_staging;
```

---

### Best Practices

#### Pre-Load Preparation
- Estimate data volume
- Plan storage requirements
- Prepare staging areas
- Backup existing data

#### During Load
- Monitor system resources
- Track progress
- Log errors
- Handle duplicates

---

### Post-Load Tasks

#### Data Verification
```sql
-- PostgreSQL
ANALYZE sales_data;
VACUUM ANALYZE sales_data;

-- MySQL
OPTIMIZE TABLE sales_data;
ANALYZE TABLE sales_data;

-- SQL Server
UPDATE STATISTICS sales_data;
ALTER INDEX ALL ON sales_data REBUILD;
```

---

### Common Pitfalls

#### Resource Constraints
- Insufficient disk space
- Memory limitations
- Network bottlenecks

#### Data Quality Issues
- Invalid formats
- Missing values
- Duplicate records

---

### Monitoring and Optimization

#### Progress Tracking
```sql
-- Check loaded rows
SELECT COUNT(*) FROM sales_data;

-- Monitor space usage
SELECT pg_size_pretty(pg_total_relation_size('sales_data'));

-- Check loading speed
SELECT current_timestamp, count(*) 
FROM sales_data;
```

---

### System Activity Monitoring

```sql
-- Monitor system activity
SELECT * FROM pg_stat_activity 
WHERE query LIKE '%COPY%';
```

---

### Summary

#### Key Requirements
1. Proper preparation and planning
2. Optimized database configuration
3. Appropriate loading technique selection
4. Careful monitoring and verification

---

### Key Takeaways

- Use bulk loading commands
- Disable unnecessary constraints
- Optimize database configuration
- Verify data integrity
- Update statistics and rebuild indexes

---

### Thank You!

#### Next Up: Scenario #10
### Advanced Database Optimization Techniques

Stay tuned for more SQL performance tuning insights! 🚀 