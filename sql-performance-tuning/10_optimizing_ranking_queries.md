# Scenario 8: Optimizing Ranking Queries

## Introduction

Ranking queries are essential for many business applications, from leaderboards to sales reports. However, they can become performance bottlenecks if not properly optimized. Understanding how to leverage window functions and proper indexing is crucial for performance.

## Common Ranking Scenarios

### 1. Top-N Queries

**Inefficient Approach:**
```sql
SELECT *
FROM (
    SELECT *, 
           ROW_NUMBER() OVER (ORDER BY sale_amount DESC) AS row_num
    FROM toyota_sales_data
) sub
WHERE row_num <= 5;
```
**Issues:**
- Calculates ranking for entire dataset
- Excessive memory usage
- Poor performance on large datasets

**Optimized Approach:**
```sql
SELECT *
FROM toyota_sales_data
ORDER BY sale_amount DESC
LIMIT 5;
```
**Benefits:**
- Uses index for sorting
- Only processes needed rows
- Minimal memory footprint

### 2. Partitioned Rankings

**Inefficient Approach:**
```sql
SELECT t1.*, 
       (SELECT COUNT(*) 
        FROM toyota_sales_data t2 
        WHERE t2.car_model = t1.car_model 
          AND t2.sale_amount >= t1.sale_amount) as rank
FROM toyota_sales_data t1;
```

**Optimized Approach:**
```sql
SELECT first_name, last_name, car_model, sale_amount,
       RANK() OVER (
           PARTITION BY car_model 
           ORDER BY sale_amount DESC
       ) AS rank
FROM sales_reps_data sr
JOIN toyota_sales_data ts ON sr.rep_id = ts.sale_rep_id
WHERE ts.sale_amount > 23000;
```
**Benefits:**
- Single-pass processing
- Efficient memory usage
- Better index utilization

## Window Functions vs. Self-Joins

### Self-Join (Inefficient)
```sql
SELECT a.*, 
       COUNT(b.sale_amount) as rank
FROM toyota_sales_data a
LEFT JOIN toyota_sales_data b 
    ON a.car_model = b.car_model 
    AND b.sale_amount >= a.sale_amount
GROUP BY a.sale_id, a.sale_amount;
```
**Issues:**
- Table scanned multiple times
- Large intermediate result sets
- Poor scalability

### Window Function (Efficient)
```sql
SELECT *,
       DENSE_RANK() OVER (
           PARTITION BY car_model 
           ORDER BY sale_amount DESC
       ) as rank
FROM toyota_sales_data;
```
**Benefits:**
- Single table scan
- No intermediate results
- Better performance

## Performance Optimization Techniques

### 1. Proper Indexing
```sql
-- Create index for common ranking patterns
CREATE INDEX idx_sales_model_amount 
ON toyota_sales_data (car_model, sale_amount DESC);
```

### 2. Materialized Views
```sql
CREATE MATERIALIZED VIEW sales_rankings AS
SELECT car_model, 
       sale_amount,
       RANK() OVER (
           PARTITION BY car_model 
           ORDER BY sale_amount DESC
       ) as rank
FROM toyota_sales_data;
```

### 3. Incremental Updates
```sql
-- Refresh materialized view concurrently
REFRESH MATERIALIZED VIEW CONCURRENTLY sales_rankings;
```

## Common Window Functions

1. **ROW_NUMBER()**
   - Unique ranking (1,2,3,4...)
   - No ties allowed

2. **RANK()**
   - Allows ties (1,1,3,4...)
   - Gaps after ties

3. **DENSE_RANK()**
   - Allows ties (1,1,2,3...)
   - No gaps

4. **NTILE()**
   - Divides results into N groups

## Best Practices

1. **Choose Appropriate Window Function**
   - ROW_NUMBER() for unique rankings
   - RANK() when ties should create gaps
   - DENSE_RANK() for continuous ranking

2. **Optimize Data Access**
   - Create proper indexes
   - Use materialized views for static data
   - Consider partitioning for large datasets

3. **Query Structure**
   - Filter data before ranking
   - Use PARTITION BY for grouped rankings
   - Avoid unnecessary self-joins

4. **Performance Monitoring**
   - Check execution plans
   - Monitor memory usage
   - Watch for spills to disk

## Common Anti-Patterns

1. **Unnecessary Subqueries**
   ```sql
   -- Avoid
   SELECT * FROM (
       SELECT *, ROW_NUMBER() OVER (...) as rn
       FROM large_table
   ) x WHERE rn <= 10;
   
   -- Better
   SELECT * FROM large_table
   ORDER BY column DESC
   LIMIT 10;
   ```

2. **Self-Joins for Rankings**
   ```sql
   -- Avoid
   SELECT a.*, COUNT(b.id) as rank
   FROM sales a
   LEFT JOIN sales b ON a.amount <= b.amount
   GROUP BY a.id;
   
   -- Better
   SELECT *,
       RANK() OVER (ORDER BY amount DESC) as rank
   FROM sales;
   ```

## Summary

Efficient ranking query optimization relies on:
- Proper use of window functions
- Appropriate indexing strategies
- Avoiding self-joins
- Using materialized views when applicable

Key Takeaways:
1. Use window functions instead of self-joins
2. Create appropriate indexes for ranking patterns
3. Filter data before applying rankings
4. Consider materialized views for static rankings
5. Monitor and optimize based on actual usage patterns
