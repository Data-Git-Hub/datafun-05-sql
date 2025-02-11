import sqlite3
import pathlib
import sys
import pandas as pd
from utils_logger import logger  # Import your custom logger

def execute_script_file(connection, file_path: pathlib.Path) -> None:
    """
    Executes a SQL script file (which may contain multiple statements)
    using connection.executescript (suitable for non-SELECT operations).
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
    except Exception as e:
        logger.error(f"Error executing SQL script file {file_path}: {e}")
        raise

def execute_multiple_queries(connection, file_path: pathlib.Path) -> list:
    """
    Executes multiple SELECT statements from a SQL file.
    Splits the file by semicolons (assuming no semicolons in literals)
    and returns a list of tuples (statement, DataFrame).
    """
    if not file_path.is_file():
        logger.error(f"SQL query file does not exist: {file_path}")
        return []
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        # Split the content on semicolons and filter out empty statements.
        statements = [stmt.strip() for stmt in content.split(';') if stmt.strip()]
        results = []
        for stmt in statements:
            try:
                # Execute the individual statement using pandas.
                df = pd.read_sql_query(stmt, connection)
                results.append((stmt, df))
                logger.info(f"Executed statement (first 50 chars): {stmt[:50]}...")
            except Exception as e:
                logger.error(f"Error executing statement: {stmt}\nError: {e}")
        return results
    except Exception as e:
        logger.error(f"Error reading SQL query file {file_path}: {e}")
        return []

def main() -> None:
    # Define paths
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    DATA_FOLDER = ROOT_DIR.joinpath("data")
    DB_PATH = DATA_FOLDER.joinpath("db.sqlite")
    SQL_QUERIES_FOLDER = ROOT_DIR.joinpath("sql_queries")
    
    # Connect to the SQLite database
    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        sys.exit(1)
    
    # Step 1: Execute data_addition.sql to update the schema and insert pricing data.
    data_addition_file = SQL_QUERIES_FOLDER.joinpath("data_addition.sql")
    try:
        execute_script_file(connection, data_addition_file)
    except Exception as e:
        logger.error(f"Failed to execute data_addition.sql: {e}")
    
    # List of query files to execute.
    query_files = [
        "query_aggregation.sql",
        "query_filters.sql",
        "query_sorting.sql",
        "query_group_by.sql",
        "query_join.sql"
    ]
    
    # Execute each query file and display its results.
    for qf in query_files:
        file_path = SQL_QUERIES_FOLDER.joinpath(qf)
        logger.info(f"Executing query file: {file_path}")
        results = execute_multiple_queries(connection, file_path)
        if results:
            print(f"\nResults for {qf}:")
            for stmt, df in results:
                print(f"\nStatement: {stmt}")
                print(df)
        else:
            logger.error(f"No results returned for {qf}")
    
    connection.close()
    logger.info("Database connection closed.")

if __name__ == "__main__":
    main()