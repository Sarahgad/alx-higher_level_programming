-- Score
ALTER TABLE second_table
ADD COLUMN number INT;


UPDATE second_table
SET number = (SELECT COUNT(score) FROM second_table);
