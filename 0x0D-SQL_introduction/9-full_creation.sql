-- script that creates a second table and add multiple rows
CREATE IF NOT EXISTS  second_table (id int, name VARCHAR(256), score int);
INSERT INTO second_table (id, name, score) VALUES
(1, "John", 10),
(1, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8)
