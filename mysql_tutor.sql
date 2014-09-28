-- type in shell -> enter mysql API
mysql -u root -p
-- now in mysql:

-- current_user is root
SELECT CURRENT_USER();

CREATE DATABASE test1;

-- change to test1
USE test1;

SHOW GRANTS FOR 'root'@'localhost';
SHOW GRANTS FOR CURRENT_USER();

CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'mypass';
GRANT ALL ON test1 TO 'testuser'@'localhost';
-- SET PASSWORD FOR 'jeffrey'@'localhost' = PASSWORD('cleartext password');

-- SHOW
SHOW databases;
SHOW tables;

-- CREATE TABLE table_name
-- (
-- column_name1 data_type(size),
-- column_name2 data_type(size),
-- column_name3 data_type(size),
-- ....
-- );
CREATE TABLE Customers
(
PersonID int NOT NULL PRIMARY KEY,
LastName varchar(255) NOT NULL,
FirstName varchar(255) NOT NULL,
Country varchar(255) NOT NULL,
City varchar(255) NOT NULL
);

-- INSERT INTO statement is used to insert new records in a table.
-- INSERT INTO table_name
-- VALUES (value1,value2,value3,...);
-- or
-- INSERT INTO table_name (column1,column2,column3,...)
-- VALUES (value1,value2,value3,...);
-- can insert partial data if rest parts can be null !!!
INSERT INTO Customers 
VALUES (12345,'Li','Hao','US','Boston');
INSERT INTO Customers (PersonID,LastName,FirstName,Country,City)
VALUES (12346,'Jordan','Michael','US','Chicago');
INSERT INTO Customers
VALUES (12347,'Rose','Derrick','US','Chicago');
INSERT INTO Customers (PersonID,LastName,FirstName,Country,City)
VALUES (12348,'Messi','Lionel','Spain','Barcelona');
INSERT INTO Customers
VALUES (12349,'Ronaldo','Cristiano','Spain','Madrid');
INSERT INTO Customers (PersonID,LastName,FirstName,City,Country)
VALUES (12350,'Bryant','Kobe','Los Angeles','US');
INSERT INTO Customers
VALUES (12250,'James','LeBron','US','Miami');

-- SELECT - extracts data from a database
-- SELECT column_name,column_name
-- FROM table_name;
select * from Customers;

-- DISTINCT keyword can be used to return only distinct (different) values.
SELECT DISTINCT City FROM Customers;

-- WHERE clause is used to extract only those records that fulfill a specified criterion.
-- SELECT column_name,column_name
-- FROM table_name
-- WHERE column_name operator value;
SELECT LastName, FirstName FROM Customers
WHERE Country='US';
-- Operator	Description in WHERE
-- =	Equal
-- <>	Not equal. Note: In some versions of SQL this operator may be written as !=
-- >	Greater than
-- <	Less than
-- >=	Greater than or equal
-- <=	Less than or equal
-- BETWEEN	Between an inclusive range
-- LIKE	Search for a pattern
-- IN	To specify multiple possible values for a column

-- AND OR
SELECT * FROM Customers
WHERE Country='Spain'
AND (City='Barcelona' OR City='Madrid');

-- LIKE, NOT LIKE: use WILDCARDS %, _
SELECT * FROM Customers
WHERE City LIKE '%ver%';
SELECT * FROM Customers
WHERE Country NOT LIKE '%S';
SELECT * FROM Customers
WHERE Country LIKE '__';
-- Wildcard	Description
-- %	A substitute for zero or more characters
-- _	A substitute for a single character
-- \%, \_ for conversion to special char

-- REGEXP, NOT REGEXP, RLIKE: use regular expression syntax
SELECT * FROM Customers
WHERE LastName REGEXP '^[ASCDJ].*$'; -- country start with []
SELECT * FROM Customers
WHERE LastName REGEXP '[^J]*' and Country REGEXP '.{5}'; -- LastName not starting with J and Country has five chars
-- '.' any single char
-- [charlist]	Sets and ranges of characters to match: [abc],[a-c],[0-9]
--  * any number of chars
-- ^,$ start, end

-- IN (value1,value2,...)
SELECT * FROM Customers
WHERE City IN ('Madrid','Chicago'); 

-- BETWEEN value1 and value2; NOT BETWEEN ...
-- does not include value2 !!!
SELECT * FROM Customers
WHERE City BETWEEN 'C' and 'M'; 

-- ORDER BY keyword sorts the records in ascending order by default. To sort the records in a descending order, you can use the DESC keyword.
-- SELECT column_name,column_name
-- FROM table_name
-- ORDER BY column_name,column_name ASC|DESC;
SELECT LastName,FirstName
FROM Customers 
WHERE City='Chicago'
ORDER BY LastName, PersonID DESC;

-- LIMIT number
SELECT * from Customers
-- WHERE
-- ORDER BY
LIMIT 2;

-- Alias: AS, can be omitted
-- use func Concat_ws to concat columns
SELECT Concat_ws(',',LastName,FirstName) as 'Full Name' FROM Customers;




-- UPDATE - updates data in a database; must use WHERE !!!!!!!!
-- UPDATE table_name
-- SET column1=value1,column2=value2,...
-- WHERE some_column=some_value;
UPDATE Customers
SET City='Cleverland'
WHERE LastName='James' and FirstName='LeBron';

-- DELETE - deletes data from a database
-- DELETE FROM table_name
-- WHERE some_column=some_value;
DELETE FROM Customers
WHERE City='Miami';
-- DELETE * FROM Customers; or DELETE FROM Customers;




-- CREATE DATABASE - creates a new database
-- ALTER DATABASE - modifies a database
-- CREATE TABLE - creates a new table
-- ALTER TABLE - modifies a table
-- DROP TABLE - deletes a table
-- CREATE INDEX - creates an index (search key)
-- DROP INDEX - deletes an index


DELETE FROM Customers;
Drop table Customers;
Drop user testuser;
Drop database test1;
