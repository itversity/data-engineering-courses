---
theme: black
transition: slide
---

# Understanding Execution Plans
### SQL Performance Tuning Scenario #1

---

### What Is an Execution Plan?

- Shows how database engine executes SQL queries
- Details steps like:
  - Index usage
  - Table joins
  - Sorting operations

---

### Execution Plans by RDBMS

- **SQL Server**: Graphical plans in SSMS
- **MySQL**: `EXPLAIN` statement
- **PostgreSQL**: `EXPLAIN` / `EXPLAIN ANALYZE`
- **Oracle**: `EXPLAIN PLAN`

---

### Why Execution Plans Matter?

- Identify Bottlenecks
- Spot Missing/Ineffective Indexes
- Compare Estimated vs. Actual Rows
- Understand Join Methods

---

### Generating Execution Plans

#### SQL Server
```sql
SET SHOWPLAN_TEXT ON;
SELECT * FROM customers 
WHERE segment = 'Consumer';
```

#### PostgreSQL
```sql
EXPLAIN ANALYZE 
SELECT * FROM customers 
WHERE segment = 'Consumer';
```

---

### More Examples

#### MySQL
```sql
EXPLAIN SELECT * 
FROM customers 
WHERE segment = 'Consumer';
```

#### Oracle
```sql
EXPLAIN PLAN FOR 
SELECT * FROM customers 
WHERE segment = 'Consumer';
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```

---

### Common Red Flags

- Full Table Scans on Large Tables
- High Estimated vs. Actual Rows
- Nested Loops on Large Joins
- No Index Usage
- Functions Wrapping Indexed Columns

---

### Practical Example: No Index

```sql
EXPLAIN ANALYZE
SELECT customer_id, first_name, last_name, segment
FROM customers
WHERE segment = 'Consumer';
```

Output:
```
Seq Scan on customers
(cost=0.00..27.50 rows=250 width=33)
```

---

### Practical Example: With Index

```sql
EXPLAIN ANALYZE
SELECT c.customer_id, c.first_name, 
       o.order_date, o.total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date > '2025-01-01';
```

---

### Tips for Analysis

- Keep Statistics Updated
- Test with Realistic Data
- Compare Query Variations
- Monitor Plans Over Time

---

### Maintaining Statistics

#### By Database
- PostgreSQL/MySQL: `ANALYZE`
- SQL Server: `UPDATE STATISTICS`
- Oracle: `DBMS_STATS.GATHER_TABLE_STATS`

---

### Best Practices

- Track plan changes as data grows
- Use monitoring tools:
  - SQL Server Query Store
  - PostgreSQL's `pg_stat_statements`
- Test different query structures

---

### Summary

- Execution plans are essential diagnostic tools
- Help identify:
  - Missing indexes
  - Inefficient joins
  - Poor query plans
- Regular monitoring is key

---

### Thank You!

#### Next Up: Scenario #2
### Indexing Foreign Key Fields

Stay tuned for more SQL performance tuning insights! 