# SQL Performance Tuning Workshop

This workshop contains practical examples and exercises for SQL performance tuning across different scenarios. The material is designed for data engineers, database administrators, and developers who want to optimize their SQL queries and database performance.

## Prerequisites

- PostgreSQL 12+ installed
- Basic understanding of SQL
- Jupyter Notebook with SQL kernel
- Sample database (provided in setup scripts)

## Setup Instructions

1. Install PostgreSQL 12 or later
2. Create a new database named `performance_tuning`:
```sql
CREATE DATABASE performance_tuning;
```

3. Run the setup scripts to create sample tables and load data:
```bash
psql -d performance_tuning -f setup/01_create_tables.sql
psql -d performance_tuning -f setup/02_load_data.sql
```

## Workshop Structure

1. **Optimizing JOIN Operations**
   - Understanding different types of joins
   - Join order optimization
   - Using proper indexes for joins

2. **Indexing Strategies**
   - B-tree indexes
   - Partial indexes
   - Covering indexes
   - Index maintenance

3. **Subquery Optimization**
   - Converting subqueries to joins
   - Correlated vs non-correlated subqueries
   - EXISTS vs IN optimization

4. **Partitioning Strategies**
   - Range partitioning
   - List partitioning
   - Hash partitioning
   - Partition pruning

5. **Query Plan Analysis**
   - Reading execution plans
   - Cost estimation
   - Plan optimization techniques

6. **Materialized Views**
   - Creating and maintaining materialized views
   - Refresh strategies
   - Query optimization with materialized views

7. **Statistics and Cardinality**
   - Table statistics
   - Column statistics
   - Analyzing data distribution

8. **Window Functions Optimization**
   - Efficient window function usage
   - Frame clause optimization
   - Partitioning considerations

9. **Temporary Tables and CTEs**
   - When to use temporary tables
   - CTE optimization
   - Memory considerations

10. **Query Rewriting**
    - Rewriting for better performance
    - Alternative query patterns
    - Optimization techniques

## Running the Notebooks

Each notebook can be run independently, but it's recommended to follow the sequence as concepts build upon each other. Make sure to run the setup scripts first to create the necessary sample data.

## Additional Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [PostgreSQL Performance Tuning](https://wiki.postgresql.org/wiki/Performance_Optimization)
- [EXPLAIN ANALYZE](https://www.postgresql.org/docs/current/using-explain.html)

## Contributing

Feel free to submit issues and enhancement requests! 