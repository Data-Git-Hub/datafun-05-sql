import sqlite3
import pathlib

DB_PATH = pathlib.Path("data/db.sqlite")
conn = sqlite3.connect(DB_PATH)
print("Authors:")
for row in conn.execute("SELECT * FROM authors;").fetchall():
    print(row)
print("\nBooks:")
for row in conn.execute("SELECT * FROM books;").fetchall():
    print(row)
conn.close()

print()
print("*******************************************************") 
print()

DB_PATH = pathlib.Path("project.db")
conn = sqlite3.connect(DB_PATH)
print("Authors:")
for row in conn.execute("SELECT * FROM authors;").fetchall():
    print(row)
print("\nBooks:")
for row in conn.execute("SELECT * FROM books;").fetchall():
    print(row)
conn.close()