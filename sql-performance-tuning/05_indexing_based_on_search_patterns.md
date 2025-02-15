# Scenario 3: Indexing Based on Search Patterns (SARGability)

## What is SARGability?

SARGable (Search ARGument able) refers to queries that can effectively use indexes. A query is SARGable when predicates in the WHERE clause can utilize indexes without transforming the indexed columns.

## Common Non-SARGable vs SARGable Patterns

### 1. String Comparisons

**Non-SARGable:**
```sql
SELECT *
FROM toyota_sales_data
WHERE LOWER(sale_status) = 'pending';
```
- Problem: Function `LOWER()` prevents index usage
- Forces full table scan

**SARGable:**
```sql
SELECT *
FROM toyota_sales_data
WHERE sale_status = 'Pending';
```
- Direct comparison allows index usage
- Better performance

### 2. Numeric Calculations

**Non-SARGable:**
```sql
SELECT *
FROM toyota_sales_data
WHERE (sale_amount * 1.05) > 40000;
```
- Problem: Calculation on column prevents index usage
- Requires evaluating every row

**SARGable:**
```sql
SELECT *
FROM toyota_sales_data
WHERE sale_amount > 40000 / 1.05;
```
- Moves calculation to the constant side
- Can use index on sale_amount

### 3. Pattern Matching (LIKE)

**Non-SARGable:**
```sql
SELECT sale_id, car_model, sale_amount
FROM toyota_sales_data
WHERE car_model LIKE '%Corolla%';
```
- Problem: Leading wildcard prevents efficient index usage
- Results in full index scan

**SARGable:**
```sql
SELECT sale_id, car_model, sale_amount
FROM toyota_sales_data
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
