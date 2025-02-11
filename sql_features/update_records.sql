-- update_records.sql
-- Update Harper Lee's last name by appending " (Updated)"
UPDATE authors
SET last = last || ' (Updated)'
WHERE author_id = 'AUTHOR_003';

-- Update the title of "1984" to indicate a revised edition
UPDATE books
SET title = '1984 (Revised Edition)'
WHERE book_id = 'BOOK_003';

