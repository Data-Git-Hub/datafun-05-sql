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
    - `last` (Author's last name)
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
    ```
    author_id,first,last
    10f88232-1ae7-4d88-a6a2-dfcebb22a596,Harper,Lee
    c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70,George,Orwell
    e0b75863-866d-4db4-85c7-df9bb8ee6dab,F. Scott,Fitzgerald
    7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d,Aldous,Huxley
    8d8107b6-1f24-481c-8a21-7d72b13b59b5,J.D.,Salinger
    0cc3c8e4-e0c0-482f-b2f7-af87330de214,Ray,Bradbury
    4dca0632-2c53-490c-99d5-4f6d41e56c0e,Jane,Austen
    16f3e0a1-24cb-4ed6-a50d-509f63e367f7,J.R.R.,Tolkien
    06cf58ab-90f1-448d-8e54-055e4393e75c,J.R.R.,Tolkien
    6b693b96-394a-4a1d-a4e2-792a47d7a568,J.K.,Rowling
    ```
  - **books.csv**  
    ```
    book_id,title,year_published,author_id
    d6f83870-ff21-4a5d-90ab-26a49ab6ed12,To Kill a Mockingbird,1960,10f88232-1ae7-4d88-a6a2-dfcebb22a596
    0f5f44f7-44d8-4f49-b8c4-c64d847587d3,1984,1949,c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70
    f9d9e7de-c44d-4d1d-b3ab-59343bf32bc2,The Great Gatsby,1925,e0b75863-866d-4db4-85c7-df9bb8ee6dab
    38e530f1-228f-4d6e-a587-2ed4d6c44e9c,Brave New World,1932,7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d
    c2a62a4b-cf5c-4246-9bf7-b2601d542e6d,The Catcher in the Rye,1951,8d8107b6-1f24-481c-8a21-7d72b13b59b5
    3a1d835c-1e15-4a48-8e8c-b12239604e98,Fahrenheit 451,1953,0cc3c8e4-e0c0-482f-b2f7-af87330de214
    c6e67918-e509-4a6b-bc3a-979f6ad802f0,Pride and Prejudice,1813,4dca0632-2c53-490c-99d5-4f6d41e56c0e
    be951205-6cc2-4b3d-96f1-7257b8fc8c0f,The Hobbit,1937,16f3e0a1-24cb-4ed6-a50d-509f63e367f7
    dce0f8f2-d3ed-48a9-b8ff-960b6baf1f6f,The Lord of the Rings,1954,06cf58ab-90f1-448d-8e54-055e4393e75c
    ca8e64c3-1e67-47f5-82cc-3e4e30f63b75,Harry Potter and the Philosopher's Stone,1997,6b693b96-394a-4a1d-a4e2-792a47d7a568
    ```

---

## SQL Inquiries and Operations
---
### Using Jupyter Notebook, create a narrative that explores and shows the following SQL operations. 

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
