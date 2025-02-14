-- Load sample data for SQL performance tuning workshop

-- Insert sample customer segments
INSERT INTO customer_segments (segment_name, description) VALUES
('Consumer', 'Individual retail customers'),
('Corporate', 'Business and corporate accounts'),
('Small Business', 'Small business customers'),
('Enterprise', 'Large enterprise accounts');

-- Insert sample product categories
INSERT INTO product_categories (category_name, description) VALUES
('Electronics', 'Electronic devices and accessories'),
('Furniture', 'Office and home furniture'),
('Office Supplies', 'General office supplies'),
('Clothing', 'Apparel and accessories');

-- Insert sample suppliers
INSERT INTO suppliers (supplier_name, contact_name, email, phone, country) VALUES
('Tech Supplies Co', 'John Smith', 'john@techsupplies.com', '555-0101', 'USA'),
('Furniture Plus', 'Mary Johnson', 'mary@furnitureplus.com', '555-0102', 'Canada'),
('Office Direct', 'Bob Wilson', 'bob@officedirect.com', '555-0103', 'USA'),
('Global Electronics', 'Alice Brown', 'alice@globalelec.com', '555-0104', 'UK');

-- Insert sample sales representatives
INSERT INTO sales_reps (first_name, last_name, email, region, hire_date) VALUES
('David', 'Miller', 'david@company.com', 'North', '2020-01-15'),
('Sarah', 'Wilson', 'sarah@company.com', 'South', '2020-02-20'),
('Michael', 'Brown', 'michael@company.com', 'East', '2020-03-25'),
('Lisa', 'Davis', 'lisa@company.com', 'West', '2020-04-30');

-- Generate sample customers
INSERT INTO customers (first_name, last_name, email, country, city, postal_code, segment)
SELECT
    'Customer' || i as first_name,
    'Last' || i as last_name,
    'customer' || i || '@email.com' as email,
    CASE (i % 4) 
        WHEN 0 THEN 'USA'
        WHEN 1 THEN 'Canada'
        WHEN 2 THEN 'UK'
        WHEN 3 THEN 'Australia'
    END as country,
    'City' || (i % 10) as city,
    '1000' || i as postal_code,
    CASE (i % 4)
        WHEN 0 THEN 'Consumer'
        WHEN 1 THEN 'Corporate'
        WHEN 2 THEN 'Small Business'
        WHEN 3 THEN 'Enterprise'
    END as segment
FROM generate_series(1, 1000) i;

-- Generate sample products
INSERT INTO products (product_name, category, subcategory, price, cost, supplier_id, stock_quantity)
SELECT
    'Product' || i as product_name,
    CASE (i % 4)
        WHEN 0 THEN 'Electronics'
        WHEN 1 THEN 'Furniture'
        WHEN 2 THEN 'Office Supplies'
        WHEN 3 THEN 'Clothing'
    END as category,
    'Subcategory' || (i % 10) as subcategory,
    (random() * 1000)::numeric(10,2) as price,
    (random() * 800)::numeric(10,2) as cost,
    (i % 4) + 1 as supplier_id,
    (random() * 100)::int as stock_quantity
FROM generate_series(1, 500) i;

-- Generate sample orders
INSERT INTO orders (customer_id, order_date, ship_date, ship_mode, status, total_amount)
SELECT
    (random() * 999 + 1)::int as customer_id,
    timestamp '2020-01-01' + (random() * (interval '3 years')) as order_date,
    timestamp '2020-01-01' + (random() * (interval '3 years')) as ship_date,
    CASE (i % 3)
        WHEN 0 THEN 'Standard'
        WHEN 1 THEN 'Express'
        WHEN 2 THEN 'Next Day'
    END as ship_mode,
    CASE (i % 4)
        WHEN 0 THEN 'Completed'
        WHEN 1 THEN 'Pending'
        WHEN 2 THEN 'Shipped'
        WHEN 3 THEN 'Cancelled'
    END as status,
    (random() * 5000)::numeric(10,2) as total_amount
FROM generate_series(1, 10000) i;

-- Generate sample order items
INSERT INTO order_items (order_id, product_id, quantity, unit_price, discount)
SELECT
    (random() * 9999 + 1)::int as order_id,
    (random() * 499 + 1)::int as product_id,
    (random() * 10 + 1)::int as quantity,
    (random() * 1000)::numeric(10,2) as unit_price,
    (random() * 0.5)::numeric(4,2) as discount
FROM generate_series(1, 50000) i;

-- Update statistics
ANALYZE customers;
ANALYZE products;
ANALYZE orders;
ANALYZE order_items;
ANALYZE suppliers;
ANALYZE sales_reps;
ANALYZE customer_segments;
ANALYZE product_categories; 