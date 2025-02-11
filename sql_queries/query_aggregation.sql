-- Count the total number of books
SELECT COUNT(*) AS total_books
FROM books;

-- Count the total number of authors
SELECT COUNT(*) AS total_authors
FROM authors;

-- Calculate the average publication year for all books
SELECT AVG(year_published) AS average_year_published
FROM books;

-- Calculate the total sum of book prices for all books
SELECT SUM(book_price) AS total_book_value
FROM books;

-- Calculate the average book price across all books
SELECT AVG(book_price) AS average_book_price
FROM books;

-- Sum the total price of books per author for authors who have more than one book.
SELECT 
    a.author_id,
    a.first,
    a.surname,
    COUNT(b.book_id) AS book_count,
    SUM(b.book_price) AS total_price,
    AVG(b.book_price) AS average_price
FROM authors a
JOIN books b ON a.author_id = b.author_id
GROUP BY a.author_id, a.first, a.surname
HAVING COUNT(b.book_id) > 1;
