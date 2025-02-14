## Overview of Azure Database for PostgreSQL
Azure Database for PostgreSQL is a fully-managed database as a service with built-in capabilities, such as high availability and intelligence.
* You can continue to use languages and frameworks of your choice with no upfront costs.
* Pay only for what you use with reserved capacity pricing now available.

Here are some of the key benefits with respect to Azure Database for PostgreSQL
* Focus on application innovation instead of database management.
* Migrate with ease to a fully managed open-source database with support for the latest PostgreSQL versions.
* Azure Database for PostgreSQL offers a service-level agreement (SLA) of up to 99.99 percent uptime, AI-powered performance    optimisation, and advanced security.

Review [Official Documentation](https://azure.microsoft.com/en-in/products/postgresql/#overview) for more details.

## Setup Azure Database for PostgreSQL
Let us go ahead and setup Azure Database for PostgreSQL.
* Login into the Azure portal.
* Search for Azure Database for PostgreSQL.
* Select the Flexible server deployment option.
* Fill out the Basics form with the relavant information.
* Select Review + create to review your selections. Select Create to provision the server. This operation may take a few minutes.

## Configure Network for Azure Database for PostgreSQL
Let us go ahead and configure network for Azure Database for PostgreSQL, so that we can connect from our local development environments.
* Go to Network on your Azure Database for PostgreSQL
* Click on add my current IP option.

## Connect to zure Database for PostgreSQL using Developer Tools
Make sure to setup Postgres on your local environment, so that you get all the tools such as pgAdmin, psql, etc.
* You can use pgAdmin or psql to connect to Azure Database for PostgreSQL.
* Make sure to keep the credentials handy and then use the following command as reference to connect to the database. Replace <host_ip>, with actual server name of the Azure Database for PostgreSQL Server.

## Setup Database in Azure Database for PostgreSQL Server
```
CREATE DATABASE itversity_retail_db;
CREATE USER itversity_retail_user WITH ENCRYPTED PASSWORD 'itversity';
GRANT ALL ON DATABASE itversity_retail_db TO itversity_retail_user;
```

## Setup Tables in Azure Database for PostgreSQL
Let us go ahead and setup retail db tables and also populate data in Azure Database for PostgreSQL.
* The scripts are provided under data/retail_db folder with in this GitHub repository.
* Connect to the newly created Postgres Database. Here are the credentials for your reference.
  * hostname - server name
  * database name -itversity_retail_db
  * username - Server admin login name
  * password - password given for Azure Database for PostgreSQL
  * port number - 5432

* Run the below commands to create tables and also populate data in the tables.
```
\i data/retail_db/create_db_tables_pg.sql 
\i data/retail_db/load_db_tables_pg.sql
```

## Validate Data in Azure Database for PostgreSQL Tables

```
\d -- List tables

SELECT * FROM departments;
SELECT count(*) FROM departments;

SELECT * FROM orders LIMIT 10;
SELECT count(*) FROM orders;

SELECT * FROM order_items LIMIT 10;
SELECT count(*) FROM order_items;

SELECT count(*) FROM categories;
SELECT count(*) FROM products;
SELECT count(*) FROM customers;
```

## Integration of Azure Database for PostgreSQL with Python
Let us also see how we can get started with Python based applications using Cloud SQL Postgres.

* We need to setup `psycopg2-binary` using `pip`. You can use `pip install psycopg2-binary` to install Postgres Python Connector Library in the virtual environment of the project.
* We can then create connection object.
* Using connection object, we can create cursor object by passing relevant query to it.
* We can process the data using cursor object.
* We can perform `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc using this approach.
```
import psycopg2
conn = psycopg2.connect(
    host='<server name>',
    database='itversity_retail_db',
    user='<Server admin login name>',
    password='<password>',
    port = '5432'
)

cur = conn.cursor()

cur.execute('SELECT * FROM orders LIMIT 10')

conn.commit()

data = cur.fetchall()

for i in data:
    print(i)

cur.close()
conn.close()
```

## Integration of Azure Database for PostgreSQL with Pandas
Pandas is a powerful Python Data Library which is used to process as well as analyze the data. It have robust APIs to work with databases.

Here are the steps involved to use Pandas to work with databases like Postgres.

* We need to make sure `pandas`, `psycopg2-binary` as well as `sqlalchemy` installed using `pip`.
* Pandas uses `sqlalchemy` to interact with database tables based on the connection url.
* `sqlalchemy` is the most popular ORM to hide the complexity of connecting to the databases using libraries such as Pandas.
* Here are the examples using Pandas. We first read the data from the files, process it and then write to Postgres Database using Pandas. We will also read the data written to Postgres Database Table using Pandas for the validation.
```
import pandas as pd
columns = ['order_id', 'order_date', 'order_customer_id', 'order_status']
orders = pd.read_csv(r'C:\Users\FL_LPT-318\data\retail_db\orders\part-00000', names=columns)
daily_status_count = orders. \
    groupby(['order_date', 'order_status'])['order_id']. \
    agg(order_count='count'). \
    reset_index()

help(daily_status_count.to_sql)

daily_status_count.to_sql(
    'daily_status_count',
    'postgresql://<Server admin login name>:<password>@<server name>:5432/itversity_retail_db', 
    if_exists='replace',
    index=False
)

help(pd.read_sql)

df = pd.read_sql(
    'SELECT * FROM daily_status_count',
    'postgresql://<Server admin login name>:<password>@<server name>:5432/itversity_retail_db'
)
print(df)
```




