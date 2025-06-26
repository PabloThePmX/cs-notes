-- 1
SELECT first_name, last_name, email FROM customer
UNION 
SELECT first_name, last_name, email FROM staff;

-- 2
SELECT first_name || ' ' || last_name name FROM customer
WHERE activebool = true
UNION
SELECT first_name || ' ' || last_name AS name FROM customer 
WHERE customer_id NOT IN (
    SELECT customer_id FROM rental
);

-- 3
SELECT title, length, c.name category FROM film
INNER JOIN film_category USING(film_id)
INNER JOIN category c USING(category_id)
WHERE c.name = 'Action'
UNION
SELECT title, length, c.name category FROM film
INNER JOIN film_category USING(film_id)
INNER JOIN category c USING(category_id)
WHERE c.name = 'Music';

-- 4
WITH clientes_frequentes AS (
	SELECT customer_id, first_name || ' ' || last_name name, COUNT(r.rental_id) qtd_alugueis FROM customer
	INNER JOIN rental r USING (customer_id)
	GROUP BY customer_id
	HAVING COUNT(r.rental_id) > 5
)
SELECT name, qtd_alugueis FROM clientes_frequentes;

-- 5
WITH mais_alugados AS (
	SELECT film_id, title, COUNT(film_id) qtd from film
	INNER JOIN inventory USING(film_id)
	INNER JOIN rental USING(inventory_id)
	GROUP BY film_id
)
SELECT title, qtd from mais_alugados
ORDER BY qtd DESC
LIMIT 5;

-- 6
WITH duracao_acima_media AS (
	SELECT AVG(length) media FROM film
)
SELECT title, length, (SELECT * FROM duracao_acima_media) FROM film
WHERE length > (SELECT * FROM duracao_acima_media);

-- 7
WITH filmes_drama AS (
	SELECT title, c.name FROM film
	INNER JOIN film_category USING(film_id)
	INNER JOIN category c USING(category_id)
	WHERE c.name = 'Drama'
)
SELECT * FROM filmes_drama;

-- 8
WITH alugueis_funcionarios AS (
	SELECT st.store_id, c.city FROM rental
	INNER JOIN inventory i USING(inventory_id)
	INNER JOIN store st USING(store_id)
	INNER JOIN address USING(address_id)
	INNER JOIN city c USING(city_id)
)
SELECT city FROM alugueis_funcionarios
GROUP BY city;

--9
SELECT title, qtd_alugueis, RANK() OVER (ORDER BY qtd_alugueis DESC) AS rank_aluguel
FROM (
	SELECT f.title, COUNT(*) AS qtd_alugueis
	FROM rental r
	INNER JOIN inventory i USING(inventory_id)
	INNER JOIN film f USING(film_id)
	GROUP BY f.film_id, f.title
) AS filmes_mais_alugados;


--10
SELECT customer_id, r.rental_date, ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY rental_date) cumulative_rentals FROM customer
INNER JOIN rental r USING(customer_id)	
ORDER BY customer_id;

--11
CREATE VIEW film_categories AS (
	SELECT title, c.name FROM film
	INNER JOIN film_category USING(film_id)
	INNER JOIN category c USING(category_id)
);
SELECT * FROM film_categories;

--12
CREATE VIEW active_customers AS (
	SELECT first_name || ' ' || last_name name FROM customer
	WHERE activebool = true
);
SELECT * FROM active_customers
ORDER BY name;

--13
CREATE MATERIALIZED VIEW total_rents_per_film AS (
	SELECT film_id, title, COUNT(film_id) qtd_alugueis from film
	INNER JOIN inventory USING(film_id)
	INNER JOIN rental USING(inventory_id)
	GROUP BY film_id
	ORDER BY COUNT(film_id) DESC
);
SELECT title, qtd_alugueis FROM total_rents_per_film;

--14
CREATE MATERIALIZED VIEW total_amount_per_staff AS (
	 SELECT s.staff_id, s.first_name || ' ' || s.last_name name, SUM(p.amount) AS total_vendas FROM staff s
	 INNER JOIN payment p USING(staff_id)
	 GROUP BY s.staff_id
);
SELECT name, total_vendas FROM total_amount_per_staff;