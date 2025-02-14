# Joining Tables using SQL

* Inner Joins using SQL Queries
* Outer Joins using SQL Queries
* Filter and Aggregate on Join Results using SQL

## Inner Joins using SQL Queries

As part of this lecture, we will go through the inner joins using SQL Queries.

```sql
Below are the code scripts for the "Inner Joins using SQL Queries".

-- INNER JOIN - Get all the records from both orders and order_items which satisfies JOIN condition.

SELECT o.order_date,
    oi.order_item_product_id,
    oi.order_item_subtotal
FROM orders AS o
    JOIN order_items AS oi
        ON o.order_id = oi.order_item_order_id;
```

## Outer Joins using SQL Queries

```sql
SELECT o.order_id, 
    o.order_date,
    oi.order_item_id ,
    oi.order_item_product_id,
    oi.order_item_subtotal
FROM orders AS o
    LEFT OUTER JOIN order_items AS oi
        ON o.order_id = oi.order_item_order_id
ORDER BY 1;
```

## Filter and Aggregate on Join Results using SQL

```sql
SELECT o.order_date,
    oi.order_item_product_id,
    round(sum(oi.order_item_subtotal)::numeric, 2) AS order_revenue
FROM orders AS o
JOIN order_items AS oi
    ON o.order_id = oi.order_item_order_id
WHERE o.order_status IN ('COMPLETE', 'CLOSED')
GROUP BY 1, 2
ORDER BY 1, 3 DESC;
```