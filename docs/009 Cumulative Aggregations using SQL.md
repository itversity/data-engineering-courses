# Cumulative Aggregations using SQL

* Introduction to Cumulative Aggregations and Ranking in SQL Queries
* Overview of CTAS to create tables based on Query Results
* Create Tables for Cumulative Aggregations and Ranking
* Overview of OVER and PARTITION BY Clause in SQL Queries
* Compute Total Aggregation using OVER and PARTITION BY in SQL Queries

## Introduction to Cumulative Aggregations and Ranking in SQL Queries

Cumulative Aggregations and Ranking can be taken care using advanced SQL Functions. These are also known as Windowing Functions or Analytical Functions.

## Overview of CTAS to create tables based on Query Results

As part of this lecture, we will go through the details related to CTAS (`CREATE TABLE AS SELECT`) to create tables based on Query Results.

1. We need to come up with query based on the requirement.
2. Once the results are reviewed, we can use CTAS to create tables based on results.
3. Column Names and Data Types for the columns will automatically be inherited based on query results.

```sql
CREATE TABLE order_count_by_status
AS
SELECT order_status, count(*) AS order_count
FROM orders
GROUP BY 1;

SELECT * FROM order_count_by_status;

CREATE TABLE orders_stg
AS
SELECT * FROM orders WHERE false;

SELECT * FROM orders_stg;
```

To develop queries for cumulative aggregations and ranking we might end up creating intermediate tables using CTAS. Intermediate table will help us in both modularizing large query as well as improving the performance of such queries.

## Create Tables for Cumulative Aggregations and Ranking

As part of this lecture, we will go through the details about creating tables for cumulative aggregations and ranking using CTAS.
* We will be creating `daily_revenue` and `daily_product_revenue` tables.

```sql
CREATE TABLE daily_revenue
AS
SELECT o.order_date,
    round(sum(oi.order_item_subtotal)::numeric, 2) AS order_revenue
FROM orders AS o
    JOIN order_items AS oi
        ON o.order_id = oi.order_item_order_id
WHERE o.order_status IN ('COMPLETE', 'CLOSED')
GROUP BY 1;

SELECT * FROM daily_revenue
ORDER BY order_date;

CREATE TABLE daily_product_revenue
AS
SELECT o.order_date,
    oi.order_item_product_id,
    round(sum(oi.order_item_subtotal)::numeric, 2) AS order_revenue
FROM orders AS o
    JOIN order_items AS oi
        ON o.order_id = oi.order_item_order_id
WHERE o.order_status IN ('COMPLETE', 'CLOSED')
GROUP BY 1,2;

SELECT * FROM daily_product_revenue
ORDER BY 1, 3 DESC;
```

The intermediate tables created will then be used for writing queries for cumulative aggregations as well as ranking.

## Overview of OVER and PARTITION BY Clause in SQL Queries

As part of this lecture, we will go through the additional clauses such as `OVER` and `PARTITION BY`.
* `OVER` is mandatory to use `PARTITION BY`.
* Under `PARTITION BY`, we specify the grouping key.
* `OVER` is typically followed by aggregate functions such as `sum`.

```sql
SELECT to_char(dr.order_date::timestamp, 'yyyy-MM') AS order_month,
    dr.order_date,
    dr.order_revenue,
    sum(order_revenue) OVER (
            PARTITION BY to_char(dr.order_date::timestamp, 'yyyy-MM')
    ) AS monthly_order_revenue
FROM daily_revenue AS dr
ORDER BY 2;
```

## Compute Total Aggregation using OVER and PARTITION BY in SQL Queries

As part of this lecture, we will see how to compute total aggregation leveraging sum followed by `OVER` and then `PARTITION BY`.

```sql
SELECT dr.*,
    sum(order_revenue) OVER (PARTITION BY 1) AS total_order_revenue
FROM daily_revenue AS dr
ORDER BY 1;
```