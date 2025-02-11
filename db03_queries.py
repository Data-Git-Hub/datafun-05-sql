import sqlite3
import pathlib
import sys
import pandas as pd
from utils_logger import logger  # Import your custom logger

def execute_script_file(connection, file_path: pathlib.Path) -> None:
    """
    Executes a SQL script file (which may contain multiple statements)
    using connection.executescript. If a duplicate column error occurs
    (for example, for book_price), log a warning and continue.
    """
    if not file_path.is_file():
        logger.error(f"SQL script file does not exist: {file_path}")
        sys.exit(1)
    try:
        with open(file_path, 'r') as file:
            sql_script = file.read()
        with connection:
            connection.executescript(sql_script)
        logger.info(f"Executed SQL script file: {file_path}")
    except sqlite3.OperationalError as e:
        # Check for duplicate column error and ignore it.
        if "duplicate column name: book_price" in str(e):
            logger.warning(f"Column 'book_price' already exists in {file_path}. Skipping ALTER TABLE command.")
        else:
            logger.error(f"Error executing SQL script file {file_path}: {e}")
            raise
    except Exception as e:
        logger.error(f"Error executing SQL script file {file_path}: {e}")
        raise

def execute_multiple_queries(connection, file_path: pathlib.Path) -> list:
    """
    Executes multiple SELECT statements from a SQL file by splitting the file
    on semicolons (assuming semicolons are not present in literals). Returns a list
    of tuples: (statement, DataFrame).
    """
    if not file_path.is_file():
        logger.error(f"SQL query file does not exist: {file_path}")
        return []
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        # Split the file into individual statements.
        statements = [stmt.strip() for stmt in content.split(';') if stmt.strip()]
        results = []
        for stmt in statements:
            try:
                df = pd.read_sql_query(stmt, connection)
                results.append((stmt, df))
                logger.info(f"Executed statement (first 50 chars): {stmt[:50]}...")
            except Exception as e:
                logger.error(f"Error executing statement:\n{stmt}\nError: {e}")
        return results
    except Exception as e:
        logger.error(f"Error reading SQL query file {file_path}: {e}")
        return []

def main() -> None:
    # Define project directories and paths.
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    DATA_FOLDER = ROOT_DIR.joinpath("data")
    DB_PATH = DATA_FOLDER.joinpath("db.sqlite")
    SQL_QUERIES_FOLDER = ROOT_DIR.joinpath("sql_queries")
    
    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        sys.exit(1)
    
    # Execute data_addition.sql to update schema (add book_price) and insert pricing.
    data_addition_file = SQL_QUERIES_FOLDER.joinpath("data_addition.sql")
    try:
        execute_script_file(connection, data_addition_file)
    except Exception as e:
        logger.error(f"Failed to execute data_addition.sql: {e}")
    
    # List of query files to execute.
    query_files = [
        "query_aggregation.sql",
        "query_filter.sql",  
        "query_sorting.sql",
        "query_group_by.sql",
        "query_join.sql"
    ]
    
    # Execute each query file and display results.
    for qf in query_files:
        file_path = SQL_QUERIES_FOLDER.joinpath(qf)
        logger.info(f"Executing query file: {file_path}")
        results = execute_multiple_queries(connection, file_path)
        if results:
            print(f"\nResults for {qf}:")
            for stmt, df in results:
                print(f"\nStatement:\n{stmt}\n")
                print(df)
        else:
            logger.error(f"No results returned for {qf}")
    
    connection.close()
    logger.info("Database connection closed.")

if __name__ == "__main__":
    main()
