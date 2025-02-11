-- query_join.sql

-- Query 1: INNER JOIN
-- Display each book with its publication details and the full name of its author.
SELECT 
    b.book_id, 
    b.title, 
    b.publication_year, 
    b.book_price,
    a.first || ' ' || a.surname AS author_full_name
FROM books b
INNER JOIN authors a ON b.author_id = a.author_id;

-- Query 2: LEFT JOIN
-- List all authors, along with any books they have written.
-- Authors without books will still appear (with NULL values for book details).
SELECT 
    a.author_id, 
    a.first, 
    a.surname,
    b.book_id,
    b.title,
    b.publication_year,
    b.book_price
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
ORDER BY a.surname;

-- Note on RIGHT JOIN:
-- SQLite does not support RIGHT JOIN directly.

SELECT 
    b.book_id, 
    b.title, 
    b.publication_year, 
    b.book_price,
    a.first || ' ' || a.surname AS author_full_name
FROM books b
LEFT JOIN authors a ON b.author_id = a.author_id;
