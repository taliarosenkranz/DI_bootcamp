--part 1

--1
CREATE TABLE customer (
	id integer primary key
	,first_name varchar(20)
	,last_name varchar(20) NOT NULL
);


CREATE TABLE customer_profile(
	id integer 
	,isLoggedIn boolean default false
	,customer_id integer 
	,constraint fk_customer_id
		foreign key(customer_id) 
		references customer(id)
		ON UPDATE CASCADE
        ON DELETE CASCADE
);

--2
INSERT into customer (id, first_name, lastname)
VALUES (1, 'John', 'Doe'), (2, 'Jerome', 'Lalu'), (3, 'Lea', 'Rive');

INSERT INTO customer_profile (isLoggedin)
SELECT TRUE as isLoggedin FROM customer_profile WHERE customer_id = 1
UNION ALL
SELECT False as isLoggedin FROM customer_profile WHERE customer_id = 2;

--4.1
select first_name
from customers 
where isLoggedIn = True

--4.2
select c.first_name, cp.isLoggedIn
from customers c
right join customer_profile cp
on c.customer_id = cp.customer_id

--4.3
select count(*)
from customer_profile
where isLoggedIn = False

--PART TWO
--1
CREATE TABLE Book(
	book_id SERIAL PRIMARY KEY
	, title varchar(50) NOT NULL
	, author varchar(20) NOT NULL);
--2
INSERT INTO Book (title, author)
VALUES ('Alice In Wonderland','Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee')

--3
CREATE TABLE Student (
	student_id SERIAL PRIMARY KEY
	, name varchar(20) NOT NULL UNIQUE
	, age integer
	, CHECK (age <= 15)
);

--4 
INSERT INTO Student (name, age)
VALUES ('John', 12)
,('Lera', 11)
,('Patrick', 10)
,('Bob', 14);


--5
CREATE TABLE Library (
    book_fk_id INTEGER,
    student_fk_id INTEGER,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id),
    FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    FOREIGN KEY (student_fk_id) REFERENCES Student(student_id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

--6 ?? NOT WORKING
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES
((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), 
 (SELECT student_id FROM Student WHERE name = 'John'), 
 '2022-02-15');

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES
((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), 
 (SELECT student_id FROM Student WHERE name = 'Bob'), 
 '2021-03-03');

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES
((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), 
 (SELECT student_id FROM Student WHERE name = 'Lera'), 
 '2021-05-23');

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES
((SELECT book_id FROM Book WHERE title = 'Harry Potter'), 
 (SELECT student_id FROM Student WHERE name = 'Bob'), 
 '2021-08-12');


--7 --ADD JOINS
select * from Library;
select name, title
from Student
join Book

select avg(age)
from student
where title = 'Alice in Wonderland';

delete from Student where name = 'Bob';


