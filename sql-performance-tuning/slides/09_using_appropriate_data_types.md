---
theme: black
transition: slide
---

# Using Appropriate Data Types
### SQL Performance Tuning Scenario #7

---

### Why Data Types Matter?

#### Impact Areas
- Storage Efficiency
- Query Performance
- Memory Utilization
- Index Effectiveness

#### Consequences of Poor Choices
- Excessive storage usage
- Slower query performance
- Higher memory consumption
- Inefficient indexing

---

### Storage Efficiency

#### Examples
- `BIGINT` (8 bytes) vs. `INT` (4 bytes)
- `VARCHAR(255)` vs. `CHAR(2)`
- Impact on backup/restore performance

#### Storage Impact
- Wasted space
- Larger data sizes
- Higher storage costs

---

### Query Performance

#### Data Type Mismatches
```sql
-- Poor Performance (String Conversion)
SELECT sr.first_name, sr.last_name, ts.car_model
FROM sales_reps sr
INNER JOIN sales ts 
    ON sr.rep_id::VARCHAR = ts.sale_rep_id;

-- Optimized (Matching Types)
SELECT sr.first_name, sr.last_name, ts.car_model
FROM sales_reps sr
INNER JOIN sales ts 
    ON sr.rep_id = ts.sale_rep_id;
```

---

### Common Data Type Pitfalls

#### 1. Integer Type Selection
```sql
-- Inefficient
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

---

### Integer Type Guidelines

- `SMALLINT` (2 bytes): Up to 32,767 rows
- `INT` (4 bytes): Up to 2 billion rows
- `BIGINT` (8 bytes): Beyond 2 billion rows

---

### String Type Misuse

```sql
-- Inefficient
CREATE TABLE users (
    status VARCHAR(255),      -- Only stores 'Active' or 'Inactive'
    country_code VARCHAR(50)  -- Only 2 characters needed
);

-- Optimized
CREATE TABLE users (
    status CHAR(1),           -- 'A' / 'I'
    country_code CHAR(2)      -- ISO country codes
);
```

---

### Date/Time Storage

```sql
-- Inefficient
CREATE TABLE events (
    event_id INT PRIMARY KEY,
    event_time VARCHAR(30),  -- Bad choice
    duration VARCHAR(20)
);

-- Optimized
CREATE TABLE events (
    event_id INT PRIMARY KEY,
    event_time TIMESTAMP,    -- Better choice
    duration INTERVAL
);
```

---

### Best Practices

#### 1. Choose Smallest Suitable Type
- Use INT instead of BIGINT
- Use CHAR instead of VARCHAR for fixed-length
- Use appropriate decimal precision

#### 2. Maintain Consistency
- Match primary/foreign key types
- Avoid type mismatches in JOINs
- Use consistent types across tables

---

### More Best Practices

#### 3. Store Data Correctly
- Use INT/DECIMAL for numeric data
- Use DATE/TIMESTAMP for dates
- Use appropriate string types

#### 4. String Storage
- Use VARCHAR(N) instead of VARCHAR(255)
- Use TEXT sparingly
- Use CHAR for fixed-length values

---

### Monitoring Data Types

#### Detecting Implicit Conversions
```sql
-- Check for implicit conversions
EXPLAIN ANALYZE
SELECT * FROM sales s
JOIN customers c ON s.customer_id::text = c.customer_id;
```

#### Analyzing Storage Usage
```sql
-- PostgreSQL
SELECT pg_size_pretty(pg_total_relation_size('table_name'));
```

---

### Common Issues to Monitor

- Data type mismatches in JOINs
- Oversized columns
- Unnecessary type conversions
- Storage inefficiencies

---

### Summary

#### Key Takeaways
- Choose smallest appropriate type
- Maintain consistency
- Avoid implicit conversions
- Monitor and optimize regularly

---

### Thank You!

#### Next Up: Scenario #8
### Advanced Query Optimization Techniques

Stay tuned for more SQL performance tuning insights! 🚀 