---
theme: black
transition: slide
---

# Indexing Foreign Key Fields
### SQL Performance Tuning Scenario #2

---

### Why Index Foreign Key Columns?

- Faster JOIN Operations
- Improved Concurrency
- Reduced Locking
- Consistent Query Performance

---

### Example Use Case

#### Tables Structure
- `orders` (child table)
- `customers` (parent table)
- Foreign Key: `orders.customer_id → customers.customer_id`

---

### Query Without Index

```sql
DROP INDEX idx_orders_customer

EXPLAIN ANALYZE
SELECT c.customer_id, c.first_name, c.last_name, 
       o.order_id, o.order_date, o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id = 1;
```

Output:
```
Seq Scan on orders  (cost=0.00..50.00 rows=1000 width=48)
Filter: (customer_id = 1)
```

---

### Adding the Index

```sql
CREATE INDEX idx_orders_customer ON orders(customer_id);
```

---

### Query With Index

```sql
EXPLAIN ANALYZE
SELECT c.customer_id, c.first_name, c.last_name, 
       o.order_id, o.order_date, o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id = 1;
```

Output:
```
Nested Loop  (cost=0.29..12.45 rows=50 width=48)
Index Scan using idx_orders_customer on orders
```

---

### Best Practices

1. Always Index the Referencing Column
2. Balance Read vs. Write Costs
3. Monitor FK-Related Queries
4. Check for Potential Locking
5. Follow Naming Conventions

---

### Common Pitfalls

- Assuming Parent PK Index is Enough
- Over-Indexing
- Ignoring SARGability
- Non-SARGable Conditions

---

### Non-SARGable Example

```sql
-- Bad: Index cannot be used efficiently
WHERE UPPER(customer_id) = '123'

-- Good: Index can be used
WHERE customer_id = 123
```

---

### Database-Specific Considerations

#### MySQL (InnoDB)
- Missing FK indexes can cause full table scans
- Affects referential integrity validation

#### Oracle
- Recommends indexing FKs
- Prevents "lock escalation"

---

### Index Naming Convention

```sql
-- Good naming convention
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_customer_fk ON orders(customer_id);
```

---

### Performance Impact

#### Benefits
- Faster lookups
- Reduced locking
- Consistent performance

#### Trade-offs
- Slight write overhead
- Additional storage space

---

### Summary

- Indexing FKs is crucial for performance
- Consider both read and write patterns
- Monitor and maintain indexes
- Follow best practices

---

### Thank You!

#### Next Up: Scenario #3
### Indexing Based on Search Patterns (SARGability)

Stay tuned for more SQL performance tuning insights! 🚀 