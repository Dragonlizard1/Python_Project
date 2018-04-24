select customer.first_name, customer.last_name, customer.email, address.address
from customer
join address on customer.address_id = address.address_id
where address.city_id LIKE 312;
 
SELECT film.title, film.description, film. release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category on film.film_id = film_category.film_id
JOIN category on film_category.category_id = category.category_id
WHERE category.name LIKE "comedy";

SELECT actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
FROM film
JOIN film_actor on film.film_id = film_actor.film_id
JOIN actor on film_actor.actor_id = actor.actor_id
WHERE film_actor.actor_id = 5;

SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address on customer.address_id = address.address_id
WHERE (customer.store_id = 1) and (address.city_id IN (1,42,312,459));

SELECT title, description, release_year, rating, special_features, film_actor.actor_id
FROM film
JOIN film_actor on film.film_id = film_actor.film_id
WHERE (film_actor.actor_id = 15) and (rating = "G") and (special_features LIKE "behind the scenes");

SELECT film.film_id, film.title, film_actor.actor_id, CONCAT(actor.first_name, " ",actor.last_name) as name
FROM film
JOIN film_actor on film.film_id = film_actor.film_id
JOIN actor on film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre, film.rental_rate
FROM film
JOIN film_category on film.film_id = film_category.film_id
JOIN category on film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99 and category.name LIKE "drama";

SELECT CONCAT(actor.first_name, " ", actor.last_name) as actor_name, film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
FROM film
JOIN film_category on film.film_id = film_category.film_id
JOIN film_actor on film.film_id = film_actor.film_id
JOIN actor on film_actor.actor_id = actor.actor_id
JOIN category on film_category.category_id = category.category_id
WHERE actor.first_name = "sandra" and actor.last_name = "Kilmer" and category.name = "action"

 
 
 
 