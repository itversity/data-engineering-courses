# Ranking using SQL Queries

* Overview of Ranking in SQL
* Compute Global Ranks using SQL
* Compute Ranks based on key using SQL
* Rules and Restrictions to Filter Data based on Ranks in SQL
* Filtering based on Global Ranks using Nested Queries and CTEs in SQL
* Filtering based on Ranks per Partition using Nested Queries and CTEs in SQL
* Create Students table with Data for ranking using SQL
* Difference between rank and dense rank using SQL

## Overview of Ranking in SQL

As part of this lecture, we will get an overview of ranking in SQL. We typically use `rank` and `dense_rank` functions to compute ranks.

```sql
SELECT count(*) FROM daily_product_revenue;
SELECT * FROM daily_product_revenue
ORDER BY order_date, order_revenue DESC;

-- rank() OVER ()
-- dense_rank() OVER ()

-- Global Ranking
   -- rank() OVER (ORDER BY col1 DESC)
-- Ranking based on key or partition key
   -- rank() OVER (PARTITION BY col2 ORDER BY col1 DESC)
```

## Compute Global Ranks using SQL

As part of this lecture, we will see how to compute global ranks using SQL. We will be using `daily_product_revenue` for the day of `2014, January 1st`.

```sql
SELECT order_date,
    order_item_product_id,
    order_revenue,
    rank() OVER (ORDER BY order_revenue DESC) AS rnk,
    dense_rank() OVER (ORDER BY order_revenue DESC) AS drnk
FROM daily_product_revenue
WHERE order_date = '2014-01-01 00:00:00.0'
ORDER BY order_revenue DESC;
```

## Compute Ranks based on key using SQL

As part of this lecture, we will see how to compute ranks based on order date for the month of 2014, January using SQL Queries.

```sql
SELECT order_date,
    order_item_product_id,
    order_revenue,
    rank() OVER (
            PARTITION BY order_date
            ORDER BY order_revenue DESC
    ) AS rnk,
    dense_rank() OVER (
            PARTITION BY order_date
            ORDER BY order_revenue DESC
    ) AS drnk
FROM daily_product_revenue
WHERE to_char(order_date::date, 'yyyy-MM') = '2014-01'
ORDER BY order_date, order_revenue DESC;
```

## Rules and Restrictions to Filter Data based on Ranks in SQL

As part of this lecture, we will review rules and restrictions to filter data based on ranks in SQL.
* The Windowing Functions or Analytical Functions can be used only in `SELECT` clause.
* As the `SELECT` clause is typically evaluated after `FROM`, `WHERE`, etc - the derived columns based on ranks in `SELECT` cannot be used in `WHERE` clause. For example, the below query will fail.

```sql
SELECT order_date,
    order_item_product_id,
    order_revenue,
    rank() OVER (
            PARTITION BY order_date
            ORDER BY order_revenue DESC
    ) AS rnk,
    dense_rank() OVER (
            PARTITION BY order_date
            ORDER BY order_revenue DESC
    ) AS drnk
FROM daily_product_revenue
WHERE to_char(order_date::date, 'yyyy-MM') = '2014-01'
    AND rnk <= 5
ORDER BY order_date, order_revenue DESC;
```

* We need to fall back on nested sub queries or views or CTEs to filter the data based on computed ranks using windowing or analytical functions.

## Filtering based on Global Ranks using Nested Queries and CTEs in SQL

As part of this lecture, we will see how to filter based on global ranks using nested queries and CTEs in SQL.

* Using Nested Sub Query

```sql
SELECT * FROM (
    SELECT order_date,
        order_item_product_id,
        order_revenue,
        rank() OVER (ORDER BY order_revenue DESC) AS rnk,
        dense_rank() OVER (ORDER BY order_revenue DESC) AS drnk
    FROM daily_product_revenue
    WHERE order_date = '2014-01-01 00:00:00.0'
) AS q
WHERE drnk <= 5
ORDER BY order_revenue DESC;
```

* Using CTE or Common Table Expressions

```sql
WITH daily_product_revenue_ranks AS (
    SELECT order_date,
        order_item_product_id,
        order_revenue,
        rank() OVER (ORDER BY order_revenue DESC) AS rnk,
        dense_rank() OVER (ORDER BY order_revenue DESC) AS drnk
    FROM daily_product_revenue
    WHERE order_date = '2014-01-01 00:00:00.0'
) SELECT * FROM daily_product_revenue_ranks
WHERE drnk <= 5
ORDER BY order_revenue DESC;
```

## Filtering based on Ranks per Partition using Nested Queries and CTEs in SQL

As part of this lecture, we will see how to filter based on ranks with in each day using nested queries and CTEs in SQL.

* Using Nested Subqueries

```sql
SELECT * FROM (
    SELECT order_date,
        order_item_product_id,
        order_revenue,
        rank() OVER (
            PARTITION BY order_date
            ORDER BY order_revenue DESC
        )  AS rnk,
        dense_rank() OVER (
            PARTITION BY order_date
            ORDER BY order_revenue DESC
        )  AS drnk
    FROM daily_product_revenue
    WHERE to_char(order_date::date, 'yyyy-MM') = '2014-01'
)  AS q
WHERE drnk <= 5
ORDER BY order_date, order_revenue DESC;
```

* Using common table expressions or CTEs

```sql
WITH daily_product_revenue_ranks AS (
    SELECT order_date,
        order_item_product_id,
        order_revenue,
        rank() OVER (
            PARTITION BY order_date
            ORDER BY order_revenue DESC
        ) AS rnk,
        dense_rank() OVER (
            PARTITION BY order_date
            ORDER BY order_revenue DESC
        ) AS drnk
    FROM daily_product_revenue
    WHERE to_char(order_date::date, 'yyyy-MM') = '2014-01'
) SELECT * FROM daily_product_revenue_ranks
WHERE drnk <= 5
ORDER BY order_date, order_revenue DESC;
```

## Create Students table with Data for ranking using SQL

As part of this lecture we will create students table with data for ranking using SQL. We will use the table to understand the difference between rank and dense_rank later.

```sql
CREATE TABLE student_scores (
    student_id INT PRIMARY KEY,
    student_score INT
);

INSERT INTO student_scores VALUES
(1, 980),
(2, 960),
(3, 960),
(4, 990),
(5, 920),
(6, 960),
(7, 980),
(8, 960),
(9, 940),
(10, 940);

SELECT * FROM student_scores;

SELECT * FROM student_scores
ORDER BY student_score DESC;

SELECT student_id,
    student_score,
    rank() OVER (ORDER BY student_score DESC) AS student_rank,
    dense_rank() OVER (ORDER BY student_score DESC) AS student_drank
FROM student_scores
ORDER BY student_score DESC;
```

## Difference between rank and dense rank using SQL

As part of this lecture, we will review the difference between `rank` and `dense_rank` functions which are typically used to compute ranks.
* `rank` will skip the ranks, in case of multiple records get same rank.
* `dense_rank` will not skip any ranks.
* Both `rank` and `dense_rank` yield same results if there are no duplicates in the column used for computing ranks.
* `dense_rank` is used more often compared to `rank`. For example, get all the students who are getting top n scores. There might be more than n number of students with ranks up to n, if there are students with same score.

```sql
SELECT student_id,
    student_score,
    rank() OVER (ORDER BY student_score DESC) AS student_rank,
    dense_rank() OVER (ORDER BY student_score DESC) AS student_drank
FROM student_scores
ORDER BY student_score DESC;
```
