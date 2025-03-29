# SQL Performance Tuning Scenario #3: Indexing Based on Search Patterns (SARGability)

Ensuring queries are **SARGable** (Search ARGument Able) is key to optimizing SQL performance. This guide explains how to structure search predicates so that indexes are effectively utilized, reducing full table scans and improving query efficiency.

## Toyota Sales Data Setup
For this scenario, we use a sample **Toyota sales dataset** with the following tables:

### Table: `toyota_sales_reps`
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

### Table: `toyota_sales`
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

### Load Data from CSV
```sql
\COPY toyota_sales_reps FROM 'data/toyota_sales/sales_reps/sales_reps_data.csv' WITH (FORMAT csv, HEADER true);
\COPY toyota_sales FROM 'data/toyota_sales/sales/toyota_october_2024_sales_data.csv' WITH (FORMAT csv, HEADER true);
\COPY toyota_sales FROM 'data/toyota_sales/sales/toyota_november_2024_sales_data.csv' WITH (FORMAT csv, HEADER true);
\COPY toyota_sales FROM 'data/toyota_sales/sales/toyota_december_2024_sales_data.csv' WITH (FORMAT csv, HEADER true);

SELECT COUNT(*) FROM toyota_sales_reps;
SELECT COUNT(*) FROM toyota_sales;
```

## What is SARGability?
**SARGability** refers to **writing queries so that search predicates can efficiently use indexes.** SARGable queries allow the database optimizer to perform an **index seek** instead of a **full table scan**, improving performance.

### Why SARGability Matters
1. **Efficient Index Utilization** → The database can quickly narrow down results.
2. **Performance Gains** → Fewer rows are scanned, reducing CPU and I/O usage.
3. **Scalability** → Index-based queries scale well as data grows.

## Writing SARGable Queries

### 1. Avoid Wrapping Indexed Columns in Functions
❌ **Non-SARGable Query:**
```sql
EXPLAIN ANALYZE
SELECT * FROM toyota_sales WHERE LOWER(sale_status) = 'pending';
```
🔴 Problem: The function `LOWER(sale_status)` prevents index usage.

✅ **SARGable Query:**
```sql
CREATE INDEX idx_sale_status ON toyota_sales(sale_status);

EXPLAIN ANALYZE
SELECT * FROM toyota_sales WHERE sale_status = 'Pending';
```
✅ **Fix:** Direct comparison allows the index to be used efficiently.

### 2. Avoid Leading Wildcards in Pattern Matching
❌ **Non-SARGable Query:**
```sql
EXPLAIN ANALYZE
SELECT sale_id, car_model FROM toyota_sales WHERE car_model LIKE '%Corolla%';
```
🔴 Problem: Leading `%` prevents index usage, causing a **full table scan** or **full index scan** with a high cost.

✅ **SARGable Query:**
```sql
CREATE INDEX idx_car_model ON toyota_sales(car_model);

EXPLAIN ANALYZE
SELECT sale_id, car_model FROM toyota_sales WHERE car_model LIKE 'Corolla%';
```
✅ **Fix:** Use a trailing wildcard (`LIKE 'Corolla%'`) to allow index seeks.

### 3. Use Direct Comparisons Instead of Calculations on Columns
❌ **Non-SARGable Query:**
```sql
EXPLAIN ANALYZE
SELECT * FROM toyota_sales WHERE sale_date + INTERVAL '1 day' > '2025-01-01';
```
🔴 Problem: The calculation on `sale_date` makes the index unusable.

✅ **SARGable Query:**
```sql
EXPLAIN ANALYZE
SELECT * FROM toyota_sales WHERE sale_date > '2024-12-31';
```
✅ **Fix:** Move transformations to the constant side of the comparison.

## Key Principles for SARGable Queries
✅ **Avoid Functions on Indexed Columns**
- Move transformations to the **constant** side of comparisons.

✅ **Pattern Matching Best Practices**
- Avoid leading wildcards (`'%search%'`), prefer trailing ones (`'search%'`).
- Consider specialized indexes like **full-text search** for complex patterns.

✅ **Date/Time Handling**
- Compare **dates directly** instead of applying functions (`YEAR(sale_date) = 2025` → ❌).

✅ **Monitor Execution Plans**
- Use `EXPLAIN ANALYZE` to check if queries are **index-seek friendly**.
- Watch for implicit type conversions affecting SARGability.

## Performance Impact
❌ **Non-SARGable Queries**
- Full table scans → **Performance degrades as data grows**.
- Increased CPU and I/O usage.

✅ **SARGable Queries**
- **Index seeks** improve query efficiency.
- **Better scalability** for large datasets.

## Best Practices for SARGability
### **Index Design**
- Create indexes based on **common search patterns**.
- Use **composite indexes** if filtering involves multiple columns.

### **Query Writing**
- Keep indexed columns **free of transformations**.
- Rewrite queries to ensure they are **SARGable**.

### **Monitoring & Optimization**
- Use **execution plans** to confirm index usage.
- Watch out for **implicit conversions**.

## Summary
Writing **SARGable queries** ensures optimal **index utilization** and **query performance**. By avoiding functions on indexed columns, using proper pattern matching, and following best practices, you can significantly improve database efficiency.

## Looking Ahead
In **Scenario #4**, we will cover **Indexing for High-Concurrency Workloads**, exploring strategies for optimizing databases in multi-user environments.

Stay tuned! 🚀
