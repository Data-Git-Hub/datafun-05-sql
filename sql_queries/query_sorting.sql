-- query_sorting.sql

-- 1. Sort all books by the publication year in ascending order.
SELECT * 
FROM books
ORDER BY publication_year ASC;

-- 2. Sort all books by the book_price in descending order.
SELECT * 
FROM books
ORDER BY book_price DESC;

-- 3. Sort authors alphabetically by surname.
SELECT * 
FROM authors
ORDER BY surname ASC;

-- 4. Sort books alphabetically by title.
SELECT * 
FROM books
ORDER BY title ASC;

-- 5. Sort books first by publication year (ascending) and then by title (ascending).
SELECT * 
FROM books
ORDER BY publication_year ASC, title ASC;
