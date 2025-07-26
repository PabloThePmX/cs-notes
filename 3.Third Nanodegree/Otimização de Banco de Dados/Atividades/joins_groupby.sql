-- 1
SELECT l.name, COUNT(f.film_id) FROM language l
LEFT JOIN film f USING(language_id)
GROUP BY l.name;

-- 2
-- CIDADE - ENDEREÇO - LOJA - INVENTORIO - ALUGUEIS
SELECT s.store_id, c.city, COUNT(r.rental_id) qtd_alugueis FROM city c
INNER JOIN address a USING(city_id)
INNER JOIN store s USING(address_id)
INNER JOIN inventory i USING (store_id)
INNER JOIN rental r USING (inventory_id)
GROUP BY s.store_id, c.city;

-- 3
-- PAYMENT - CUSTOMER
SELECT c.first_name, MAX(p.amount) valor_amx FROM customer c 
INNER JOIN payment p USING(customer_id)
GROUP BY c.first_name
ORDER BY c.first_name ASC;