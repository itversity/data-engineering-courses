# Views and Common Table Expressions in SQL

* Overview of Database Views
* Overview of Common Table Expressions or CTEs
* Outer Join with Additional Conditions in SQL Queries
* Explanation about Fix of SQL Queries with Filtering on Outer Join Results

## Overview of Database Views

As part of this lecture, we will get an overview of Database Views.
* Views are created for commonly used queries.
* Unlike Tables, data will not be stored in views.
* Views will be persisted in the database with the query logic used while creating it.

```sql
CREATE OR REPLACE VIEW order_details_v
AS
SELECT o.order_date,
    oi.order_item_product_id,
    oi.order_item_subtotal
FROM orders AS o
    JOIN order_items AS oi
        ON o.order_id = oi.order_item_order_id;
```

## Overview of Common Table Expressions or CTEs

As part of this lecture, we will go through the details related to CTEs which is known as Common Table Expressions.
* CTEs are similar to views, but CTEs will not be persisted in the database.
* If the session is closed, the CTEs will be flushed out.
* We need to recreate CTEs in new sessions to use them.
* CTEs are typically used to modularize large queries.

```sql
WITH order_details_cte AS
(SELECT o.order_date,
    oi.order_item_product_id,
    oi.order_item_subtotal
FROM orders AS o
    JOIN order_items AS oi
        ON o.order_id = oi.order_item_order_id)
SELECT * FROM order_details_cte;

WITH order_details_cte AS
(SELECT o.order_date,
    oi.order_item_product_id,
    oi.order_item_subtotal
FROM orders AS o
    JOIN order_items AS oi
        ON o.order_id = oi.order_item_order_id)
SELECT * FROM order_details_cte
WHERE order_id = 2;
```

## Outer Join with Additional Conditions in SQL Queries

As part of this lecture we will see how we add additional conditions related to outer joins.

```sql
SELECT * FROM order_details_v;

SELECT * FROM products;

SELECT * 
FROM products AS p
    LEFT OUTER JOIN order_details_v AS odv
        ON p.product_id = odv.order_item_product_id
WHERE odv.order_item_product_id IS NULL;

SELECT * 
FROM products AS p
    LEFT OUTER JOIN order_details_v AS odv
        ON p.product_id = odv.order_item_product_id
WHERE to_char(odv.order_date::timestamp, 'yyyy-MM') = '2004-01';

-- Query with bug
-- It doesn't return any thing
SELECT * 
FROM products AS p
    LEFT OUTER JOIN order_details_v AS odv
        ON p.product_id = odv.order_item_product_id
WHERE to_char(odv.order_date::timestamp, 'yyyy-MM') = '2004-01'
    AND odv.order_item_product_id IS NULL;

SELECT * FROM products AS p
WHERE NOT EXISTS (
    SELECT 1 FROM order_details_v AS odv
    WHERE p.product_id = odv.order_item_product_id
        to_char(odv.order_date::timestamp, 'yyyy-MM') = '2004-01'
);

-- The join conditions should be updated with the condition against month.
SELECT * 
FROM products AS p
    LEFT OUTER JOIN order_details_v AS odv
        ON p.product_id = odv.order_item_product_id
            AND to_char(odv.order_date::timestamp, 'yyyy-MM') = '2004-01'
WHERE odv.order_item_product_id IS NULL;
```

## Explanation about Fix of SQL Queries with Filtering on Outer Join Results

We are performing left outer join not just on the common field but also using additional condition to compare order month with a given month.