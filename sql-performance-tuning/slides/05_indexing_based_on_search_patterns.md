---
theme: black
transition: slide
---

# Indexing Based on Search Patterns
### SQL Performance Tuning Scenario #3

---

### What is SARGability?

- Search ARGument Able
- Writing queries for efficient index usage
- Enables index seeks over table scans
- Improves query performance

---

### Toyota Sales Data Setup

#### Tables Structure

```sql
CREATE TABLE toyota_sales_reps (
    rep_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(20),
    hire_date DATE,
    region VARCHAR(50),
    status VARCHAR(50)
);
```

---

### Sales Table Structure

```sql
CREATE TABLE toyota_sales (
    sale_id SERIAL PRIMARY KEY,
    sale_rep_id INT,
    sale_date DATE,
    car_model VARCHAR(100),
    sale_amount DECIMAL(10,2),
    commission_pct DECIMAL(5,2),
    sale_status VARCHAR(50),
    FOREIGN KEY (sale_rep_id) REFERENCES toyota_sales_reps(rep_id)
);
```

---

### Non-SARGable Query Examples

#### 1. Functions on Indexed Columns
```sql
-- Bad: Function prevents index usage
SELECT * FROM toyota_sales 
WHERE LOWER(sale_status) = 'pending';
```

#### 2. Leading Wildcards
```sql
-- Bad: Full table scan
SELECT sale_id, car_model 
FROM toyota_sales 
WHERE car_model LIKE '%Corolla%';
```

---

### SARGable Query Examples

#### 1. Direct Column Comparison
```sql
-- Good: Index can be used
SELECT * FROM toyota_sales 
WHERE sale_status = 'Pending';
```

#### 2. Trailing Wildcards
```sql
-- Good: Index seek possible
SELECT sale_id, car_model 
FROM toyota_sales 
WHERE car_model LIKE 'Corolla%';
```

---

### Date/Time Handling

#### Non-SARGable
```sql
-- Bad: Function prevents index usage
SELECT * FROM toyota_sales 
WHERE sale_date + INTERVAL '1 day' > '2025-01-01';
```

#### SARGable
```sql
-- Good: Direct date comparison
SELECT * FROM toyota_sales 
WHERE sale_date > '2024-12-31';
```

---

### Key Principles

1. Avoid Functions on Indexed Columns
2. Use Proper Pattern Matching
3. Direct Date/Time Comparisons
4. Monitor Execution Plans

---

### Performance Impact

#### Non-SARGable Queries
- Full table scans
- Performance degrades with data growth
- High CPU and I/O usage

#### SARGable Queries
- Index seeks
- Better scalability
- Efficient resource usage

---

### Best Practices

#### Index Design
- Create indexes based on search patterns
- Use composite indexes when needed

#### Query Writing
- Keep indexed columns clean
- Rewrite for SARGability

---

### Monitoring & Optimization

- Use EXPLAIN ANALYZE
- Watch for implicit conversions
- Monitor index usage
- Regular performance reviews

---

### Summary

- SARGability is crucial for performance
- Avoid functions on indexed columns
- Use proper pattern matching
- Monitor and optimize regularly

---

### Thank You!

#### Next Up: Scenario #4
### Indexing for High-Concurrency Workloads

Stay tuned for more SQL performance tuning insights! 🚀 