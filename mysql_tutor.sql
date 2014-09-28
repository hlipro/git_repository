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
-- constrains: NOT NULL; UNIQUE; PRIMARY KEY; FOREIGN KEY; CHECK; DEFAULT
-- data types: http://www.tutorialspoint.com/mysql/mysql-data-types.htm

CREATE TABLE usCustomers
(
PersonID int PRIMARY KEY,
LastName varchar(255) NOT NULL,
FirstName varchar(255) NOT NULL,
Country varchar(255) NOT NULL,
City varchar(255) DEFAULT NULL COMMENT 'primary mail address',
-- constraint uc_PersonID UNIQUE (PersonID, LastName)
-- UNIQUE (PersonID)
-- Primary key (PersonID)
CHECK (PersonID>0)
);
CREATE TABLE USCustomers
(
PersonID int NOT NULL PRIMARY KEY,
LastName varchar(255) NOT NULL,
FirstName varchar(255) NOT NULL,
Country varchar(255) NOT NULL,
City varchar(255) NOT NULL,
CHECK (PersonID>0)
);
CREATE TABLE Orders
(
OrdID int NOT NULL AUTO_INCREMENT, -- it automatically generates a value with increment 1 from previous record if a new row is inserted
CustomerID int,
Orderdate Date DEFAULT '2014-02-28', -- the default value must be a constant; it cannot be a function or an expression
-- constraint CID FOREIGN KEY (CustomerID) REFERENCES Customers (PersonID)
-- this works for creating foreign key with multiple columns
-- CHECK (OrdID>0 and CustomerID>0) -- mysql doesn't have check!!
PRIMARY KEY (OrdID),
CONSTRAINT fk_customer FOREIGN KEY (CustomerID) REFERENCES Customers(PersonID) ON DELETE Cascade
-- foreign key options:
-- ON UPDATE/DELETE CASCADE : if update/delete parent columns, update/delete child foreign key columns
-- ON UPDATE/DELETE SET NULL : if ..., set child fk columns to null
-- ON UPDATE/DELETE RESTRICT : cannot update/delete parent refered columns
-- ON UPDATE/DELETE NO ACTION : same as restrict
-- ON UPDATE/DELETE SET DEFAULT : if..., set child fk columns to default
) ENGINE=INNODB;

-- Alter table ...
-- ALTER TABLE Customers
-- ADD column_name datatype
-- MODIFY COLUMN column_name datatype
-- ADD UNIQUE (PersonID)
-- ADD CHECK (PersonID>0)
-- ALTER City SET DEFAULT 'BOSTON'
-- ADD FOREIGN KEY (CustomerID) REFERENCES Customers (PersonID)
-- ADD CONSTRAINT chk_Person CHECK (P_Id>0 AND City='Sandnes') -- not for mysql
-- ADD CONSTRAINT pk_PersonID PRIMARY KEY (PersonID,LastName)
-- ADD CONSTRAINT uc_PersonID UNIQUE (P_Id,LastName)
-- ADD CONSTRAINT fk_PerOrders FOREIGN KEY (col1 col2) REFERENCES Persons(col1 col2)
-- Drop COLUMN column_name
-- Drop INDEX uc_PersonID -- for unique key 
-- ALTER City Drop DEFAULT
-- Drop primary key
-- Drop CHECK chk_Person 
-- DROP FOREIGN KEY fk_PerOrders

-- CREATE INDEX allow the database application to find data fast;
-- CREATE INDEX index_name
-- ON table_name (column_name)
-- Or create a unique index
-- CREATE UNIQUE INDEX index_name
-- ON table_name (column_name)
CREATE INDEX Pindex 
ON Customers (LastName, FirstName);
-- Drop
DROP INDEX Customers.Pindex;
-- Or
-- ALTER TABLE Customers DROP INDEX Pindex;

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

-- don't need to specify ordID since it has auto-increment
-- ALTER TABLE orders AUTO_INCREMENT=100
INSERT INTO Orders (CustomerID,Orderdate)
VALUES (12250,last_day('2011-11-01'));
INSERT INTO Orders (CustomerID,Orderdate)
VALUES (12346,'2013-05-31'+INTERVAL 0 DAY);
INSERT INTO Orders (CustomerID,Orderdate)
VALUES (12348,last_day('2014-02-28'));
INSERT INTO Orders (CustomerID,Orderdate)
VALUES (12349,last_day('2014-02-13'));
INSERT INTO Orders (CustomerID,Orderdate)
VALUES (12348,last_day('2014-01-01'));

-- SELECT - extracts data from a database
-- SELECT column_name,column_name
-- FROM table_name;
select * from Customers;

-- DISTINCT keyword can be used to return only distinct (different) values.
SELECT DISTINCT City FROM Customers;

-- Last_day(), +INTERVAL 0 DAY, +INTERVAL 0 MONTH to avoid datatime error
SELECT LAST_DAY('2008-02-31') as my_day;
SELECT '2008-02-31'+INTERVAL 0 day;

-- WHERE clause is used to extract only those records that fulfill a specified criterion.
-- SELECT column_name,column_name
-- FROM table_name
-- WHERE column_name operator value;
SELECT LastName, FirstName FROM Customers
WHERE Country='US';

-- Operator	Description:
-- BETWEEN ... AND ...	Check whether a value is within a range of values
-- COALESCE()	Return the first non-NULL argument
-- <=>	NULL-safe equal to operator
-- =	Equal operator
-- >=	Greater than or equal operator
-- >	Greater than operator
-- GREATEST()	Return the largest argument
-- IN()	Check whether a value is within a set of values
-- INTERVAL()	Return the index of the argument that is less than the first argument
-- IS NOT NULL	NOT NULL value test
-- IS NOT	Test a value against a boolean
-- IS NULL	NULL value test
-- IS	Test a value against a boolean
-- ISNULL()	Test whether the argument is NULL
-- LEAST()	Return the smallest argument
-- <=	Less than or equal operator
-- <	Less than operator
-- LIKE	Simple pattern matching
-- NOT BETWEEN ... AND ...	Check whether a value is not within a range of values
-- !=, <>	Not equal operator
-- NOT IN()	Check whether a value is not within a set of values
-- NOT LIKE	Negation of simple pattern matching
-- STRCMP()	Compare two strings

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

-- SELECT INTO - output to OUTFILE 'filename' / DUMPFILE 'filename' /var_name 

-- Alias: AS, can be omitted
-- use func Concat_ws to concat columns
SELECT Concat_ws(',',LastName,FirstName) as 'Full Name' FROM Customers;
-- alias the tables to simplify codes:
-- SELECT o.OrderID, o.OrderDate, c.CustomerName
-- FROM Customers AS c, Orders AS o
-- WHERE c.CustomerName="Around the Horn" AND c.CustomerID=o.CustomerID;

-- Duplicate/copy table:
-- CREATE TABLE name SELECT ... if table doesn't exist
CREATE TABLE USCustomers SELECT * FROM Customers WHERE country='US';
-- INSERT INTO table SELECT columns from table1 where ... if table exists
-- INSERT INTO table2
-- (column_name(s))
-- SELECT column_name(s)
-- FROM table1;
INSERT INTO USCustomers SELECT * FROM Customers where Country='Spain';

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
DELETE FROM Customers WHERE City='Miami';
-- DELETE * FROM Customers; or DELETE FROM Customers; careful !!!

-- JOIN - combine rows from two or more tables
-- INNER JOIN: Returns all rows when there is at least one match in BOTH tables
SELECT o.OrdID,c.PersonID,o.OrderDate
from Orders as o INNER JOIN Customers as c
ON o.CustomerID=c.PersonID;
-- LEFT JOIN: Return all rows from the left table, and the matched rows from the right table
SELECT o.OrdID,c.PersonID,o.OrderDate
from Orders as o LEFT JOIN Customers as c
ON o.CustomerID=c.PersonID;
-- RIGHT JOIN: Return all rows from the right table, and the matched rows from the left table
SELECT c.LastName,c.FirstName,c.PersonID,o.OrderDate
from Orders as o RIGHT JOIN Customers as c
ON o.CustomerID=c.PersonID;
-- FULL OUTER JOIN: Return all rows when there is a match in ONE of the tables
-- No full outer join in mysql, use union !!!
SELECT o.OrdID,c.PersonID,o.OrderDate
from Orders as o LEFT JOIN Customers as c
ON o.CustomerID=c.PersonID
union
SELECT o.OrdID,c.PersonID,o.OrderDate
from Orders as o RIGHT JOIN Customers as c
ON o.CustomerID=c.PersonID;

-- UNION - ombine the result-set of two or more SELECT statements
-- Notice that each SELECT statement within the UNION must have the same number of columns. The columns must also have similar data types. Also, the columns in each SELECT statement must be in the same order.
SELECT CustomerID from Orders
where Orderdate>'2012-01-01'
union
SELECT PersonID from Customers
where country='US';
-- The UNION operator selects only distinct values by default. To allow duplicate values, use the ALL keyword with UNION.
SELECT CustomerID from Orders 
union all
SELECT PersonID from Customers;

-- View - virtual table based on the result-set of an SQL statement
-- CREATE
--     [OR REPLACE]
--     [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
--     [DEFINER = { user | CURRENT_USER }]
--     [SQL SECURITY { DEFINER | INVOKER }]
--     VIEW view_name [(column_list)]
--     AS select_statement
--     [WITH [CASCADED | LOCAL] CHECK OPTION]
CREATE VIEW Current_Customer (ID, Name) AS
SELECT o.CustomerID , Concat_ws(',',c.LastName,c.FirstName)
FROM Orders as o 
INNER JOIN Customers as c
ON o.Orderdate>='2014-01-01' and o.CustomerID=c.PersonID;
-- Replace view
CREATE OR REPLACE VIEW Current_Customer AS
SELECT o.CustomerID as ID, Concat_ws(',',c.LastName,c.FirstName) as name,o.OrderDate as OrderDate
FROM Orders as o 
INNER JOIN Customers as c
ON o.Orderdate>='2014-01-01' and o.CustomerID=c.PersonID;
-- Drop view
Drop view Current_Customer

-- MySQL comes with the following data types for storing a date or a date/time value in the database:
-- DATE - format YYYY-MM-DD
-- DATETIME - format: YYYY-MM-DD HH:MM:SS
-- TIMESTAMP - format: YYYY-MM-DD HH:MM:SS
-- YEAR - format YYYY or YY
-- -------------------------------------------------------
-- MySQL Date Functions
-- Function	Description
-- NOW()	Returns the current date and time
-- CURDATE()	Returns the current date
-- CURTIME()	Returns the current time
-- DATE()	Extracts the date part of a date or date/time expression
-- EXTRACT()	Returns a single part of a date/time
-- DATE_ADD()	Adds a specified time interval to a date
-- DATE_SUB()	Subtracts a specified time interval from a date
-- DATEDIFF()	Returns the number of days between two dates
-- DATE_FORMAT()	Displays date/time data in different formats
-- http://www.tutorialspoint.com/mysql/mysql-date-time-functions.htm

-- IS NULL OPTIMIZATION
SELECT * FROM Customers WHERE Customers.LastName REGEXP '^[JL].*$' or Customers.LastName is NULL;
SELECT * FROM Customers WHERE Customers.LastName REGEXP '^[JL].*$' or Customers.LastName <=> NULL;
-- USE IFNULL(), COALESCE() (Return the first non-NULL argument) to convert NULL to 0
-- SELECT ProductName,UnitPrice*(UnitsInStock+IFNULL(UnitsOnOrder,0)) FROM Products;
-- SELECT ProductName,UnitPrice*(UnitsInStock+COALESCE(UnitsOnOrder,0)) FROM Products;

-- MYSQL aggregate functions
-- GROUP BY : aggregate counts by columns
SELECT Concat_ws(',',c.LastName,c.FirstName) as Name,Count(*)
FROM Orders as o INNER JOIN Customers as c
ON o.CustomerID=c.PersonID
GROUP BY Name;

-- max(column) , min(column), avg(column), sum(column)
SELECT max(PersonID) FROM Customers;
-- combine max(),min(), avg(), sum() and group by to find max/min value for each name
SELECT Concat_ws(',',c.LastName,c.FirstName) as Name,max(o.OrderDate) as 'Recent Visit'
FROM Orders as o INNER JOIN Customers as c
ON o.CustomerID=c.PersonID
GROUP BY Name;

-- SQRT()		square root
-- RAND(SEED)	random number between 0 and 1; use ORDER BY RAND() to randomize orders
SELECT * FROM Customers ORDER BY RAND();
-- CONCAT(col1,col2...)	concatenate columns/strings
-- numerical functions : http://www.tutorialspoint.com/mysql/mysql-numeric-functions.htm
-- string functions: http://www.tutorialspoint.com/mysql/mysql-string-functions.htm

-- delete and drop
Truncate TABLE Customers; -- empty a table
DELETE FROM Customers;
Drop table if exists Customers;
Drop table USCustomers;
Drop user testuser;
Drop database test1;
