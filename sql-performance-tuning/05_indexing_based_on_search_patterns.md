# Scenario 3: Indexing Based on Search Patterns (SARGability)

## Setup Toyota Sales Data

### Create the tables
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

CREATE TABLE toyota_sales (
    sale_id SERIAL PRIMARY KEY,
    sale_rep_id INT,
    sale_date DATE,
    car_model VARCHAR(100),
    sale_amount DECIMAL(10,2),
    commission_pct DECIMAL(5,2),
    sale_status VARCHAR(50)
);

-- Add foreign key constraint
ALTER TABLE toyota_sales 
   ADD CONSTRAINT fk_sales_reps 
   FOREIGN KEY (sale_rep_id) 
   REFERENCES toyota_sales_reps(rep_id);
```

### Load the data
Copy the data from `toyota_sales_data.csv` and `sales_reps.csv` into the tables.

```sql
\COPY toyota_sales_reps FROM 'data/sales_reps_data.csv' WITH (FORMAT csv, HEADER true);
\COPY toyota_sales FROM 'data/toyota_october_2024_sales_data.csv' WITH (FORMAT csv, HEADER true);
\COPY toyota_sales FROM 'data/toyota_november_2024_sales_data.csv' WITH (FORMAT csv, HEADER true);
\COPY toyota_sales FROM 'data/toyota_december_2024_sales_data.csv' WITH (FORMAT csv, HEADER true);
```

## What is SARGability?

SARGable (Search ARGument able) refers to queries that can effectively use indexes. A query is SARGable when predicates in the WHERE clause can utilize indexes without transforming the indexed columns.

## Common Non-SARGable vs SARGable Patterns

### 1. String Comparisons

**Non-SARGable:**
```sql
CREATE INDEX idx_sale_status ON toyota_sales(sale_status);

EXPLAIN ANALYZE
SELECT count(*)
FROM toyota_sales
WHERE LOWER(sale_status) = 'pending';
```
- Problem: Function `LOWER()` prevents index usage
- Forces full table scan

**SARGable:**
```sql
EXPLAIN ANALYZE
SELECT *
FROM toyota_sales
WHERE sale_status = 'Pending';
```
- Direct comparison allows index usage
- Better performance

### 2. Pattern Matching (LIKE)
The results might be different if the index is used. In Oracle, the index is used for the SARGable query. In PostgreSQL, the index is not used.

**Non-SARGable:**
```sql
CREATE INDEX idx_car_model ON toyota_sales(car_model);

EXPLAIN ANALYZE
SELECT sale_id, car_model, sale_amount
FROM toyota_sales
WHERE car_model LIKE '%Corolla%';
```
- Problem: Leading wildcard prevents efficient index usage
- Results in full index scan

**SARGable:**
```sql
EXPLAIN ANALYZE
SELECT sale_id, car_model, sale_amount
FROM toyota_sales
WHERE car_model LIKE 'Corolla%';
```
- No leading wildcard allows index seek
- More efficient for large datasets

## Key Principles for SARGable Queries

1. **Avoid Functions on Indexed Columns**
   - Don't wrap indexed columns in functions
   - Move transformations to the constant side

2. **Pattern Matching Best Practices**
   - Avoid leading wildcards when possible
   - Consider specialized indexes for text search

3. **Date/Time Handling**
   - Use proper date comparisons
   - Avoid functions that transform date columns

## Performance Impact

1. **Non-SARGable Queries**
   - Force full table/index scans
   - Performance degrades with data growth
   - Higher CPU and I/O usage

2. **SARGable Queries**
   - Can utilize index seeks
   - Better scalability
   - Reduced resource usage

## Best Practices

1. **Index Design**
   - Create indexes based on common search patterns
   - Consider column order in composite indexes

2. **Query Writing**
   - Keep indexed columns free of transformations
   - Rewrite queries to maintain SARGability

3. **Monitoring**
   - Use execution plans to verify index usage
   - Watch for implicit conversions

## Summary

Writing SARGable queries is crucial for optimal index utilization and query performance. By avoiding functions on indexed columns, using appropriate pattern matching, and following best practices, you can ensure your queries make effective use of indexes and maintain performance as data grows.
