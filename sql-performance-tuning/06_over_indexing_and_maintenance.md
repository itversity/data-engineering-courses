# Scenario 4: Over-Indexing & Maintenance

## 4.1 What Is Over-Indexing?

Over-indexing occurs when a table has excessive indexes, typically due to:
- Adding new indexes for each query requirement without reviewing existing ones
- Creating redundant or overlapping indexes
- Keeping obsolete indexes that are no longer used

## 4.2 Impact of Over-Indexing

### Write Performance Degradation
- Each INSERT, UPDATE, or DELETE must maintain all indexes
- More indexes = higher write operation overhead
- Significant impact on high-volume systems

### Resource Consumption
- Increased storage requirements
- Higher memory usage (buffer pool)
- Extended backup and recovery times

### Maintenance Overhead
- Longer index rebuild/reorganize operations
- Extended statistics update times
- Reduced system availability during maintenance

### Query Optimizer Issues
- Too many similar indexes can confuse the optimizer
- May lead to suboptimal execution plans

## 4.3 Identifying Over-Indexing

### Using System Tools
```sql
-- SQL Server
SELECT * FROM sys.dm_db_index_usage_stats;

-- PostgreSQL
SELECT * FROM pg_stat_user_indexes;

-- MySQL
SELECT * FROM performance_schema.table_io_waits_summary_by_index_usage;
```

### Common Signs
1. Unused indexes
2. Duplicate/overlapping indexes
3. High write latency
4. Excessive storage usage

## 4.4 Index Maintenance Best Practices

### Statistics Management
```sql
-- PostgreSQL
ANALYZE table_name;

-- SQL Server
UPDATE STATISTICS table_name;

-- MySQL
ANALYZE TABLE table_name;
```

### Index Optimization
```sql
-- SQL Server
ALTER INDEX index_name ON table_name REBUILD;
ALTER INDEX index_name ON table_name REORGANIZE;

-- PostgreSQL
REINDEX TABLE table_name;

-- MySQL
OPTIMIZE TABLE table_name;
```

## 4.5 Practical Example

### Over-Indexed Table
```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    email VARCHAR(200),
    created_at DATETIME,
    status VARCHAR(50)
);

-- Excessive Indexing
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_created_at ON users(created_at);
CREATE INDEX idx_status ON users(status);
CREATE INDEX idx_email_status ON users(email, status);
CREATE INDEX idx_status_created ON users(status, created_at);
CREATE INDEX idx_email_created ON users(email, created_at);
```

### Optimized Indexing
```sql
-- Reduced to essential indexes
CREATE UNIQUE INDEX idx_email ON users(email);
CREATE INDEX idx_status_created ON users(status, created_at);
```

## 4.6 Maintenance Strategy

1. **Regular Monitoring**
   - Track index usage statistics
   - Monitor fragmentation levels
   - Analyze query patterns

2. **Scheduled Maintenance**
   - Update statistics regularly
   - Rebuild/reorganize based on fragmentation
   - Perform during low-traffic periods

3. **Index Review**
   - Audit indexes quarterly
   - Remove unused indexes
   - Consolidate overlapping indexes

## 4.7 Best Practices

1. **Before Creating New Indexes**
   - Check existing indexes
   - Analyze query patterns
   - Consider impact on writes

2. **Maintenance Windows**
   - Schedule regular maintenance
   - Use online operations when possible
   - Monitor maintenance impact

3. **Documentation**
   - Track index creation reasons
   - Document maintenance procedures
   - Keep index inventory updated

## Summary

Over-indexing is a common performance anti-pattern that can significantly impact database performance. Regular monitoring, maintenance, and careful index management are essential for maintaining optimal database performance. The key is finding the right balance between query performance and maintenance overhead.
