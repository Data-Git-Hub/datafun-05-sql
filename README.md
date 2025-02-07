# datafun-05-sql
---

## Project 5 integrates Python and SQL, focusing on database interactions using SQLite. The project involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

---

## Database Management and Creation
---
In this project, database management is handled through a combination of SQL scripts and Python automation. The objective is to ensure that the database is easy to initialize, modify, and reset for repeated testing and demonstration of SQL operations.

### SQL Script Organization:
- **sql_create Folder:**  
  Contains the SQL scripts used to set up the database:
  - **01_drop_tables.sql:**  
    Contains SQL commands to drop existing tables. This ensures that you can re-run the setup script without encountering errors due to pre-existing tables.
  - **02_create_tables.sql:**  
    Contains SQL commands to create the new database schema. This script defines the tables, columns, and constraints, including primary keys and foreign keys.
  - **03_insert_records.sql:**  
    Contains SQL commands to insert at least 10 sample records into each table, providing a dataset for testing and demonstrating various SQL operations.

### Python Integration:
- **db01_setup.py:**  
  A Python script that:
  1. Connects to (or creates) the SQLite database.
  2. Executes the SQL scripts in order (drop, create, then insert) to ensure a clean and repeatable setup.
  3. Incorporates error handling and messaging to confirm that each step executes successfully.
  
This approach makes it straightforward to reset the database state, which is critical during development and testing.

---

## Database Schema
---
The database schema is designed to demonstrate relational database principles, including the use of primary keys, foreign keys, and data integrity constraints. Our schema includes at least two related tables that illustrate a typical one-to-many relationship.

### Key Elements:
- **Table Relationships:**  
  For example, you might have:
  - A **Customers** table that stores customer information with a unique customer ID as the primary key.
  - An **Orders** table that stores order details. Each order is linked to a customer via a foreign key (customer ID), representing a one-to-many relationship.
  
- **Primary Keys:**  
  Each table has a primary key that uniquely identifies its records.
  
- **Foreign Keys:**  
  The child table (e.g., Orders) includes a foreign key that references the parent table (e.g., Customers), ensuring referential integrity.
  
- **Data Types and Constraints:**  
  Columns are defined with appropriate data types (e.g., INTEGER, TEXT, DATE) along with constraints such as NOT NULL and UNIQUE to maintain data integrity.

### Documentation:
- The complete schema is implemented in the `02_create_tables.sql` file.
- Detailed documentation (including entity-relationship diagrams or descriptions of each table and its relationships) is provided here to help developers understand the design decisions.

---

## SQL Inquiries and Operations
---
### Using Jupyter Notebook create a narrative that explores and shows the following SQL operations. 

- SELECT command
- WHERE command
- ORDER BY command
- INNER JOIN command
- INSERT INTO command
- UPDATE command
- DELETE FROM command
- GROUP BY command
- LEFT JOIN command
- RIGHT JOIN command
- COUNT command
- AVG command
- SUM command

These operations are demonstrated through a set of SQL scripts and corresponding Python scripts:

### SQL Scripts Organization:
- **sql_features Folder:**  
  Contains scripts that focus on data cleaning and feature engineering:
  - **update_records.sql:** Contains SQL commands to update one or more records.
  - **delete_records.sql:** Contains SQL commands to delete specific records.

- **sql_queries Folder:**  
  Contains scripts for performing aggregations and queries:
  - **query_aggregation.sql:** Demonstrates aggregation functions (e.g., COUNT, AVG, SUM).
  - **query_filter.sql:** Uses WHERE clauses to filter data.
  - **query_sorting.sql:** Uses ORDER BY to sort data.
  - **query_group_by.sql:** Uses GROUP BY to group data along with aggregations.
  - **query_join.sql:** Uses INNER JOIN (and optionally LEFT JOIN or RIGHT JOIN) to combine data from multiple tables.

### Python Integration:
- **db02_features.py:**  
  A Python script that executes the feature engineering SQL scripts, showcasing operations like updating, deleting, or even adding additional columns.
  
- **db03_queries.py:**  
  A Python script that:
  1. Connects to the SQLite database.
  2. Executes the query scripts.
  3. Retrieves and displays the results.
  4. Optionally, includes additional analysis or visualizations using libraries such as pandas or matplotlib.

This section illustrates how various SQL operations are applied to manipulate and analyze the database, providing a practical overview of working with relational databases in Python.

---