import sqlite3
import os
import pathlib
import pandas as pd
import sys
from utils_logger import logger  # Import the logger

def execute_sql_file(connection, file_path: pathlib.Path) -> None:
    """
    Executes a SQL file using the provided SQLite connection.

    Args:
        connection (sqlite3.Connection): SQLite connection object.
        file_path (pathlib.Path): Path to the SQL file to be executed.
    """
    # Check if the SQL file exists before proceeding
    if not file_path.is_file():
        logger.error(f"SQL file does not exist: {file_path}")
        raise FileNotFoundError(f"SQL file not found: {file_path}")
    
    try:
        with open(file_path, 'r') as file:
            # Read the SQL file into a string
            sql_script: str = file.read()
        with connection:
            # Execute the SQL script using the connection
            connection.executescript(sql_script)
        logger.info(f"Executed: {file_path}")
    except Exception as e:
        logger.error(f"Failed to execute {file_path}: {e}")
        raise

def insert_data_from_csv(db_path: pathlib.Path, author_csv: pathlib.Path, book_csv: pathlib.Path) -> None:
    """
    Reads CSV files using pandas and inserts data into the database.
    This replaces any existing data in the 'authors' and 'books' tables.
    """
    try:
        # Read CSV files using pandas
        authors_df = pd.read_csv(author_csv)
        books_df = pd.read_csv(book_csv)
        # Write data to the database, replacing any existing data
        with sqlite3.connect(db_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
        logger.info("CSV data inserted successfully.")
    except Exception as e:
        logger.error(f"Error inserting CSV data: {e}")
        raise

def main() -> None:
    # Log the start of the database setup
    logger.info("Starting database setup...")
    
    # Define path variables
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_CREATE_FOLDER = ROOT_DIR.joinpath("sql_create")
    DATA_FOLDER = ROOT_DIR.joinpath("data")
    DB_PATH = DATA_FOLDER.joinpath('db.sqlite')
    
    # Define CSV file paths (ensure these CSVs have the correct headers)
    AUTHOR_CSV = DATA_FOLDER.joinpath("authors.csv")
    BOOK_CSV = DATA_FOLDER.joinpath("books.csv")
    
    # Ensure the data folder exists
    DATA_FOLDER.mkdir(exist_ok=True)
    
    try:
        # Connect to SQLite database (it will be created if it doesn't exist)
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")
        
        # Execute SQL files to set up the database schema
        execute_sql_file(connection, SQL_CREATE_FOLDER.joinpath('01_drop_tables.sql'))
        execute_sql_file(connection, SQL_CREATE_FOLDER.joinpath('02_create_tables.sql'))
        # If you have a SQL script that inserts test data, comment it out if you want to use CSV data.
        # execute_sql_file(connection, SQL_CREATE_FOLDER.joinpath('03_insert_tables.sql'))
        
        connection.close()  # Close connection before CSV import
        
        # Insert data from CSV files to populate the database with your CSV headers
        insert_data_from_csv(DB_PATH, AUTHOR_CSV, BOOK_CSV)
        
        logger.info("Database setup and CSV data import completed successfully.")
    except Exception as e:
        logger.error(f"Error during database setup: {e}")
    finally:
        try:
            connection.close()
        except Exception:
            pass
        logger.info("Database connection closed.")

if __name__ == '__main__':
    main()
