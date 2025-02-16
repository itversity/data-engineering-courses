# Scenario 6: Table Partitioning and Partition Pruning

## 6.1 What Is Table Partitioning?

Table partitioning divides large tables into smaller, manageable physical segments while maintaining a single logical view. Each partition contains a subset of data based on defined criteria (partition key).

## 6.2 Benefits of Partitioning

1. **Performance Optimization**
   - Partition pruning eliminates irrelevant data segments
   - Reduced I/O through targeted partition access
   - Parallel query execution possibilities

2. **Improved Manageability**
   - Easier maintenance of large tables
   - Simplified backup and recovery
   - Efficient data archival

3. **Enhanced Scalability**
   - Better handling of large datasets
   - Improved query performance
   - Efficient resource utilization

## 6.3 Partitioning Strategies

### Range Partitioning
```sql
-- Create partitioned table
-- sale_id,sale_rep_id,sale_date,car_model,sale_amount,commission_pct,sale_status
CREATE TABLE toyota_sales_partitioned (
    sale_id INT,
    sale_rep_id INT,
    sale_date DATE,
    car_model VARCHAR(50),
    sale_amount DECIMAL(12,2),
    commission_pct DECIMAL(5,2),
    sale_status VARCHAR(50)****
) PARTITION BY RANGE (sale_date);

-- Create monthly partitios for October to December 2024
CREATE TABLE toyota_sales_2024_10 PARTITION OF toyota_sales_partitioned
    FOR VALUES FROM ('2024-10-01') TO ('2024-11-01');
CREATE TABLE toyota_sales_2024_11 PARTITION OF toyota_sales_partitioned
    FOR VALUES FROM ('2024-11-01') TO ('2024-12-01');
CREATE TABLE toyota_sales_2024_12 PARTITION OF toyota_sales_partitioned
    FOR VALUES FROM ('2024-12-01') TO ('2025-01-01');

-- Insert data into the partitioned table
INSERT INTO toyota_sales_partitioned
SELECT * FROM toyota_sales;
```

### List Partitioning
```sql
-- Create list partitioned table using region
-- sale_id,sale_rep_id,sale_date,car_model,sale_amount,commission_pct,sale_status
CREATE TABLE toyota_sales_list_partitioned (
    sale_id INT,
    sale_rep_id INT,
    sale_date DATE,
    car_model VARCHAR(50),
    sale_amount DECIMAL(12,2),
    commission_pct DECIMAL(5,2),
    sale_status VARCHAR(50)
) PARTITION BY LIST (sale_status);

-- Create partitions for each sale status
CREATE TABLE toyota_sales_status_pending PARTITION OF toyota_sales_list_partitioned
    FOR VALUES IN ('Pending');
CREATE TABLE toyota_sales_status_completed PARTITION OF toyota_sales_list_partitioned
    FOR VALUES IN ('Completed');
CREATE TABLE toyota_sales_status_cancelled PARTITION OF toyota_sales_list_partitioned
    FOR VALUES IN ('Cancelled');

-- Insert data into the partitioned table
INSERT INTO toyota_sales_list_partitioned
SELECT * FROM toyota_sales;
```

### Hash Partitioning
```sql
-- First create the parent table
CREATE TABLE toyota_sales_hash_partitioned (
    sale_id INT,
    sale_rep_id INT,
    sale_date DATE,
    car_model VARCHAR(50),
    sale_amount DECIMAL(12,2),
    commission_pct DECIMAL(5,2),
    sale_status VARCHAR(50)
) PARTITION BY HASH (sale_rep_id);

-- Then create the individual hash partitions
CREATE TABLE toyota_sales_hash_0 PARTITION OF toyota_sales_hash_partitioned 
    FOR VALUES WITH (MODULUS 4, REMAINDER 0);

CREATE TABLE toyota_sales_hash_1 PARTITION OF toyota_sales_hash_partitioned 
    FOR VALUES WITH (MODULUS 4, REMAINDER 1);

CREATE TABLE toyota_sales_hash_2 PARTITION OF toyota_sales_hash_partitioned 
    FOR VALUES WITH (MODULUS 4, REMAINDER 2);

CREATE TABLE toyota_sales_hash_3 PARTITION OF toyota_sales_hash_partitioned 
    FOR VALUES WITH (MODULUS 4, REMAINDER 3);

-- Insert data into the partitioned table
INSERT INTO toyota_sales_hash_partitioned
SELECT * FROM toyota_sales;
```

## 6.4 Partition Pruning Example

### Without Partitioning
For this example, we will use the `toyota_sales` table which has 10 years of data. As the table is not partitioned, the query will scan the entire table to get the result for October 2024.
```sql
-- Query that benefits from partition pruning
-- Get count and revenue by status for October 2024

EXPLAIN ANALYZE
SELECT sale_status, COUNT(*), SUM(sale_amount)
FROM toyota_sales
WHERE sale_date >= '2024-10-01' 
    AND sale_date < '2024-11-01'
GROUP BY sale_status
ORDER BY sale_status;

-- Scans the entire table. If the table have 10 years of data, it will scan all 10 years of data to get the result for October 2024.
```

### With Partitioning
Partitioning is a technique that allows the database to skip irrelevant partitions, reducing the amount of data scanned and improving query performance. This process is called partition pruning.

```sql
EXPLAIN ANALYZE
SELECT sale_status, COUNT(*), SUM(sale_amount)
FROM toyota_sales_partitioned
WHERE sale_date >= '2024-10-01' 
    AND sale_date < '2024-11-01'
GROUP BY sale_status
ORDER BY sale_status;

-- Only scans the 2024_10 partition instead of the entire table. Even if the table has 10 years of data, it will only scan the 2024_10 partition which is less than 1% of the data (1 month versus 120 months).
```
Partition pruning is a technique that allows the database to skip irrelevant partitions, reducing the amount of data scanned and improving query performance.

You can see similar behavior even with other partitioning strategies (if applicable).

Range partitioning is the most common partitioning strategy and is supported by most databases.

## 6.5 Platform-Specific Implementation

### PostgreSQL
- Declarative partitioning (PostgreSQL 10+)
- Range, list, and hash methods
- Partition pruning at planning and execution

### MySQL
- Range, list, hash, and key partitioning
- Maximum 1024 partitions per table
- Automatic partition pruning

### SQL Server
- Partition functions and schemes
- Up to 15,000 partitions
- Aligned indexes for better performance

### Oracle
- Advanced partitioning features
- Range, list, hash, composite
- Partition-wise joins

## 6.6 Best Practices

1. **Partition Key Selection**
   - Choose frequently filtered columns
   - Ensure sufficient cardinality
   - Consider query patterns

2. **Partition Size Management**
   - Avoid too large or too small partitions
   - Plan for data growth
   - Monitor partition usage

3. **Indexing Strategy**
   - Consider local vs. global indexes
   - Align indexes with partition keys
   - Monitor index usage

4. **Maintenance Procedures**
   - Regular partition management
   - Archival strategies
   - Statistics updates

## 6.7 Common Pitfalls

1. **Over-Partitioning**
   - Too many small partitions
   - Increased management overhead
   - Complex maintenance

2. **Poor Partition Key Choice**
   - Insufficient pruning
   - Uneven data distribution
   - Suboptimal performance

3. **Inadequate Monitoring**
   - Missing partition usage patterns
   - Delayed maintenance
   - Performance degradation

## 6.8 Summary

Table partitioning is a powerful technique for managing large-scale databases. Success depends on:
- Choosing appropriate partitioning strategies
- Careful partition key selection
- Regular maintenance and monitoring
- Understanding platform-specific features

When implemented correctly, partitioning provides:
- Improved query performance
- Better data management
- Enhanced scalability
- Efficient maintenance operations
