-- Insert records into the books table to give more data to work with to make the outputs more interesting
-- Alter the books table to add a new column for book price.
ALTER TABLE books ADD COLUMN book_price REAL;

-- Update the new column using a CASE statement.
UPDATE books
SET book_price = 
    CASE book_id
        WHEN 'BOOK_001' THEN 12.99
        WHEN 'BOOK_002' THEN 13.99
        WHEN 'BOOK_003' THEN 12.99
        WHEN 'BOOK_004' THEN 9.99
        WHEN 'BOOK_005' THEN 14.50
        WHEN 'BOOK_006' THEN 10.00
        WHEN 'BOOK_007' THEN 11.50
        WHEN 'BOOK_008' THEN 9.99
        WHEN 'BOOK_009' THEN 15.75
        WHEN 'BOOK_010' THEN 8.50
        WHEN 'BOOK_011' THEN 16.25
        WHEN 'BOOK_012' THEN 22.00
        WHEN 'BOOK_013' THEN 18.99
        ELSE 0.0
    END;