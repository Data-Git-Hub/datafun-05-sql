import sqlite3
import pathlib
import sys
import pandas as pd
import matplotlib.pyplot as plt
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
    on semicolons (assuming semicolons are not present in literals) and returns a list
    of tuples: (statement, DataFrame).
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
                df = pd.read_sql_query(stmt, connection)
                results.append((stmt, df))
                logger.info(f"Executed statement (first 50 chars): {stmt[:50]}...")
            except Exception as e:
                logger.error(f"Error executing statement:\n{stmt}\nError: {e}")
        return results
    except Exception as e:
        logger.error(f"Error reading SQL query file {file_path}: {e}")
        return []

def visualize_group_by_authors(df: pd.DataFrame) -> None:
    """
    Creates a bar chart showing total books per author based on the group-by query results.
    Assumes the DataFrame has columns: author_id and total_books.
    """
    try:
        plt.figure(figsize=(8, 6))
        plt.bar(df['author_id'], df['total_books'], color='skyblue')
        plt.xlabel('Author ID')
        plt.ylabel('Total Books')
        plt.title('Total Books per Author')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        logger.error(f"Error during visualization (group by authors): {e}")

def visualize_aggregation_publication_year(df: pd.DataFrame) -> None:
    """
    Optionally, creates a line chart (or other suitable chart) showing the average publication year.
    Assumes the DataFrame has one row with the average_publication_year value.
    """
    try:
        avg_year = df.iloc[0]['average_publication_year']
        plt.figure(figsize=(4, 4))
        plt.text(0.5, 0.5, f"Avg Publication Year: {avg_year:.1f}",
                 fontsize=14, ha='center', va='center')
        plt.axis('off')
        plt.title('Average Publication Year')
        plt.show()
    except Exception as e:
        logger.error(f"Error during visualization (aggregation publication year): {e}")

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
    
    # Step 1: Execute data_addition.sql to update schema (add book_price) and insert pricing data.
    data_addition_file = SQL_QUERIES_FOLDER.joinpath("data_addition.sql")
    try:
        execute_script_file(connection, data_addition_file)
    except Exception as e:
        logger.error(f"Failed to execute data_addition.sql: {e}")
    
    # List of query files to execute.
    query_files = [
        "query_aggregation.sql",
        "query_filters.sql",  # Ensure this file exists; otherwise, remove from the list.
        "query_sorting.sql",
        "query_group_by.sql",
        "query_join.sql"
    ]
    
    # Dictionary to store results for possible visualization
    query_results = {}
    
    # Execute each query file and display its results.
    for qf in query_files:
        file_path = SQL_QUERIES_FOLDER.joinpath(qf)
        logger.info(f"Executing query file: {file_path}")
        results = execute_multiple_queries(connection, file_path)
        if results:
            print(f"\nResults for {qf}:")
            for stmt, df in results:
                print(f"\nStatement:\n{stmt}\n")
                print(df)
            # Store results for visualization (e.g., for group by queries)
            query_results[qf] = results
        else:
            logger.error(f"No results returned for {qf}")
    
    # Optional Visualization: If query_group_by.sql was executed,
    # visualize the total books per author using the first statement's results.
    if "query_group_by.sql" in query_results:
        # Assuming the first statement in query_group_by.sql is the group by author query.
        stmt, df_group = query_results["query_group_by.sql"][0]
        if 'author_id' in df_group.columns and 'total_books' in df_group.columns:
            visualize_group_by_authors(df_group)
    
    # Optional Visualization: Visualize the average publication year from query_aggregation.sql.
    if "query_aggregation.sql" in query_results:
        # Find the statement that returns average_publication_year.
        for stmt, df_agg in query_results["query_aggregation.sql"]:
            if 'average_publication_year' in df_agg.columns:
                visualize_aggregation_publication_year(df_agg)
                break

    connection.close()
    logger.info("Database connection closed.")

if __name__ == "__main__":
    main()
