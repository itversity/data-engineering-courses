-- Verify table creation and data loading

-- Check table existence and row counts
SELECT 
    table_name, 
    (xpath('/row/cnt/text()', xml_count))[1]::text::int as row_count
FROM (
    SELECT 
        table_name,
        query_to_xml(format('SELECT COUNT(*) as cnt FROM %I', table_name), false, true, '') as xml_count
    FROM information_schema.tables
    WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
) t
ORDER BY table_name;

-- Check index creation
SELECT 
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;

-- Verify data distribution
SELECT 'Customers by Country' as metric,
    country,
    COUNT(*) as count,
    ROUND(COUNT(*)::numeric / SUM(COUNT(*)) OVER () * 100, 2) as percentage
FROM customers
GROUP BY country
ORDER BY count DESC;

SELECT 'Orders by Status' as metric,
    status,
    COUNT(*) as count,
    ROUND(COUNT(*)::numeric / SUM(COUNT(*)) OVER () * 100, 2) as percentage
FROM orders
GROUP BY status
ORDER BY count DESC;

SELECT 'Products by Category' as metric,
    category,
    COUNT(*) as count,
    ROUND(COUNT(*)::numeric / SUM(COUNT(*)) OVER () * 100, 2) as percentage
FROM products
GROUP BY category
ORDER BY count DESC;

-- Check foreign key relationships
SELECT 
    tc.table_name, 
    kcu.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_schema = kcu.table_schema
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
    AND ccu.table_schema = tc.table_schema
WHERE tc.constraint_type = 'FOREIGN KEY'
AND tc.table_schema = 'public'
ORDER BY tc.table_name;

-- Check view definitions
SELECT 
    viewname,
    definition
FROM pg_views
WHERE schemaname = 'public'
ORDER BY viewname;

-- Sample data preview
\echo '\nCustomers Sample:'
SELECT * FROM customers LIMIT 5;

\echo '\nProducts Sample:'
SELECT * FROM products LIMIT 5;

\echo '\nOrders Sample:'
SELECT * FROM orders LIMIT 5;

\echo '\nOrder Items Sample:'
SELECT * FROM order_items LIMIT 5;

-- Basic performance test
\timing on

\echo '\nBasic JOIN Performance Test:'
EXPLAIN ANALYZE
SELECT 
    c.country,
    p.category,
    COUNT(DISTINCT o.order_id) as num_orders,
    SUM(oi.quantity * oi.unit_price) as total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date >= '2022-01-01'
GROUP BY c.country, p.category
ORDER BY total_revenue DESC
LIMIT 10; 