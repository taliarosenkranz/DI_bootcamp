create table students(
	id serial,
	first_name varchar(50),
	last_name varchar(50),
	birth_date date
);

INSERT INTO students (first_name, last_name, birth_date) VALUES 
('Marc', 'Benichou', '1998-02-11'),
('Yoan', 'Cohen', '2010-03-12'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-03-10');


--Fetch all of the data from the table.
select * from students;
-- Fetch all of the students first_names and last_names.
select first_name, last_name from students;
-- For the following questions, only fetch the first_names and last_names of the students.
-- Fetch the student which id is equal to 2.
-- Fetch the student whose last_name is Benichou AND first_name is Marc.
select first_name, last_name from students
where last_name = 'Benichou' AND first_name = 'Marc';
-- Fetch the students whose last_names are Benichou OR first_names are Marc.
select first_name, last_name from students
where last_name = 'Benichou' OR first_name = 'Marc';
--Fetch the students whose first_names contain the letter a.
select first_name, last_name from students
where first_name LIKE '%a%';
-- Fetch the students whose first_names start with the letter a.
select first_name, last_name from students
where first_name LIKE 'A%';
-- Fetch the students whose first_names end with the letter a.
select first_name, last_name from students
where first_name LIKE '%a';
-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
select first_name, last_name from students
where first_name LIKE '%a_';
--Fetch the students whose id’s are equal to 1 AND 3 .
select first_name, last_name, from students
where id = 1 
OR id = 3;
--Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
select * from students
where birth_date >= '1/01/2000'