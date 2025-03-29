# SQL Performance Tuning Scenario #2: Indexing Foreign Key Fields

## Introduction
Boost query efficiency and minimize locking by properly indexing foreign key (FK) fields. This guide explains why indexing FKs is essential, how to validate query plans, and best practices for maintaining indexed foreign keys in SQL.

## Why Index Foreign Key Columns?
Foreign keys enforce relationships between tables (typically a child table referencing a parent table). Indexing the FK column improves performance in the following ways:

### 1. Faster JOIN Operations
- If queries frequently join a child table (FK) to a parent table, an index on the FK column speeds up lookups and avoids full table scans.

### 2. Improved Concurrency & Reduced Locking
- In high-write environments (e.g., frequent INSERTs/UPDATEs), some RDBMS engines escalate locks or validate constraints more efficiently with indexed FKs.
- Without an index, DELETE or UPDATE operations on the parent table may cause extensive locking or scanning of the child table.

### 3. Query Performance Consistency
- As data grows, missing FK indexes lead to slower queries.
- Indexing ensures stable query performance over time.

## Example Use Case
Consider two tables: `orders` (child) and `customers` (parent)

**Foreign Key:** `orders.customer_id → customers.customer_id`

### Query Without an Index
```sql
DROP INDEX idx_orders_customer

EXPLAIN ANALYZE
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, o.order_date, o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id = 1;
```
#### Potential Output:
```
Seq Scan on orders  (cost=0.00..50.00 rows=1000 width=48)
Filter: (customer_id = 1)
```
- A **sequential scan** occurs because there is no index on `orders.customer_id`.

### Adding an Index on `orders.customer_id`
```sql
CREATE INDEX idx_orders_customer ON orders(customer_id);
```

### Query With Index
```sql
EXPLAIN ANALYZE
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, o.order_date, o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id = 1;
```
#### Potential Output:
```
Nested Loop  (cost=0.29..12.45 rows=50 width=48)
Index Scan using idx_orders_customer on orders (cost=0.28..8.29 rows=1 width=22)
```
- **Index scan is used**, leading to **better performance**.

## Best Practices & Considerations
### 1. Always Index the Referencing Column
- The child table’s FK column (e.g., `orders.customer_id`) should be indexed.
- Critical when used frequently in `JOIN` or `WHERE` clauses.

### 2. Balance Read vs. Write Costs
- Every new index slightly slows down `INSERT`, `UPDATE`, and `DELETE` operations.
- Since FKs are often queried, the performance gains usually outweigh the write overhead.

### 3. Monitor FK-Related Queries
- Use execution plans to verify index utilization.
- Ensure queries are **SARGable** (Search ARGument Able) so that indexes are effectively used.

### 4. Check for Potential Locking
- **MySQL (InnoDB)**: Missing FK indexes can cause full table scans during referential integrity validation.
- **Oracle**: Recommends indexing FKs to prevent "lock escalation" on child tables.

### 5. Naming Conventions for Indexes
- Consider naming indexes to match constraint names (e.g., `idx_orders_customer_id`).
- Improves clarity and maintainability.

## Common Pitfalls
### 1. Assuming a Parent PK Index is Enough
- Indexing the **parent table’s PK** isn’t sufficient.
- The **child table’s FK column** also requires an index.

### 2. Over-Indexing
- Too many indexes slow down writes (`INSERT/UPDATE/DELETE`).
- Avoid redundant indexes.

### 3. Ignoring SARGability
- Even with an FK index, non-SARGable conditions prevent efficient index usage.
- Example of a non-SARGable query:
  ```sql
  WHERE UPPER(customer_id) = '123'
  ```
  - This prevents the index from being used efficiently.

## Recap
Indexing foreign key fields is a key performance optimization in relational databases:

- **Benefits**:
  - Faster lookups
  - Reduced locking
  - More consistent performance as data grows
- **Trade-offs**:
  - Consider the write overhead vs. read performance gains
- **Best practice**:
  - Always index FKs when frequent joins or filters involve the column

## Looking Ahead
Now that we've improved join performance and reduced locking with well-indexed FKs, the next scenario in our **SQL Performance Tuning series** will cover **Indexing Based on Search Patterns (SARGability)**. Learn how query structure impacts index usage and how to write efficient queries!

Stay tuned! 🚀
