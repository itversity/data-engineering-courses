---
theme: black
transition: slide
---

# Optimizing Ranking Queries
### SQL Performance Tuning Scenario #8

---

### Common Ranking Scenarios

#### Top-N Queries
```sql
-- Inefficient Approach
SELECT *
FROM (
    SELECT *, 
           ROW_NUMBER() OVER (ORDER BY sale_amount DESC) AS row_num
    FROM toyota_sales
) sub
WHERE row_num <= 5;

-- Optimized Approach
SELECT *
FROM toyota_sales
ORDER BY sale_amount DESC
LIMIT 5;
```

---

### Partitioned Rankings

```sql
-- Inefficient Approach
SELECT t1.*, 
       (SELECT COUNT(*) 
        FROM toyota_sales t2 
        WHERE t2.car_model = t1.car_model 
          AND t2.sale_amount >= t1.sale_amount) as rank
FROM toyota_sales t1;

-- Optimized Approach
SELECT first_name, last_name, car_model, sale_amount,
       RANK() OVER (
           PARTITION BY car_model 
           ORDER BY sale_amount DESC
       ) AS rank
FROM toyota_sales_reps sr
JOIN toyota_sales ts ON sr.rep_id = ts.sale_rep_id
WHERE ts.sale_amount > 23000;
```

---

### Window Functions vs Self-Joins

#### Self-Join (Inefficient)
```sql
SELECT a.*, 
       COUNT(b.sale_amount) as rank
FROM toyota_sales a
LEFT JOIN toyota_sales b 
    ON a.car_model = b.car_model 
    AND b.sale_amount >= a.sale_amount
GROUP BY a.sale_id, a.sale_amount;
```

#### Window Function (Efficient)
```sql
SELECT *,
       DENSE_RANK() OVER (
           PARTITION BY car_model 
           ORDER BY sale_amount DESC
       ) as rank
FROM toyota_sales;
```

---

### Performance Optimization Techniques

#### Proper Indexing
```sql
-- Create index for common ranking patterns
CREATE INDEX idx_sales_model_amount 
ON toyota_sales (car_model, sale_amount DESC);
```

#### Materialized Views
```sql
CREATE MATERIALIZED VIEW sales_rankings AS
SELECT car_model, 
       sale_amount,
       RANK() OVER (
           PARTITION BY car_model 
           ORDER BY sale_amount DESC
       ) as rank
FROM toyota_sales;
```

---

### Incremental Updates

```sql
-- Refresh materialized view concurrently
REFRESH MATERIALIZED VIEW CONCURRENTLY sales_rankings;
```

---

### Common Window Functions

#### ROW_NUMBER()
- Assigns unique rank to each row
- No concept of ties

#### RANK()
- Permits ties
- Leaves gaps in ranking

#### DENSE_RANK()
- Permits ties
- No gaps in ranking

#### NTILE()
- Divides rows into N equal groups

---

### Best Practices

#### Choose Appropriate Window Function
- ROW_NUMBER(): For unique positions
- RANK(): When ties should reflect skipped ranks
- DENSE_RANK(): When ties should not skip ranks

#### Optimize Data Access
- Use indices matching ORDER BY and PARTITION BY
- Consider materialized views for semi-static data
- Partition large tables

---

### Query Structure Best Practices

- Filter first, rank second
- Use PARTITION BY for group rankings
- Avoid unnecessary self-joins
- Leverage window functions

---

### Performance Monitoring

```sql
-- Check execution plans
EXPLAIN SELECT * FROM toyota_sales
ORDER BY sale_amount DESC
LIMIT 5;

-- Monitor memory usage
SELECT * FROM pg_stat_activity 
WHERE query LIKE '%ORDER BY%';
```

---

### Common Anti-Patterns

#### Unnecessary Subqueries
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

---

### Summary

#### Key Requirements
1. Use window functions instead of self-joins
2. Create appropriate indexes
3. Filter data before ranking
4. Consider materialized views
5. Monitor and optimize continuously

---

### Key Takeaways

- Window functions are more efficient
- Proper indexing is crucial
- Filter before ranking
- Use materialized views for static data
- Monitor performance regularly

---

### Thank You!

#### Next Up: Scenario #9
### Bulk Loading Strategies

Stay tuned for more SQL performance tuning insights! 🚀 