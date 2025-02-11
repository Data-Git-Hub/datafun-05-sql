-- query_filters.sql

-- Select all books published after 1950.
SELECT *
FROM books
WHERE year_published > 1950;

-- Select all authors whose surname is exactly 'Orwell'.
SELECT *
FROM authors
WHERE surname = 'Orwell';

-- Select books with a book_price greater than 15.00.
SELECT *
FROM books
WHERE book_price > 15.00;
