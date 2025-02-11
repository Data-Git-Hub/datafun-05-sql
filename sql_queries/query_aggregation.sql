-- Count the total number of books
SELECT COUNT(*) AS total_books
FROM books;

-- Count the total number of authors
SELECT COUNT(*) AS total_authors
FROM authors;

-- Calculate the average publication year for all books
SELECT AVG(year_published) AS average_year_published
FROM books;