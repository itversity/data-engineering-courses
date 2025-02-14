#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting PostgreSQL setup for SQL Performance Tuning Workshop...${NC}"

# Wait for PostgreSQL to be ready
echo -e "${YELLOW}Waiting for PostgreSQL to be ready...${NC}"
until pg_isready -h postgres -p 6432 -U postgres > /dev/null 2>&1; do
    echo -n "."
    sleep 1
done
echo -e "\n${GREEN}PostgreSQL is ready!${NC}"

# Create tables
echo -e "${YELLOW}Creating tables...${NC}"
psql -h postgres -p 6432 -U postgres -d performance_tuning -f /docker-entrypoint-initdb.d/01_create_tables.sql
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Tables created successfully!${NC}"
else
    echo -e "${RED}Error creating tables${NC}"
    exit 1
fi

# Load data
echo -e "${YELLOW}Loading data...${NC}"
psql -h postgres -p 6432 -U postgres -d performance_tuning -f /docker-entrypoint-initdb.d/02_load_data.sql
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Data loaded successfully!${NC}"
else
    echo -e "${RED}Error loading data${NC}"
    exit 1
fi

# Verify setup
echo -e "${YELLOW}Verifying setup...${NC}"
psql -h postgres -p 6432 -U postgres -d performance_tuning -f /docker-entrypoint-initdb.d/03_verify_setup.sql > setup_verification.log
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Setup verified successfully!${NC}"
    echo -e "${YELLOW}Verification results saved to setup_verification.log${NC}"
else
    echo -e "${RED}Error during verification${NC}"
    exit 1
fi

echo -e "${GREEN}Setup completed successfully!${NC}"
echo -e "${YELLOW}You can now connect to:${NC}"
echo -e "  PostgreSQL: localhost:6432"
echo -e "  Database: performance_tuning"
echo -e "  Username: postgres"
echo -e "  Password: postgres"
echo -e "  pgAdmin: http://localhost:5050"
echo -e "  pgAdmin login: admin@admin.com / admin" 