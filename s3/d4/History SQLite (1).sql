--- 09-11-2023 10:48:25
--- SQLite
CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(20)
);

INSERT INTO Customers (id, name, email, address, phone_number)
VALUES
    (1, 'Customer1', 'customer1@email.com', 'Address1', '123-456-7890'),
    (2, 'Customer2', 'customer2@email.com', 'Address2', '987-654-3210'),
    (3, 'Customer3', 'customer3@email.com', 'Address3', '555-555-5555'),
    (4, 'Customer4', 'customer4@email.com', 'Address4', '777-777-7777'),
    (5, 'Customer5', 'customer5@email.com', 'Address5', '999-999-9999');

SELECT * FROM Customers;

--- 09-11-2023 10:48:48
--- SQLite
/***** ERROR ******
table Customers already exists
 ----- 
CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(20)
);

INSERT INTO Customers (id, name, email, address, phone_number)
VALUES
    (1, 'Customer1', 'customer1@email.com', 'Address1', '123-456-7890'),
    (2, 'Customer2', 'customer2@email.com', 'Address2', '987-654-3210'),
    (3, 'Customer3', 'customer3@email.com', 'Address3', '555-555-5555'),
    (4, 'Customer4', 'customer4@email.com', 'Address4', '777-777-7777'),
    (5, 'Customer5', 'customer5@email.com', 'Address5', '999-999-9999');

SELECT * FROM Customers;
SELECT name, email FROM Customers;
*****/

--- 09-11-2023 10:49:59
--- SQLite

SELECT name, email FROM Customers;

--- 09-11-2023 10:50:18
--- SQLite

SELECT * FROM Customers WHERE id = 3;

--- 09-11-2023 10:50:33
--- SQLite
SELECT * FROM Customers WHERE name LIKE 'A%';

--- 09-11-2023 10:50:58
--- SQLite
SELECT * FROM Customers ORDER BY name DESC;

--- 09-11-2023 10:52:28
--- SQLite
UPDATE Customers SET address = 'New Address' WHERE id = 4;

--- 09-11-2023 10:52:49
--- SQLite
SELECT * FROM Customers ORDER BY id ASC LIMIT 3;

--- 09-11-2023 10:53:05
--- SQLite
DELETE FROM Customers WHERE id = 2;

--- 09-11-2023 10:53:14
--- SQLite
SELECT COUNT(*) FROM Customers;

--- 09-11-2023 10:53:25
--- SQLite
/***** ERROR ******
near "OFFSET": syntax error
 ----- 
SELECT * FROM Customers ORDER BY id ASC OFFSET 2;
*****/

--- 09-11-2023 10:54:42
--- SQLite
/***** ERROR ******
near "OFFSET": syntax error
 ----- 
SELECT * FROM Customers ORDER BY id ASC OFFSET 2 ROWS;
*****/

--- 09-11-2023 11:25:17
--- SQLite
SELECT * FROM Customers ;

--- 09-11-2023 11:25:39
--- SQLite
/***** ERROR ******
near "OFFSET": syntax error
 ----- 
SELECT * FROM Customers ORDER BY name ASC OFFSET 2 ROWS;
*****/

--- 09-11-2023 11:26:26
--- SQLite
SELECT * FROM Customers WHERE id > 2 AND name LIKE 'C%';

--- 09-11-2023 11:26:39
--- SQLite
SELECT * FROM Customers WHERE id < 3 OR name LIKE '%s';

--- 09-11-2023 11:26:50
--- SQLite
SELECT * FROM Customers WHERE phone_number IS NULL OR phone_number = '';

