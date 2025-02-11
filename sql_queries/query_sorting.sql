-- Sort all books by the publication year in ascending order.
SELECT * 
FROM books
ORDER BY year_published ASC;

-- Sort all books by the book_price in descending order.
SELECT * 
FROM books
ORDER BY book_price DESC;

-- Sort authors alphabetically by surname.
SELECT * 
FROM authors
ORDER BY surname ASC;

-- Sort books alphabetically by title.
SELECT * 
FROM books
ORDER BY title ASC;

-- Sort books first by publication year (ascending) and then by title (ascending).
SELECT * 
FROM books
ORDER BY year_published ASC, title ASC;
