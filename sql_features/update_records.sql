-- update_records.sql
-- Update Harper Lee's last name by appending " (Updated)"
UPDATE authors
SET last = last || ' (Updated)'
WHERE author_id = '10f88232-1ae7-4d88-a6a2-dfcebb22a596';

-- Update the title of "1984" to indicate a revised edition
UPDATE books
SET title = '1984 (Revised Edition)'
WHERE book_id = '0f5f44f7-44d8-4f49-b8c4-c64d847587d3';

