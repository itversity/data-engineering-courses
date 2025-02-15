# Scenario 2: Indexing Foreign Key Fields

## 2.1 Why Index Foreign Key Columns?

A foreign key (FK) enforces a relationship between two tables — usually a child table referencing a primary key or unique key in a parent table. When queries frequently join these two tables (or filter on the foreign key column in the child table), indexing that FK column can offer several benefits:

### a. Faster JOIN Operations
- If your application regularly joins a child table (containing the FK) to its parent table, an index on the FK column allows quick lookups and avoids scanning the entire child table.

### b. Improved Concurrency & Reduced Locking
- In high-write environments (e.g., many INSERTs/UPDATEs on the child table), some RDBMS engines (like InnoDB in MySQL or Oracle) can escalate locks or check parent-child referential constraints in ways that benefit from an indexed FK.
- Without an index, certain delete or update operations on the parent table may cause more extensive locking or scanning of the child table to validate constraints.

### c. Query Performance Consistency
- Over time, as data grows, a missing index on a foreign key column can lead to increasingly slow queries.
- Indexing ensures more stable performance despite larger data volumes.

## 2.2 Example Use Case

Imagine you have two tables, orders (child) and customers (parent):

Foreign Key: `orders.customer_id → customers.customer_id`

#### Drop the index
```sql
DROP INDEX idx_orders_customer ON orders;
```

#### Validate the query plan
This query will perform a sequential scan on the orders table as there is no index on the customer_id column (in orders table).

```sql
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, o.order_date, o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id = 1;

EXPLAIN ANALYZE
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, o.order_date, o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id = 1;
```

If queries often look like this, then adding an index on `orders(customer_id)` helps the optimizer quickly locate rows when joining or filtering by customer_id.

Adding an index on `orders(customer_id)` helps the optimizer quickly locate rows when joining or filtering by customer_id.

Additionally, if your application frequently deletes customers, an indexed FK in orders can reduce scanning overhead and locking when checking for referencing rows.

#### Add the index
```sql
CREATE INDEX idx_orders_customer ON orders(customer_id);
```

#### Validate the query plan
This query will perform a nested loop join on the orders and customers tables as there is an index on the customer_id column (in orders table).

```sql
EXPLAIN ANALYZE
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, o.order_date, o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id = 1;
```

## 2.3 Best Practices & Considerations

1. **Always Index the Referencing Column**
   - The child table's FK column (`orders.customer_id` in the example) is typically the most critical to index
   - Especially important when used in frequent joins or filters

2. **Balance Read vs. Write Costs**
   - Each new index slightly slows down INSERT, UPDATE, and DELETE operations
   - FKs are typically among the most frequently queried relationships
   - Performance gains often outweigh the write overhead

3. **Monitor FK-Related Queries**
   - Use execution plans to confirm that your FK index is actually used
   - Watch for non-SARGable queries that might prevent index usage

4. **Check for Potential Locking**
   - MySQL (InnoDB): Missing FK index can cause table scans during referential integrity validation
   - Oracle: Recommends indexing FKs to avoid "lock escalation" on child tables

5. **Naming Conventions**
   - Consider naming indexes to match constraint names (e.g., `idx_orders_customer_id`)
   - Helps with maintenance and clarity

## 2.4 Common Pitfalls

1. **Assuming a Parent PK Index is Enough**
   - Parent table's primary key index isn't sufficient
   - Need matching index on child table's foreign key column

2. **Over-Indexing**
   - Be mindful of overall index count
   - Too many indexes can hurt write performance
   - Redundant indexes complicate maintenance

3. **Ignoring SARGability**
   - Even with FK index, non-SARGable predicates prevent effective index usage
   - Example: `WHERE UPPER(customer_id) = '123'`

## 2.5 Recap

Indexing Foreign Key fields is a critical piece of relational design, especially when queries frequently join or filter by those fields:

- Benefits include:
  - Speedier lookups
  - Reduced locking
  - More consistent performance as data grows

- Always weigh the impact:
  - Consider DML operations (write overhead)
  - Balance against read performance gains
  - In most real-world scenarios, indexing FKs remains a best practice

**Takeaway**: Properly indexed foreign keys ensure that referential integrity checks and JOIN operations run smoothly, preventing bottlenecks in high-concurrency applications and large data sets. This scenario exemplifies a universal SQL optimization principle across all major database platforms.



