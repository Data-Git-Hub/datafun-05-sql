-- update_records.sql
-- Update Harper Lee's name by appending " (Updated)"
UPDATE authors
SET name = name || ' (Updated)'
WHERE author_id = 'AUTHOR_003';

-- Update the title of "Animal Farm" to indicate a revised edition
UPDATE books
SET title = 'Animal Farm (Revised Edition)'
WHERE book_id = 'BOOK_004';
