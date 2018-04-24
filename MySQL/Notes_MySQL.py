make the table name plural and ALL lowercase - make it plural (ex. users, leads, sites, clients, chapters, courses, modules)
use "id" as the primary key - name it id (also make it auto-incremented).
name foreign keys with singular_table_name_id when referencing to a primary key in another table name it [singular name of the table you're referring to]_id (ex. user_id, lead_id, site_id, client_id, chapter_id, course_id, module_id).
use created_at and updated_at as columns for the timestamp in EVERY table you create.


for SQL

 C:\MySQL\MySQLServer\my.cnf

NET STOP MYSQL
NET START MYSQL

for deleting stuff in database

SET SQL_SAFE_UPDATES = 0;

SELECT * 
FROM users
WHERE first_name LIKE "K%";

INSERT INTO table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value');

UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)

DELETE FROM table_name WHERE condition(s)

------
Text Functions Data Types (VARCHAR, TEXT, CHAR etc.)

Numeric Functions Data Types (INT, BIGINT, FLOAT etc.)

Date and Time Functions Data Types (DATETIME)

SELECT FUNCTION (column) FROM table_name

------
Joining Table 

SELECT * FROM customers 
JOIN addresses ON addresses.id = customers.address_id;

many to many Joining

SELECT * FROM orders 
JOIN items_orders ON orders.id = items_orders.order_id 
JOIN items ON items.id = items_orders.item_id;

LEFT JOIN   #  IS SHOW ALL RECORD
JOIN        #  SHOW ALL RECORD EXCEPT FOR EMPTY








