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
The database schema for this project is designed to demonstrate relational database principles using data sourced from two CSV files: `authors.csv` and `books.csv`. The schema consists of two related tables:

### Key Elements:
- **Authors Table:**  
  - **Primary Key:**  
    The `author_id` field is used as the primary key to uniquely identify each author.
  - **Columns:**  
    - `author_id` (Primary Key)
    - `first` (Author's first name)
    - `surname` (Author's last name)
  - **Data Source:**  
    Data is imported from the `authors.csv` file.

- **Books Table:**  
  - **Primary Key:**  
    The `book_id` field is used as the primary key to uniquely identify each book.
  - **Columns:**  
    - `book_id` (Primary Key)
    - `title` (Book title)
    - `year_published` (Year the book was published)
    - `author_id` (Foreign key referencing the Authors table)
  - **Foreign Key Constraint:**  
    The `author_id` in the Books table creates a relationship with the Authors table, ensuring that each book is associated with a valid author.

### Data Integrity and Constraints:
- The use of `author_id` as the primary key in the Authors table guarantees that each author is uniquely identified.
- The foreign key constraint in the Books table enforces referential integrity, meaning every `author_id` in the Books table must correspond to an existing author in the Authors table.
- Columns are defined with appropriate data types and constraints (such as NOT NULL and UNIQUE) to maintain consistent and valid data.

### Documentation:
- The complete schema is implemented in the `02_create_tables.sql` file located in the `sql_create` folder.
- Data is sourced from the following CSV files, located in the `data` folder:
  - **authors.csv**  
  - **books.csv**  

---

## SQL Inquiries and Operations
---
### Create a narrative that explores and shows the following SQL operations. 

- COUNT command
- AVG command
- SUM command
- WHERE command
- ORDER BY command
- GROUP BY command
- INNER JOIN command
- LEFT JOIN command
- RIGHT JOIN command


These operations are demonstrated through a set of SQL scripts and corresponding Python scripts:

### SQL Scripts Organization:
- **sql_features Folder:**  
  Contains scripts that focus on data cleaning and feature engineering:
  - **update_records.sql:** Contains SQL commands to update one or more records.
  - **delete_records.sql:** Contains SQL commands to delete specific records.

- **sql_queries Folder:**  
  Contains scripts for performing aggregations and queries:
  - **data_addition.sql** Add additional column for book_price to give more fidelity of data
  - **query_aggregation.sql:** Demonstrates aggregation functions (e.g., COUNT, AVG, SUM).
  - **query_filter.sql:** Uses WHERE clauses to filter data.
  - **query_sorting.sql:** Uses ORDER BY to sort data.
  - **query_group_by.sql:** Uses GROUP BY to group data along with aggregations.
  - **query_join.sql:** Uses INNER JOIN (and optionally LEFT JOIN) to combine data from multiple tables.

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

## Run Scripts

---
### 1. Create a Virtual Environment and Install Dependencies
Create a virtual environment, activate it, and install the required packages listed in `requirements.txt`.

#### Windows Example:


