---
theme: black
transition: slide
---

# Joins vs. Subqueries
### SQL Performance Tuning Scenario #5

---

### Performance Comparison

#### Subqueries
- Simpler to write and understand
- Can cause multiple lookups
- Often performs poorly on large datasets
- May not leverage indexes efficiently

#### Joins
- More efficient for large datasets
- Avoids redundant data scans
- Better utilizes indexes
- Allows complex relationships

---

### Example Scenario

#### Business Question
"Find all sales representatives who have completed at least one sale worth more than $30,000"

---

### Subquery Approach

```sql
EXPLAIN ANALYZE  
SELECT first_name, last_name  
FROM sales_reps  
WHERE rep_id IN (  
    SELECT sale_rep_id  
    FROM toyota_sales  
    WHERE sale_amount > 30000  
);
```

Issues:
- Inner query may run multiple times
- Performance degradation
- May not utilize indexes effectively

---

### Join Approach

```sql
EXPLAIN ANALYZE  
SELECT sr.first_name, sr.last_name  
FROM sales_reps sr  
INNER JOIN toyota_sales ts   
    ON sr.rep_id = ts.sale_rep_id  
WHERE ts.sale_amount > 30000;
```

Benefits:
- Single pass processing
- Better index utilization
- Works better for large datasets

---

### When to Use Each Approach

#### Use Joins When:
1. Combining data from multiple tables
2. Working with large datasets
3. Need to leverage indexes
4. Performance is critical

#### Use Subqueries When:
1. Logic is easier to express
2. Not possible to use Joins

---

### Optimizer Considerations

- Modern databases can convert subqueries to joins
- Don't rely on automatic transformations
- Explicit JOINs give better control
- Analyze execution plans

---

### Best Practices

#### Query Design
- Start with JOINs for multi-table queries
- Choose right join type
- Ensure indexes exist on join columns

#### Performance Testing
- Compare both approaches
- Use realistic data volumes
- Measure CPU, I/O, and execution time

---

### Common Anti-Patterns

#### Correlated Subqueries
```sql
SELECT first_name, last_name  
FROM sales_reps sr  
WHERE EXISTS (  
    SELECT 1  
    FROM toyota_sales ts  
    WHERE ts.sale_rep_id = sr.rep_id  
    AND ts.sale_amount > 30000  
);
```

Better Alternative: Convert to JOIN
```sql
SELECT DISTINCT sr.first_name, sr.last_name
FROM sales_reps sr
INNER JOIN toyota_sales ts 
    ON ts.sale_rep_id = sr.rep_id
WHERE ts.sale_amount > 30000;
```

---

### Multiple Nested Subqueries

```sql
SELECT first_name, last_name  
FROM sales_reps  
WHERE rep_id IN (  
    SELECT sale_rep_id FROM toyota_sales 
    WHERE sale_amount > (  
        SELECT AVG(sale_amount) FROM toyota_sales  
    )  
);
```

Better Alternative: Use JOINs and CTEs

```sql
WITH avg_sales AS (
    SELECT ts.*,
           AVG(sale_amount) OVER () as overall_avg
    FROM toyota_sales ts
)
SELECT DISTINCT sr.first_name, sr.last_name
FROM sales_reps sr
INNER JOIN avg_sales ts ON ts.sale_rep_id = sr.rep_id
WHERE ts.sale_amount > ts.overall_avg;
```

---

### Maintenance Best Practices

- Keep database statistics updated
- Periodically review and adjust indexes
- Monitor query performance over time
- Optimize when needed

---

### Summary

- JOINs generally perform better
- Subqueries can improve readability
- Analyze execution plans
- Test with representative data

---

### Thank You!

#### Next Up: Scenario #6
### Advanced Query Optimization Techniques

Stay tuned for more SQL performance tuning insights! 🚀 