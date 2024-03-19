-- Exercise 1: DVD Rental

-- 1
select name
from language;


-- 2
select f.title, f.description, l.name
from film f 
join language l
on f.language_id = l.language_id

--3
select f.title, f.description, l.name
from film f 
right join language l
on f.language_id = l.language_id

--4
create table new_film (
	id serial, 
	name varchar(50);

insert into new_film (name)
	values ('pretty woman'), ('Lion King');

select * from new_film;

--5
ALTER TABLE new_film ADD PRIMARY KEY (id);


CREATE TABLE customer_review (
	review_id serial PRIMARY KEY,
	film_id integer,
	language_id integer,
	title varchar(50),
	score integer,
	review_text text,
	last_update date,
	CONSTRAINT fk_film_id
		FOREIGN KEY (film_id)
		REFERENCES new_film(id)
		ON UPDATE CASCADE
        ON DELETE CASCADE, 
	CONSTRAINT fk_language
        FOREIGN KEY (language_id)
        REFERENCES language(language_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL 
);

--6
insert into customer_review (film_id, language_id, title, score, review_text,last_update)
	values (1,1,'Pretty Woman','10','Lorem Ipsum Description','03.19.2024'),
		   (2,1,'Lion King','7','Lorem Ipsum Different Description','03.19.2024');
	
select * from customer_review

--7 The row containing the movie with name lion king should also be removed from customer reviews when deleted from new_films
select * from new_film
delete from new_film where name = 'Lion King';
select * from customer_review;


--Exercise 2 : DVD Rental

--1
select * from film
select * from language
	
update film 
set language_id = 2
where title = 'Chamber Italian';

update film 
set language_id = 3
where title = 'Airport Pollock';

--2
--customer_id and address_id are foreign keys for three other tables (rental, payment & address). 
--When inserting in to customer table we influence the referenced tables as a new customer_id and address_id will also be added to those tables

--3 
Drop table if exists customer_review;
-- works easily to drop table bc it is not referenced by a table meaning if new_film would be droped then this would effect reviews table but not other way arround. It did reference two tables but they are not afected 

--4
select count(*) outstanding_rentals from rental
where return_date is null

--5 Find the 30 most expensive movies which are outstanding 
select r.return_date, i.film_id, f.rental_rate
from rental r
left join inventory i
	on r.inventory_id = i.inventory_id
left join film f
	on i.film_id = f.film_id
where return_date is null
order by rental_rate desc
limit 30;
	
	
--6.1
select f.film_id, f.title, f.description, a.first_name, a.last_name
from film f
left join film_actor fa
on f.film_id = fa.film_id
left join actor a
on fa.actor_id = a.actor_id
where 1 = 1
AND f.description LIKE '%Sumo Wrestler%'
AND a.first_name = 'Penelope'
AND a.last_name = 'Monroe';

--6.2
select f.title, f.length, f.rating, c.name
from film f
left join film_category fc
	on f.film_id = fc.film_id
left join category c
	on fc.category_id = c.category_id
where 1 = 1
and c.name = 'Documentary'
and length < 60
and rating = 'R';

--6.3
select f.title, c.first_name, c.last_name, f.rental_rate, r.return_date
from customer c
left join rental r
	on c.customer_id = r.customer_id
left join inventory i
	on r.inventory_id = i.inventory_id
left join film f
	on i.film_id = f.film_id 
where 1 = 1 
and c.first_name = 'Matthew'
and c.last_name = 'Mahan'
and return_date between '2005-07-28' AND '2005-08-01'
and f.rental_rate > 4.00;

--6.4
select f.title, c.first_name, c.last_name, f.replacement_cost, description
from customer c
left join rental r
	on c.customer_id = r.customer_id
left join inventory i
	on r.inventory_id = i.inventory_id
left join film f
	on i.film_id = f.film_id 
where 1 = 1 
and c.first_name = 'Matthew'
and c.last_name = 'Mahan'
and description LIKE '%Boat%' or title like '%Boat%'
and replacement_cost > (select avg(replacement_cost) from film)
order by replacement_cost desc;