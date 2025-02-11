-- query_filters.sql

-- Select all books published after 1950.
SELECT * 
FROM books
WHERE year_published > 1950;

-- Select all authors whose surname is exactly 'Orwell'.
SELECT * 
FROM authors
WHERE surname = 'Orwell';

-- Select all books with a book_price greater than 15.00.
SELECT * 
FROM books
WHERE book_price > 15.00;

-- Select details of books by authors with the surname 'Rowling'.
SELECT 
    b.book_id, 
    b.title, 
    b.year_published, 
    b.book_price, 
    a.first, 
    a.surname
FROM books b
JOIN authors a ON b.author_id = a.author_id
WHERE a.surname = 'Rowling';

-- Select books published between 1930 and 2000 that have a price below 20.00.
SELECT *
FROM books
WHERE year_published BETWEEN 1930 AND 2000
  AND book_price < 20.00;

-- Select authors whose surname starts with the letter 'R'.
SELECT *
FROM authors
WHERE surname LIKE 'R%';
