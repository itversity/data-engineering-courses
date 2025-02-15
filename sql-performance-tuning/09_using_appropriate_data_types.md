# Scenario 7: Using Appropriate Data Types

## Introduction

Data type selection significantly impacts database performance, affecting storage efficiency, memory usage, and query speed. Proper data type choices form the foundation of an optimized database.

## Impact Areas

1. **Storage Efficiency**
   - Each data type has different storage requirements
   - Improper choices lead to wasted space
   - Affects backup and restore times

2. **Query Performance**
   - Data type mismatches cause implicit conversions
   - Affects join operations and indexing
   - Impacts memory usage during query execution

3. **Memory Utilization**
   - Buffer cache efficiency
   - Sort and hash operation performance
   - Temporary space usage

## Common Data Type Pitfalls

### 1. Integer Type Selection
```sql
-- Inefficient (when < 2 billion records expected)
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,  -- 8 bytes
    customer_id BIGINT,           -- 8 bytes
    total_amount DECIMAL(10,2)
);

-- Optimized
CREATE TABLE orders (
    order_id INT PRIMARY KEY,     -- 4 bytes
    customer_id INT,              -- 4 bytes
    total_amount DECIMAL(10,2)
);
```

### 2. String Type Misuse
```sql
-- Inefficient
CREATE TABLE users (
    user_id VARCHAR(20),          -- For numeric IDs
    status VARCHAR(255),          -- For 'active'/'inactive'
    country_code VARCHAR(50)      -- For 2-char codes
);

-- Optimized
CREATE TABLE users (
    user_id INT,
    status CHAR(1),              -- 'A'/'I'
    country_code CHAR(2)         -- ISO codes
);
```

### 3. Temporal Data
```sql
-- Inefficient
CREATE TABLE events (
    event_id INT,
    event_time VARCHAR(30),      -- Storing timestamps as strings
    duration VARCHAR(20)         -- Storing intervals as strings
);

-- Optimized
CREATE TABLE events (
    event_id INT,
    event_time TIMESTAMP,
    duration INTERVAL
);
```

## Performance Impact Examples

### 1. Join Performance
```sql
-- Poor Performance (implicit conversion)
SELECT sr.first_name, sr.last_name, ts.car_model
FROM sales_reps_data sr
INNER JOIN toyota_sales_data ts 
    ON sr.rep_id::VARCHAR = ts.sale_rep_id;

-- Optimized
SELECT sr.first_name, sr.last_name, ts.car_model
FROM sales_reps_data sr
INNER JOIN toyota_sales_data ts 
    ON sr.rep_id = ts.sale_rep_id;
```

### 2. Storage Impact
```sql
-- Example table with 1 million rows
-- BIGINT vs INT difference: 4 bytes * 1M rows = 4MB
-- VARCHAR(255) vs CHAR(2): ~253 bytes * 1M rows = ~253MB
```

## Best Practices

1. **Integer Types**
   - Use INT for most IDs (4 bytes, up to 2 billion)
   - BIGINT only when exceeding INT limits
   - SMALLINT for small ranges (-32K to 32K)

2. **String Types**
   - CHAR for fixed-length strings
   - VARCHAR for variable-length
   - TEXT for unlimited length
   - Consider compression for large text

3. **Decimal/Numeric**
   - Use DECIMAL for exact calculations (money)
   - FLOAT/REAL for scientific calculations
   - Specify precise scale and precision

4. **Date/Time**
   - Use DATE for dates only
   - TIMESTAMP for date + time
   - INTERVAL for durations
   - Avoid string storage for temporal data

## Common Optimization Patterns

1. **ID Columns**
   ```sql
   -- Choose based on expected row count
   SMALLINT   -- Up to 32,767
   INT        -- Up to 2 billion
   BIGINT     -- Up to 9 quintillion
   ```

2. **Status Flags**
   ```sql
   -- Instead of VARCHAR
   BOOLEAN    -- True/False
   CHAR(1)    -- Single character codes
   SMALLINT   -- Small number of states
   ```

3. **Code Tables**
   ```sql
   -- For country codes, currencies, etc.
   CHAR(2)    -- ISO country codes
   CHAR(3)    -- ISO currency codes
   ```

## Performance Monitoring

1. **Check for Implicit Conversions**
   ```sql
   EXPLAIN ANALYZE
   SELECT * FROM table1 t1
   JOIN table2 t2 ON t1.id::text = t2.id;
   ```

2. **Storage Analysis**
   ```sql
   SELECT pg_size_pretty(pg_total_relation_size('table_name'));
   ```

## Summary

Proper data type selection is crucial for:
- Optimal storage utilization
- Better query performance
- Reduced memory usage
- Improved join operations

Key Takeaways:
1. Choose the smallest appropriate data type
2. Maintain consistency across related columns
3. Avoid implicit conversions
4. Consider future growth in type selection
5. Regular monitoring and optimization
