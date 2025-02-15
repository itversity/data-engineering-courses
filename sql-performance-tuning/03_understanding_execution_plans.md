# Scenario 1: Understanding Execution Plans

## 1.1 What Is an Execution Plan?

An execution plan (sometimes called a query plan) shows how the database engine will (or did) execute your SQL query. It breaks down the steps involved in retrieving data — such as which indexes are used, how tables are joined, whether data is sorted, and more.

Each RDBMS has its own method for displaying these plans:
- **SQL Server**: Graphical plans in SQL Server Management Studio (SSMS) or text-based via `SET SHOWPLAN_TEXT` or `SET STATISTICS PROFILE`
- **MySQL**: The `EXPLAIN` statement shows how tables are accessed (e.g., type of access, possible and chosen indexes)
- **PostgreSQL**: `EXPLAIN` or `EXPLAIN ANALYZE` gives a text-based or JSON-based plan, including row estimates, actual rows processed, and timing
- **Oracle**: The `EXPLAIN PLAN` command and tools like `DBMS_XPLAN.DISPLAY` show the plan operations

## 1.2 Why Execution Plans Matter

1. **Identify Bottlenecks**: 
   - Plans reveal if your query is performing full table scans on large datasets when an index seek would be more efficient

2. **Spot Missing or Ineffective Indexes**: 
   - If no appropriate index is found, or if the optimizer chooses a suboptimal plan, you'll see it reflected here

3. **Estimate vs. Actual**: 
   - Some databases (like PostgreSQL's `EXPLAIN ANALYZE`) compare expected row counts to actual rows retrieved
   - Crucial for diagnosing inaccurate statistics or skewed data distributions

4. **Join Methods**: 
   - You can see if the engine used a nested loop, hash join, or merge join
   - Helps optimize large or multi-table queries

## 1.3 How to Generate & Interpret Plans (Multi-Platform)

### SQL Server
```sql
-- In SSMS, right-click and select "Include Actual Execution Plan"
-- Key Icons: Look for "Clustered Index Seek" vs. "Clustered Index Scan," "Hash Match," "Merge Join"
```

### MySQL
```sql
EXPLAIN SELECT ...;
-- type=ALL usually indicates a full table scan
-- key=NULL might indicate no index is used
```

### PostgreSQL
```sql
-- For estimated row counts:
EXPLAIN SELECT ...;

-- For actual row counts and timing:
EXPLAIN ANALYZE SELECT ...;

-- Key Lines: "Seq Scan", "Index Scan", "Bitmap Heap Scan"
```

### Oracle
```sql
EXPLAIN PLAN FOR SELECT ...;
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
-- Key Operations: TABLE ACCESS (FULL), INDEX RANGE SCAN, NESTED LOOPS, HASH JOIN
```

## 1.4 Common Red Flags & What They Mean

1. **Full Table Scans on Large Tables**
   - Indicates missing vital index
   - May suggest non-SARGable filters

2. **High Estimated vs. Actual Rows**
   - Statistics may be out of date or incorrect
   - Can lead to poor plan choices
   - Example: Estimated 1,000 rows but processed 1,000,000

3. **Nested Loops on Large Joins**
   - Optimal for small sets
   - Can degrade with large data
   - Consider hash join or merge join for massive result sets

4. **No Index Usage**
   - Check for proper indexes on WHERE/JOIN clauses
   - Verify columns aren't wrapped in functions (non-SARGable)

## 1.5 Practical Example

### Scenario 1: No Index Usage
```sql
EXPLAIN ANALYZE
SELECT customer_id, first_name, last_name, segment
FROM customers
WHERE segment = 'Consumer';

-- Possible Plan Output:
--  Seq Scan on customers  (cost=0.00..27.50 rows=250 width=33) (actual time=0.012..0.196 rows=250 loops=1)
--    Filter: ((segment)::text = 'Consumer'::text)
--    Rows Removed by Filter: 750
--  Planning Time: 0.283 ms
```
This is a simple query that is performing a sequential scan on the customers table and filtering the rows based on the segment column. Since there is no index on the segment column, the query is performing a full table scan.

### Scenario 2: Index Usage
```sql
EXPLAIN ANALYZE
SELECT c.customer_id, c.first_name, c.last_name, o.order_date, o.total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.segment = 'Consumer'
AND o.order_date > '2025-01-01';

-- Possible Plan Output:
-- Nested Loop  (cost=0.56..16.66 rows=1 width=36) (actual time=0.005..
-- 0.006 rows=0 loops=1)
--    ->  Index Scan using idx_orders_date on orders o  (cost=0.29..8.30
--  rows=1 width=18) (actual time=0.004..0.005 rows=0 loops=1)
--          Index Cond: (order_date > '2025-01-01 00:00:00'::timestamp without time zone)
--    ->  Index Scan using customers_pkey on customers c  (cost=0.28..8.29 rows=1 width=22) (never executed)
--          Index Cond: (customer_id = o.customer_id)
--          Filter: ((segment)::text = 'Consumer'::text)

```
This query is performing a nested loop join on the customers and orders tables. The orders table uses an index on the order_date column and the customers table uses a sequential scan.

Key Observations:
- Orders table uses index on order_date
- Customers table uses sequential scan
- Potential optimization: Add index on `segment` column of customers table if selective enough
- However, if the segment column is dense and not frequently used in WHERE clause, it may not be beneficial to add an index on it. It might end up being a waste of space and time and also impact the performance of the insert operations.

## 1.6 Tips for Getting the Most Out of Execution Plans

1. **Keep Statistics Updated**
   - PostgreSQL/MySQL: `ANALYZE`
   - SQL Server: `UPDATE STATISTICS`
   - Oracle: `DBMS_STATS.GATHER_TABLE_STATS`

2. **Test Queries on Realistic Data**
   - Plans can differ between dev/test and production data

3. **Compare Query Variations**
   - Test different structures (subquery vs. join)
   - Try predicate reordering

4. **Monitor Over Time**
   - Track plan changes as data grows
   - Use tools like SQL Server's Query Store or PostgreSQL's pg_stat_statements

## 1.7 Summary

Execution plans serve as your "MRI scan" for SQL queries: they show exactly where the database engine invests time and resources. By interpreting them, you can:
- Spot missing indexes
- Identify inefficient join methods
- Detect poor cardinality estimates
- Optimize query performance

The concepts learned are universal across major RDBMS platforms, making execution plan analysis a fundamental skill in SQL Performance Tuning.



