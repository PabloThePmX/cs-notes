--1
-- FILM - INVENTORY - STORE
SELECT title FROM film
INNER JOIN inventory USING(film_id)
WHERE store_id IN (
	SELECT store_id FROM store 
	WHERE store_id = 1
);

--2
-- CUSTOMER - RENTAL
SELECT first_name || ' ' || last_name nome FROM customer c
WHERE EXISTS (
	SELECT 1 FROM rental r
	WHERE c.customer_id = r.customer_id
);

--3
-- ACTORS - FILM_ACTOR - FILM - FILM_CATEGORY - CATEGORY
SELECT first_name || ' ' || last_name nome FROM actor a
INNER JOIN film_actor USING (actor_id)
INNER JOIN film USING (film_id)
WHERE film_id IN (
	SELECT film_id FROM film_category
	INNER JOIN category USING(category_id)
	WHERE name = 'Comedy'
);

--4 
-- INVENTORY
SELECT film_id, COUNT(film_id) qtd FROM inventory
GROUP BY film_id
HAVING COUNT(film_id) > 1
ORDER BY COUNT(film_id) DESC;

--5
-- CUSTOMERS - ADDRESS - CITY
-- verifica se a cidade existe no address e se ela se chama dessa forma
SELECT first_name || ' ' || last_name nome, city_id FROM customer c
INNER JOIN address a USING (address_id)
WHERE EXISTS (
	SELECT 1 FROM city ci
	WHERE ci.city = 'San Bernardino' AND ci.city_id = a.city_id
);

--6
-- FILM - FILM_CATEGORY - CATEGORY
SELECT title, c.name FROM film f
INNER JOIN film_category USING(film_id)
INNER JOIN category c USING(category_id)
WHERE c.name IN ('Action', 'Horror');

--7
-- CUSTOMERS - RENTALS
SELECT first_name || ' ' || last_name nome FROM customer c
WHERE customer_id NOT IN (
	SELECT customer_id FROM rental
);

--8
-- FILM - RENTAL - INVENTORY
SELECT title FROM film f
WHERE EXISTS (
    SELECT 1 FROM rental r
    INNER JOIN inventory i USING (inventory_id)
    WHERE i.film_id = f.film_id
    GROUP BY i.film_id
    HAVING COUNT(r.rental_id) > 10
);

--9
-- FILM - FILM_CATEGORY - CATEGORY
SELECT c.name, COUNT(*) FROM film
INNER JOIN film_category USING(film_id)
INNER JOIN category c USING (category_id)
GROUP BY c.name
HAVING COUNT(*) > 20;

--10
-- ACTOR - FILM_ACTOR - FILM
-- usa o distinct pq tem atores que participaram de mis filmes no mesmo ano
SELECT DISTINCT first_name || ' ' || last_name nome FROM actor a
INNER JOIN film_actor USING(actor_id)
WHERE film_id IN (
	SELECT film_id FROM film f 
	WHERE release_year = 2006
)

--11
-- FILM - INVENTORY - RENTAL
SELECT title FROM film
INNER JOIN inventory i USING(film_id)
WHERE NOT EXISTS (
	SELECT 1 FROM rental r
	WHERE r.inventory_id = i.inventory_id
);

--12
-- CITY - ADDRESS - CUSTOMER
-- onde esta na cidade que existe em um cadastro de cliente
SELECT DISTINCT city FROM city 
WHERE city_id IN (
    SELECT city_id FROM address 
	INNER JOIN customer USING(address_id)
);


--13
-- STAFF - RENTAL
SELECT s.first_name || ' ' || s.last_name nome FROM staff s
WHERE EXISTS (
    SELECT 1 FROM rental r
    WHERE s.staff_id = r.staff_id
    GROUP BY r.staff_id
    HAVING COUNT(r.rental_id) > 100
);


--14
-- CUSTOMERS - RENTAL
SELECT customer_id, c.first_name || ' ' || c.last_name nome FROM rental
INNER JOIN customer c USING(customer_id)
WHERE EXTRACT(MONTH FROM rental_date) = EXTRACT(MONTH FROM CURRENT_DATE - INTERVAL '1 month')
	AND EXTRACT(YEAR FROM rental_date) = EXTRACT(YEAR FROM CURRENT_DATE - INTERVAL '1 month')
GROUP BY customer_id
HAVING COUNT(rental_id) > 5;


--15
-- FILM - FILM_CATEGORY - CATEGORY
SELECT title FROM film
INNER JOIN film_category USING(film_id)
WHERE category_id IN (
	SELECT category_id FROM category
	WHERE name = 'Drama'
) AND length > 100