-- Database: public

-- DROP DATABASE IF EXISTS public;

CREATE DATABASE public
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE items(
	furniture_id serial,
	furniture varchar(50),
	price money);

CREATE TABLE customers(
	customer_id serial,
	first_name varchar(50),
	last_name varchar(50));

INSERT INTO items(furniture,price)
VALUES ('Small Desk',100)
	,('Large Desk',300)
	,('Fan',80);

INSERT INTO customers(first_name, last_name)
VALUES ('Greg', 'Jones')
	,('Sandra', 'Jones')
	,('Scott', 'Scott')
	,('Trevor', 'Green')
	,('Melanie', 'Johnson');

--All the items.
select * from items;

--All the items with a price above 80 (80 not included).
select * 
from items
where price > '$80';

--All the items with a price below 300. (300 included)
select * 
from items
where price <= '$300';

--All customers whose last name is ‘Smith’ (What will be your outcome?)
--empty table bc no customer with this name

select * from customers where last_name = 'Smith';

--All customers whose last name is ‘Jones’.
select * from customers 
where last_name = 'Jones';

--All customers whose firstname is not ‘Scott’.
select * from customers
where first_name <> 'Scott';