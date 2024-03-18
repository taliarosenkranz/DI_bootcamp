--EXERCISE 1:
--All items, ordered by price (lowest to highest).
SELECT * 
FROM items
ORDER BY price ASC;

--Items with a price above 80 (80 included), ordered by price (highest to lowest).
SELECT *
FROM items
WHERE price >= '80'
ORDER BY price DESC;

--The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
SELECT first_name, last_name 
FROM customers
ORDER BY first_name ASC
LIMIT 3;

--All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT last_name
FROM customers
ORDER BY last_name DESC;



--EXERCISE 2:

SELECT * 
FROM customer;

select CONCAT(first_name, ' ' , last_name) as full_name
from customer;

select DISTINCT create_date
from customer;

select * 
from customer
order by first_name desc;

select film_id, title, description, release_year, rental_rate
from film
order by rental_rate asc;

select address, phone
from address
where district = 'Texas';

select *
from film
where film_id = 15 
OR film_id = 150;

select film_id, title, description, length, rental_rate
from film
where title = 'Pretty Woman';

select film_id, title, description, length, rental_rate
from film
where title LIKE 'Pr%';

select film_id, title, rental_rate 
from film
order by rental_rate asc
limit 10;

SELECT film_id, title, rental_rate 
FROM film
WHERE film_id NOT IN (
    SELECT film_id 
    FROM film
    ORDER BY rental_rate ASC
    LIMIT 10
)
ORDER BY rental_rate ASC
LIMIT 10;

SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

select f.*
from film f
left join inventory i
on f.film_id = i.film_id
where i.film_id IS NULL;

select ci.city_id, ci.city, co.country
from city ci
left join country co
on ci.country_id = co.country_id;

select c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, s.staff_id
from customer c
left join payment p
on c.customer_id = p.customer_id
left join staff s
on p.staff_id = s.staff_id
order by s.staff_id;


