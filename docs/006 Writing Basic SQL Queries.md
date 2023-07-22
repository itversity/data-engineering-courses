# Writing Basic SQL Queries

* Review Data Model Diagram
* Define Problem Statement for SQL Queries
* Filtering Data using SQL Queries
* Total Aggregations using SQL Queries
* Group By Aggregations using SQL Queries
* Order of Execution of SQL Queries
* Rules and Restrictions to Group and Filter Data in SQL queries
* Filter Data based on Aggregated Results using Group By and Having

## Review Data Model Diagram

Here are the details related to Retail DB Data Model. We have 6 tables in retail_db database.
* `departments`
* `categories` - Child table to `departments`.
* `products` - Child table to `categories`.
* `orders` - Child table to `customers`.
* `order_items` - Child table to both `products` and `orders`.
* `customers`

## Define Problem Statement for SQL Queries

Here are the details related to problem statement to review basic SQL Queries.
* Compute Daily Product Revenue considering only `COMPLETE` or `CLOSED` orders.
* The problem statement covers filtering, joins, aggregations as well as sorting.

## Filtering Data using SQL Queries

As part of this lecture we will see how to Filter the Data using SQL. Here are some of the examples related to filtering data using SQL.

```sql
-- Taking distinct order status from order table and ordered by first column

SELECT DISTINCT order_status FROM orders
ORDER BY 1;

-- Filter orders which are in COMPLETE status

SELECT * FROM orders
WHERE order_status = 'COMPLETE';

-- Filter orders which iares in CLOSED status
 
SELECT * FROM orders
WHERE order_status = 'CLOSED';

-- Filter orders which are in CLOSED or COMPLETE status

SELECT * FROM orders
WHERE order_status = 'CLOSED' OR order_status = 'COMPLETE';

-- Filter the orders which are in CLOSED or COMPLETE status by using IN operator

SELECT * FROM orders
WHERE order_status IN ('CLOSED', 'COMPLETE');
```

## Total Aggregations using SQL Queries

As part of this lecture, you will see how to get total aggregations using SQL Queries. We use functions such as `count`, `sum`, `min`, `max`, etc for total aggregations.

```sql
-- Get total number of orders

SELECT count(*) FROM orders;

-- Get total number of order items

SELECT count(*) FROM order_items;

-- Get total number of distinct order statuses from orders table

SELECT count(DISTINCT order_status) FROM  orders;

-- Get total number of distinct order dates from orders table

SELECT count(DISTINCT order_date) FROM orders;

-- Get all rows using all columns from order items table

SELECT * FROM order_items; 

-- Get sum of order item subtotal for a given order id

SELECT sum(order_item_subtotal) 
FROM order_items
WHERE order_item_order_id = 2;
```

## Group By Aggregations using SQL Queries

As part of this lecture, we will understand how to write SQL Queries to perform aggregations based on a key using `GROUP BY`.

```sql
SELECT * FROM orders;

-- Get the count for each order status and count should be in descending order

SELECT order_status, count(*) AS order_count
FROM orders
GROUP BY 1
ORDER BY 2 DESC;

-- Get the count for each order date and count should be in descending order

SELECT order_date, count(*) AS order_count
FROM orders
GROUP BY 1
ORDER BY 2 DESC;

-- Get the count for each order month (derived column) and count should be in descending order

SELECT to_char(order_date, 'yyyy-MM') AS order_month, count(*) AS order_count
FROM orders
GROUP BY 1
ORDER BY 2 DESC;

-- Get all the columns in order items table

SELECT * FROM order_items;

-- Get the order revenue for each order id

SELECT order_item_order_id, 
round(sum(order_item_subtotal)::numeric, 2) AS order_revenue
FROM order_items
GROUP BY 1
ORDER BY 1;
```

## Order of Execution of SQL Queries

As part of this lecture, we will go through the details about order of execution of SQL Queries. The order in which the queries are executed is different from the order in which SQL Queries are written.
* Order in which SQL Queries are written
  * SELECT
  * FROM (Optionally JOIN)
  * WHERE
  * GROUP BY (Optionally HAVING)
  * ORDER BY
* Order in which SQL Queries are executed
  * FROM
  * WHERE
  * GROUP BY (followed by HAVING, if used)
  * SELECT
  * ORDER BY

## Rules and Restrictions to Group and Filter Data in SQL queries

As part of this lecture, we will review the rules and restrictions to group and filter data in SQL Queries.
* `SELECT` clause should have only those columns that are specified in GROUP BY and derived columns using aggregate functions such as `sum`, `count`, etc.
* The aliases used for derived columns using aggregate functions in `SELECT` clause, cannot be used in `WHERE` clause.

## Filter Data based on Aggregated Results using Group By and Having

As part of this lecture, we will go through the details about filtering data based on aggregate results using `GROUP BY` and `HAVING`.
* We need to use `HAVING` to filter the data based on aggregate results.

```sql
-- Get the order count by date where the order count by date is greater than 120.
-- We will consider only those orders which are either in COMPLETE or CLOSED status.
-- Data will be sorted in descending order by the count

SELECT order_date, count(*) AS order_count
FROM orders
WHERE order_status IN ('COMPLETE', 'CLOSED')
GROUP BY 1
HAVING count(*) >= 120
ORDER BY 2 DESC;

-- Typical query execution

-- FROM
-- WHERE
-- GROUP BY
-- SELECT
-- ORDER BY

-- Get the order ids which have order revenue more than or equal to 2000

SELECT order_item_order_id,
round(sum(order_item_subtotal)::numeric, 2) AS order_revenue
FROM order_items
GROUP BY 1
HAVING round(sum(order_item_subtotal)::numeric, 2) >= 2000
ORDER BY 2 DESC;
```