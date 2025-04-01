---
theme: black
transition: slide
---

# Table Partitioning & Partition Pruning
### SQL Performance Tuning Scenario #6

---

### What Is Table Partitioning?

- Splits large tables into smaller segments
- Maintains single logical view
- Improves query performance
- Enhances manageability and scalability

---

### How Table Partitioning Works

#### Logical vs. Physical Storage
- Logically unified (single table view)
- Physically split across partitions
- Based on partition key

#### Partition Key
- Column(s) used to distribute data
- Crucial for performance and scalability

---

### Why Use Table Partitioning?

- Faster Query Performance
- Optimized Storage Management
- Efficient Data Maintenance
- Parallel Processing
- Reduced Index Overhead

---

### When to Use Partitioning

✅ Tables with millions/billions of rows
<br>
✅ Data with clear logical divisions
<br>
✅ Frequent filtering on specific column
<br>
✅ Historical data management

---

### When NOT to Use Partitioning

🚫 Small tables (few million rows)
<br>
🚫 Queries not filtering by partition key
<br>
🚫 Read-heavy workloads without maintenance needs

---

### Partitioning Strategies

1. Range Partitioning
2. List Partitioning
3. Hash Partitioning

---

### Range Partitioning Example

```sql
CREATE TABLE toyota_sales_partitioned (
    sale_id INT,
    sale_rep_id INT,
    sale_date DATE,
    car_model VARCHAR(50),
    sale_amount DECIMAL(12,2),
    commission_pct DECIMAL(5,2),
    sale_status VARCHAR(50)
) PARTITION BY RANGE (sale_date);

-- Create monthly partitions
CREATE TABLE toyota_sales_2024_10 PARTITION OF toyota_sales_partitioned
    FOR VALUES FROM ('2024-10-01') TO ('2024-11-01');

CREATE TABLE toyota_sales_2024_11 PARTITION OF toyota_sales_partitioned
    FOR VALUES FROM ('2024-11-01') TO ('2024-12-01');

CREATE TABLE toyota_sales_2024_12 PARTITION OF toyota_sales_partitioned
    FOR VALUES FROM ('2024-12-01') TO ('2025-01-01');

INSERT INTO toyota_sales_partitioned
SELECT * FROM toyota_sales;

COMMIT;
```

---

### List Partitioning Example

```sql
CREATE TABLE toyota_sales_list_partitioned (
    sale_id INT,
    sale_rep_id INT,
    sale_date DATE,
    car_model VARCHAR(50),
    sale_amount DECIMAL(12,2),
    commission_pct DECIMAL(5,2),
    sale_status VARCHAR(50)
) PARTITION BY LIST (sale_status);

-- Create status-based partitions
CREATE TABLE toyota_sales_status_pending PARTITION OF toyota_sales_list_partitioned
    FOR VALUES IN ('Pending');

CREATE TABLE toyota_sales_status_completed PARTITION OF toyota_sales_list_partitioned
    FOR VALUES IN ('Completed');

CREATE TABLE toyota_sales_status_cancelled PARTITION OF toyota_sales_list_partitioned
    FOR VALUES IN ('Cancelled');

INSERT INTO toyota_sales_list_partitioned
SELECT * FROM toyota_sales;

COMMIT;
```

---

### Hash Partitioning Example

```sql
CREATE TABLE toyota_sales_hash_partitioned (
    sale_id INT,
    sale_rep_id INT,
    sale_date DATE,
    car_model VARCHAR(50),
    sale_amount DECIMAL(12,2),
    commission_pct DECIMAL(5,2),
    sale_status VARCHAR(50)
) PARTITION BY HASH (sale_rep_id);

-- Create hash partitions
CREATE TABLE toyota_sales_hash_0 PARTITION OF toyota_sales_hash_partitioned
    FOR VALUES WITH (MODULUS 4, REMAINDER 0);
```

---

### Understanding Partition Pruning

- Optimizes query performance
- Reduces partitions to scan
- Automatic based on query filters
- Improves resource utilization

```sql
EXPLAIN 
SELECT *
FROM toyota_sales
WHERE sale_status = 'Completed';

EXPLAIN 
SELECT *
FROM toyota_sales_list_partitioned
WHERE sale_status = 'Completed';
```

---

### Best Practices

#### Choosing Partition Key
- Frequently used in WHERE conditions
- Sufficient distinct values
- Avoid high-cardinality columns

#### Managing Partition Size
- Balance partition sizes
- Plan for future growth
- Use historical trends

---

### More Best Practices

#### Indexing Strategy
- Use local indexes
- Align with partition key
- Consider global indexes

#### Maintenance
- Regular cleanup and archival
- Update table statistics
- Monitor query execution plans

---

### Common Pitfalls

#### Over-Partitioning
- Too many small partitions
- Higher disk I/O
- Complex maintenance

#### Poor Partition Key Choice
- Insufficient pruning
- Uneven data distribution
- Suboptimal performance

---

### Database-Specific Features

#### PostgreSQL
- Range, List, Hash partitioning
- Automatic partition pruning
- Partition-wise joins

#### MySQL
- Up to 1024 partitions
- Four partitioning methods
- Automatic pruning

---

### More Database Features

#### SQL Server
- Up to 15,000 partitions
- Partition functions & schemes
- Partition switching

#### Oracle
- Most advanced features
- Composite partitioning
- Automatic maintenance

---

### Summary

- Partitioning for large datasets
- Choose right strategy
- Monitor and maintain
- Avoid common pitfalls

---

### Thank You!

#### Next Up: Scenario #7
### Advanced Database Optimization Techniques

Stay tuned for more SQL performance tuning insights! 🚀 