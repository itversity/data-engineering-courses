# Setup Application Tables and Data in Postgres Database

* Overview of Postgres Database Server and pgAdmin
* Overview of Database Connection Details
* Overview of Connecting to External Databases using pgAdmin
* Create Application Database and User in Postgres Database Server
* Clone Data Sets from Git Repository for Database Scripts
* Register Server in pgAdmin using Application Database and User
* Setup Application Tables and Data in Postgres Database
* Overview of pgAdmin to write SQL Queries

## Overview of Postgres Database Server and pgAdmin

As part of this lecture we will get an overview of Postgres Database Server and pgAdmin.
* Postgres Database Server is a multi tenant Database Server.
* There can be many databases as part of one Postgres Database Server.
* **pgAdmin** is an IDE to interact with Postgres Database.
* **pgAdmin** can simplify the connection process to multiple Postgres Databases on multiple Database Servers.
* **pgAdmin** provides tools to access Database objects and also run SQL Queries.

## Overview of Database Connection Details

As part of this lecture we will get an overview of Database Connection Details. Typically we need following to connect to any Postgres Database.
* Hostname or Server IP on which Postgres Database Server is installed.
* Port Number on which a given Postgres Database is running.
* Database Name using which we would like to run queries.
* Username and Password to authenticate against a given Database.

Note: The User should have required permissions on the Database to create tables or manage data in the tables or run SQL queries against the tables.

## Overview of Connecting to External Databases using pgAdmin

As part of this lecture we will get an overview of Connecting to External Postgres Databases using pgAdmin.
* If we are attempting to connect to the Postgres database server running on our PC where pgAdmin is also installed, then we use localhost or 127.0.0.1.
* In case we would like to connect to an external Postgres database server, then we need to provide DNS Alias or IP Address of the server.

## Create Application Database and User in Postgres Database Server

As part of this lecture we will create application database and user in Postgres Database Server.
* By default, we will be provided with a database and user by name **postgres** as part of installed Postgres Database Server.
* We should not use **postgres** database except for administration tasks.
* For now, we will connect to **postgres** database using **postgres** user and create Application Database and User.
* Here are the commands that are used to create Application Database and User in Postgres Database Server.

```sql
CREATE DATABASE itversity_retail_db;
CREATE USER itversity_retail_user WITH ENCRYPTED PASSWORD 'itversity';
GRANT ALL ON DATABASE itversity_retail_db TO itversity_retail_user;

-- Applicable for Postgres 15 and not covered in the video
ALTER DATABASE itversity_retail_db OWNER TO itversity_retail_user;
```

## Clone Data Sets from Git Repository for Database Scripts

As part of this lecture we will clone data sets from git repository for Database Scripts. The Database Scripts have required commands to not only create tables in Postgres Database but also to populate data into Postgres Tables.
* Make sure to go to https://github.com/dgadiraju/data and download into your Mac or Windows. We will also provide the data folder as part of this repository.
* It contain several folders, but the scripts to create Postgres Tables and load data into Postgres Tables under **retail_db** folder.
* You need to use following scripts to create tables and populate data into Postgres Tables.
  * **create_db_tables_pg.sql** - to create tables in Postgres Database.
  * **load_db_tables_pg.sql** - to populate data into Postgres Tables.

## Register Server in pgAdmin using Application Database and User

As part of this lecture, you will learn how to register server with connection details in pgAdmin to connect to newly created Application Database and User.
* Server: localhost
* Port: 5432
* Database Name: itversity_retail_db
* Username: itversity_retail_user
* Password: itversity

Note: If you use some other details while creating the Postgres Database and Credentials (username and password), make sure to use the correct information.

## Setup Application Tables and Data in Postgres Database

As part of this lecture you will understand how to setup Application Table and Data in Postgres Database using Scripts.
* Make sure to connect to right Postgres Database using correct credentials. You can use **pgAdmin** to connect to the database.
* Load the scripts and run using **pgAdmin**.

## Overview of pgAdmin to write SQL Queries

As part of this lecture, you will get an overview of pgAdmin to write SQL Queries against Postgres Database Tables.
* Make sure to connect to right postgres database.
* Launch **Query Tool** by right clicking and selection **Query Tool** in the menu.
* Here are the queries you can run to see data in `orders` and `order_items` tables.

```sql
SELECT * FROM orders LIMIT 10;

SELECT * FROM order_items LIMIT 10;
```