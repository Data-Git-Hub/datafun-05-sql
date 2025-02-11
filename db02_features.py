import sqlite3
import pathlib
import sys
from utils_logger import logger  # Import the logger

def execute_sql_file(connection, file_path: pathlib.Path) -> None:
    """
    Executes a SQL file using the provided SQLite connection.

    Args:
        connection (sqlite3.Connection): SQLite connection object.
        file_path (pathlib.Path): Path to the SQL file to be executed.
    """
    if not file_path.is_file():
        logger.error(f"SQL file does not exist: {file_path}")
        sys.exit(1)
    
    try:
        with open(file_path, 'r') as file:
            sql_script = file.read()
        with connection:
            connection.executescript(sql_script)
        logger.info(f"Executed SQL file: {file_path}")
    except Exception as e:
        logger.error(f"Error executing SQL file {file_path}: {e}")
        raise

def main() -> None:
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    DATA_FOLDER = ROOT_DIR.joinpath("data")
    DB_PATH = DATA_FOLDER.joinpath("db.sqlite")
    # Define folder paths for both SQL creation and feature scripts
    SQL_CREATE_FOLDER = ROOT_DIR.joinpath("sql_create")
    SQL_FEATURES_FOLDER = ROOT_DIR.joinpath("sql_features")
    
    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        return

    # Execute the insert script from the sql_create folder to populate the tables
    insert_sql_file = SQL_CREATE_FOLDER.joinpath("03_insert_tables.sql")
    execute_sql_file(connection, insert_sql_file)
    
    # Now run the feature scripts: update and delete operations
    update_sql_file = SQL_FEATURES_FOLDER.joinpath("update_records.sql")
    execute_sql_file(connection, update_sql_file)

    delete_sql_file = SQL_FEATURES_FOLDER.joinpath("delete_records.sql")
    execute_sql_file(connection, delete_sql_file)
    
    logger.info("Feature engineering operations completed successfully.")
    connection.close()
    logger.info("Database connection closed.")

if __name__ == "__main__":
    main()
