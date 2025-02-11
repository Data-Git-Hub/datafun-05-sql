INSERT INTO authors (author_id, first, surname) VALUES
    ('AUTHOR_001', 'J.K.', 'Rowling'),
    ('AUTHOR_002', 'George', 'Orwell'),
    ('AUTHOR_003', 'Harper', 'Lee');


-- Insert records into the books table
-- And include foreign key references to the authors table
INSERT INTO books (book_id, title, genre, publication_year, author_id) VALUES
    ('BOOK_001', 'Harry Potter and the Sorcerer''s Stone', 'Fantasy', 1997, 'AUTHOR_001'),
    ('BOOK_002', 'Harry Potter and the Chamber of Secrets', 'Fantasy', 1998, 'AUTHOR_001'),
    ('BOOK_003', '1984', 'Dystopian', 1949, 'AUTHOR_002'),
    ('BOOK_004', 'Animal Farm', 'Political Satire', 1945, 'AUTHOR_002'),
    ('BOOK_005', 'To Kill a Mockingbird', 'Fiction', 1960, 'AUTHOR_003');