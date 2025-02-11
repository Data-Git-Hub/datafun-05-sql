import sqlite3
import pathlib
import sys
import pandas as pd
import matplotlib.pyplot as plt
from utils_logger import logger  # Import your custom logger

# Set a global font size for other matplotlib elements.
plt.rcParams.update({'font.size': 11})

def insert_data_from_csv(db_path: pathlib.Path, authors_csv: pathlib.Path, books_csv: pathlib.Path) -> None:
    """
    Reads the CSV files and imports the data into the database.
    This will replace the 'authors' and 'books' tables with data from the CSV files.
    """
    try:
        authors_df = pd.read_csv(authors_csv)
        books_df = pd.read_csv(books_csv)
        with sqlite3.connect(db_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
        logger.info("CSV data inserted successfully.")
    except Exception as e:
        logger.error(f"Error inserting CSV data: {e}")
        raise

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
        # Split on semicolons and remove empty statements.
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

def maximize_figure():
    """
    Attempts to maximize the current matplotlib figure window.
    This may depend on the backend and operating system.
    """
    try:
        mng = plt.get_current_fig_manager()
        # For TkAgg backend on Windows.
        try:
            mng.window.state('zoomed')
        except AttributeError:
            try:
                mng.window.showMaximized()
            except Exception as e:
                logger.warning("Could not maximize window: " + str(e))
    except Exception as e:
        logger.warning("Error maximizing figure: " + str(e))

def display_dataframe_text(df: pd.DataFrame, title: str) -> None:
    """
    Displays the DataFrame as preformatted text in a matplotlib figure using a monospace font.
    Maximizes the figure window and waits for a key press (Spacebar/Enter) in the figure window.
    """
    try:
        table_str = df.to_string(index=False)
        num_lines = table_str.count('\n') + 1
        fig, ax = plt.subplots(figsize=(12, num_lines * 0.6 + 2), dpi=100)
        maximize_figure()
        ax.axis('off')
        ax.text(0.5, 0.5, table_str, fontsize=17, ha='center', va='center', fontfamily='monospace')
        plt.title(title, fontsize=21)
        plt.tight_layout()
        plt.show(block=False)
        print("Press Spacebar or Enter in the figure window to continue...")
        plt.waitforbuttonpress()
        plt.close(fig)
    except Exception as e:
        logger.error(f"Error displaying DataFrame text: {e}")

def visualize_publication_year_histogram(connection) -> None:
    """
    Creates a histogram of the number of books by publication year,
    using bins from 1950 to 2020 in 10-year intervals.
    """
    try:
        query = "SELECT year_published FROM books WHERE year_published BETWEEN 1950 AND 2020"
        df = pd.read_sql_query(query, connection)
        if df.empty:
            logger.error("No year_published data available for histogram.")
            return
        bins = list(range(1950, 2030, 10))
        fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
        maximize_figure()
        ax.hist(df['year_published'], bins=bins, edgecolor='black', color='skyblue')
        ax.set_xlabel('Publication Year', fontsize=13)
        ax.set_ylabel('Number of Books', fontsize=13)
        ax.set_title('Distribution of Books by Publication Year (1950-2020)', fontsize=15)
        ax.set_xticks(bins)
        ax.tick_params(axis='both', labelsize=11)
        plt.tight_layout()
        plt.show(block=False)
        print("Press Spacebar or Enter in the figure window to continue...")
        plt.waitforbuttonpress()
        plt.close()
    except Exception as e:
        logger.error(f"Error during publication year histogram visualization: {e}")

def visualize_book_price_pie(connection) -> None:
    """
    Creates a pie chart where each slice represents a book's price as a percentage of
    the total book prices. The label for each slice is the book's price.
    """
    try:
        query = "SELECT book_price FROM books WHERE book_price IS NOT NULL"
        df = pd.read_sql_query(query, connection)
        if df.empty:
            logger.error("No book_price data available for pie chart.")
            return
        labels = df['book_price'].astype(str)
        fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
        maximize_figure()
        ax.pie(df['book_price'], labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 15})
        ax.set_title('Book Price Distribution', fontsize=19)
        plt.tight_layout()
        plt.show(block=False)
        print("Press Spacebar or Enter in the figure window to continue...")
        plt.waitforbuttonpress()
        plt.close()
    except Exception as e:
        logger.error(f"Error during book price pie chart visualization: {e}")

def visualize_total_books_per_author(connection) -> None:
    """
    Creates a bar chart showing the total number of books per author.
    Uses a LEFT JOIN to include all authors.
    Displays the author's first and surname (concatenated) as the x-axis labels.
    """
    try:
        query = """
        SELECT 
            a.first, 
            a.surname,
            COUNT(b.book_id) AS total_books
        FROM authors a
        LEFT JOIN books b ON a.author_id = b.author_id
        GROUP BY a.first, a.surname
        ORDER BY a.surname;
        """
        df = pd.read_sql_query(query, connection)
        if df.empty:
            logger.error("No data available for Total Books per Author visualization.")
            return
        df['full_name'] = df['first'] + ' ' + df['surname']
        fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
        maximize_figure()
        ax.bar(df['full_name'], df['total_books'], color='skyblue')
        ax.set_xlabel('Author (First and Surname)', fontsize=13)
        ax.set_ylabel('Total Books', fontsize=13)
        ax.set_title('Total Books per Author', fontsize=15)
        plt.xticks(rotation=45, ha='right', fontsize=11)
        plt.yticks(fontsize=11)
        plt.tight_layout()
        plt.show(block=False)
        print("Press Spacebar or Enter in the figure window to continue...")
        plt.waitforbuttonpress()
        plt.close()
    except Exception as e:
        logger.error(f"Error during visualization (Total Books per Author): {e}")

def visualize_average_publication_year(connection) -> None:
    """
    Creates a simple visualization for the average publication year.
    It queries the average year from the books table and displays it as text.
    """
    try:
        query = "SELECT AVG(year_published) AS average_year_published FROM books"
        df = pd.read_sql_query(query, connection)
        if df.empty or df['average_year_published'].isnull().all():
            logger.error("No data available for Average Publication Year visualization.")
            return
        avg_year = df.iloc[0]['average_year_published']
        fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
        maximize_figure()
        ax.text(0.5, 0.5, f"Avg Publication Year: {avg_year:.0f}",
                fontsize=19, ha='center', va='center')
        ax.axis('off')
        plt.title('Average Publication Year', fontsize=19)
        plt.show(block=False)
        print("Press Spacebar or Enter in the figure window to continue...")
        plt.waitforbuttonpress()
        plt.close()
    except Exception as e:
        logger.error(f"Error during Average Publication Year visualization: {e}")

def main() -> None:
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
    
    # Load CSV data into the database.
    authors_csv = DATA_FOLDER.joinpath("authors.csv")
    books_csv = DATA_FOLDER.joinpath("books.csv")
    try:
        insert_data_from_csv(DB_PATH, authors_csv, books_csv)
    except Exception as e:
        logger.error(f"Failed to insert CSV data: {e}")
    
    # Execute data_addition.sql to update schema and insert pricing data.
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
    
    query_results = {}
    
    for qf in query_files:
        file_path = SQL_QUERIES_FOLDER.joinpath(qf)
        logger.info(f"Executing query file: {file_path}")
        results = execute_multiple_queries(connection, file_path)
        if results:
            print(f"\nResults for {qf}:")
            for stmt, df in results:
                print(f"\nStatement:\n{stmt}\n")
                print(df)
                display_dataframe_text(df, title=f"Results for {qf}\nQuery: {stmt[:50]}...")
            query_results[qf] = results
        else:
            logger.error(f"No results returned for {qf}")
            input("Press Enter to continue...")
    
    # Additional Visualizations:
    visualize_publication_year_histogram(connection)
    visualize_book_price_pie(connection)
    visualize_total_books_per_author(connection)
    visualize_average_publication_year(connection)
    
    connection.close()
    logger.info("Database connection closed.")

if __name__ == "__main__":
    main()
