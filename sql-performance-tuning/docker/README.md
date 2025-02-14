# Docker Setup for SQL Performance Tuning Workshop

This directory contains Docker configuration for setting up PostgreSQL with sample data for the SQL Performance Tuning Workshop.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Start the containers:
```bash
docker-compose up -d
```

2. The following services will be available:
   - PostgreSQL: localhost:6432
     - Database: performance_tuning
     - Username: postgres
     - Password: postgres
   - pgAdmin: http://localhost:5050
     - Email: admin@admin.com
     - Password: admin

3. The sample tables and data will be automatically created when the container starts up.

## Connecting to PostgreSQL

### Using psql in the container:
```bash
docker exec -it postgres_performance_tuning psql -U postgres -d performance_tuning
```

### Using psql from host:
```bash
psql -h localhost -p 6432 -U postgres -d performance_tuning
```

### Using pgAdmin:
1. Open http://localhost:5050 in your browser
2. Login with admin@admin.com / admin
3. Add a new server:
   - Host: postgres
   - Port: 5432
   - Database: performance_tuning
   - Username: postgres
   - Password: postgres

## Directory Structure
```
sql-performance-tuning/
├── docker/
│   ├── docker-compose.yml
│   └── README.md
└── setup/
    ├── 01_create_tables.sql
    └── 02_load_data.sql
```

## Verifying the Setup

After the containers are running, you can verify the setup by running:

```sql
-- Connect to the database
\c performance_tuning

-- List all tables
\dt

-- Check row counts
SELECT 
    table_name, 
    (xpath('/row/cnt/text()', xml_count))[1]::text::int as row_count
FROM (
    SELECT 
        table_name,
        query_to_xml(format('SELECT COUNT(*) as cnt FROM %I', table_name), false, true, '') as xml_count
    FROM information_schema.tables
    WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
) t;
```

## Troubleshooting

1. If the containers don't start properly:
```bash
# Check container logs
docker-compose logs

# Check postgres logs specifically
docker-compose logs postgres
```

2. If you need to reset the data:
```bash
# Stop containers and remove volumes
docker-compose down -v

# Start fresh
docker-compose up -d
```

3. If you need to rebuild the containers:
```bash
docker-compose build --no-cache
docker-compose up -d
```

## Performance Testing

The setup includes pgAdmin for visual query analysis and monitoring. You can use it to:
1. View query execution plans
2. Monitor database performance
3. Analyze table statistics
4. View index usage

For command-line performance testing, you can use:
```sql
-- Enable timing
\timing

-- Example query with execution plan
EXPLAIN ANALYZE
SELECT c.country, COUNT(*)
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.country;
``` 