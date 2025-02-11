-- Group books by author.
-- For each author, count the number of books, and compute the average and total book price.
SELECT 
    a.author_id, 
    a.first, 
    a.surname,
    COUNT(b.book_id) AS total_books,
    AVG(b.book_price) AS avg_book_price,
    SUM(b.book_price) AS total_book_price
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
GROUP BY a.author_id, a.first, a.surname;

-- Group books by author.
-- For each author, count the number of books, and compute the average and total book price.
SELECT 
    a.author_id, 
    a.first, 
    a.surname,
    COUNT(b.book_id) AS total_books,
    AVG(b.book_price) AS avg_book_price,
    SUM(b.book_price) AS total_book_price
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
GROUP BY a.author_id, a.first, a.surname;

-- Group books by publication year.
-- This query counts the number of books published in each year and aggregates their pricing information.
SELECT 
    publication_year,
    COUNT(*) AS total_books,
    AVG(book_price) AS avg_book_price,
    SUM(book_price) AS total_book_price
FROM books
GROUP BY publication_year;

-- Group authors by the first letter of their surname. This query shows how many authors have surnames starting with the same letter.
SELECT 
    SUBSTR(surname, 1, 1) AS surname_initial,
    COUNT(*) AS num_authors
FROM authors
GROUP BY surname_initial;
