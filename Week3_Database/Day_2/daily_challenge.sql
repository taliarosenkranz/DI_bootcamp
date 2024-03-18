CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);

SELECT * FROM SecondTab;

--Q1: number of rows - 0 (both have null ids but computer does not understand them both as the same value)

--Q2: number of rows - 2 (counting rows with id 6 and id 7. excludinf id 5 and null)

--Q3: number of rows - 0 (why not 2? we have 2 values in first tab that are not in secondtab)

--Q4: number of rows - 2 (row with id 5 and null are not counted leaving id 6 and id 7)
   