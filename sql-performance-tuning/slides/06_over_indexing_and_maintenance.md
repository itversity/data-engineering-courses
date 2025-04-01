---
theme: black
transition: slide
---

# Over-Indexing & Maintenance
### SQL Performance Tuning Scenario #4

---

### What Is Over-Indexing?

- Excessive indexes on tables
- Common causes:
  - Adding indexes for each query
  - Creating redundant indexes
  - Keeping obsolete indexes

---

### Impact of Over-Indexing

#### Write Performance
- Higher overhead for INSERT/UPDATE/DELETE
- Each index must be maintained
- Significant impact on high-volume systems

#### Resource Usage
- Increased storage requirements
- Higher memory usage
- Longer backup/recovery times

---

### Identifying Over-Indexing

#### System Tools
```sql
-- PostgreSQL
SELECT * FROM pg_stat_user_indexes;

-- SQL Server
SELECT * FROM sys.dm_db_index_usage_stats;

-- MySQL
SELECT * FROM performance_schema.table_io_waits_summary_by_index_usage;
```

---

### Common Signs

- Unused indexes
- Duplicate/overlapping indexes
- High write latency
- Excessive storage usage

---

### Index Maintenance

#### Statistics Management
```sql
-- PostgreSQL
ANALYZE table_name;

-- SQL Server
UPDATE STATISTICS table_name;

-- MySQL
ANALYZE TABLE table_name;
```

---

### Index Optimization

```sql
-- SQL Server
ALTER INDEX index_name ON table_name REBUILD;

-- PostgreSQL
REINDEX TABLE table_name;

-- MySQL
OPTIMIZE TABLE table_name;
```

---

### Example: Over-Indexed Table

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

---

### Optimized Indexing

```sql
-- Reduced to essential indexes
CREATE UNIQUE INDEX idx_email ON users(email);
CREATE INDEX idx_status_created ON users(status, created_at);
```

---

### Maintenance Strategy

1. Regular Monitoring
   - Track index usage
   - Monitor fragmentation
   - Analyze query patterns

2. Scheduled Maintenance
   - Update statistics
   - Rebuild/reorganize
   - Low-traffic periods

---

### Best Practices

#### Before Creating Indexes
- Check existing indexes
- Analyze query patterns
- Consider write impact

#### Maintenance Windows
- Schedule regular maintenance
- Use online operations
- Monitor impact

---

### Documentation

- Track index creation reasons
- Document maintenance procedures
- Keep index inventory updated

---

### Summary

- Balance query performance vs. maintenance
- Regular monitoring is essential
- Careful index management
- Document and review regularly

---

### Thank You!

#### Next Up: Scenario #5
### Advanced Indexing Strategies

Stay tuned for more SQL performance tuning insights! 🚀 