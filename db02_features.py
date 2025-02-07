import sqlite3
import pathlib
import sys
from utils_logger import logger  # Import the logger

def execute_sql_file(connection, file_path: pathlib.Path) -> None:
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
    SQL_FEATURES_FOLDER = ROOT_DIR.joinpath("sql_features")
    
    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        return

    update_sql_file = SQL_FEATURES_FOLDER.joinpath("update_records.sql")
    execute_sql_file(connection, update_sql_file)

    delete_sql_file = SQL_FEATURES_FOLDER.joinpath("delete_records.sql")
    execute_sql_file(connection, delete_sql_file)
    
    logger.info("Feature engineering operations completed successfully.")
    connection.close()
    logger.info("Database connection closed.")

if __name__ == "__main__":
    main()
