--1
-- cria a coluna caso não existir
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1 
		FROM information_schema.columns 
		WHERE table_name='staff' and column_name='extra'
	) THEN
		ALTER TABLE staff
		ADD extra numeric;
	END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION extra_in_staff()
	RETURNS TRIGGER AS 
$BODY$
DECLARE
	last_extra NUMERIC;
BEGIN
	last_extra := (
		SELECT extra FROM staff
		WHERE staff_id = NEW.staff_id
	);

	IF last_extra IS NULL THEN
    	RAISE WARNING 'There is no value in the column "extra"! Adding one now.';
		UPDATE staff
		SET extra = 1
		WHERE staff_id = NEW.staff_id;
	ELSE
		UPDATE staff
		SET extra = last_extra + 1
		WHERE staff_id = NEW.staff_id;
	END IF;

	RETURN NULL;
END;
$BODY$ LANGUAGE plpgsql;

CREATE TRIGGER insert_rental
	AFTER INSERT
	ON rental
	FOR EACH ROW
	EXECUTE PROCEDURE extra_in_staff();

INSERT INTO rental(rental_date, inventory_id, customer_id, return_date, staff_id)
VALUES(CURRENT_DATE, 6, 1, CURRENT_DATE + 5, 2);

SELECT * FROM staff;


--2
CREATE OR REPLACE FUNCTION check_password()
	RETURNS TRIGGER AS 
$BODY$
BEGIN
	IF LENGTH(NEW.password) < 8 OR NEW.password !~ '[0-9]' OR NEW.password !~ '[A-Z]' THEN
		RAISE EXCEPTION 'A senha (password) deverá conter, pelo menos, uma letra maíuscula, e um número. O tamanho mínimo da senha deverá ser de, pelo menos, oito caracteres.';
	END IF;

	RETURN NEW;
END;
$BODY$ LANGUAGE plpgsql;

CREATE TRIGGER check_password_staff
	BEFORE INSERT OR UPDATE
	ON staff
	FOR EACH ROW
	EXECUTE PROCEDURE check_password();

--Sem numero
INSERT INTO staff(first_name, last_name, address_id, email, store_id, active, username, password)
VALUES('Ciclano', 'da Silva', 1, 'ciclano@gmail.com', 1, true, 'Ciclano123', 'TesteTeste');

--Sem upper
INSERT INTO staff(first_name, last_name, address_id, email, store_id, active, username, password)
VALUES('Ciclano', 'da Silva', 1, 'ciclano@gmail.com', 1, true, 'Ciclano123', 'teste123');

--Menor que 8
INSERT INTO staff(first_name, last_name, address_id, email, store_id, active, username, password)
VALUES('Ciclano', 'da Silva', 1, 'ciclano@gmail.com', 1, true, 'Ciclano123', 'Teste1');

--Funciona
INSERT INTO staff(first_name, last_name, address_id, email, store_id, active, username, password)
VALUES('Ciclano', 'da Silva', 1, 'ciclano@gmail.com', 1, true, 'Ciclano123', 'TesteTeste123');

SELECT * FROM staff;


--3
CREATE OR REPLACE FUNCTION check_rentals()
	RETURNS TRIGGER AS
$BODY$
DECLARE
	user_rental RECORD;
BEGIN
	--CHECK IF THERES RENTALS WITH THAT CUSTOMER
	--CHECK IF THE RETURN DATE IS LESS THAN TODAY
	--CHECK IF THE PAYMENT OF THE RENTAL IS LESS THEN TODAY
	FOR user_rental IN (
		SELECT r.return_date, p.payment_date FROM rental r
		INNER JOIN payment p USING(customer_id)
		WHERE p.customer_id = NEW.customer_id AND r.return_date IS NOT NULL
	)
	LOOP
		IF user_rental.return_date::date IS NULL THEN
			RAISE EXCEPTION 'Existem devoluções pendentes.';
		END IF;

		IF user_rental.payment_date IS NULL THEN
			RAISE EXCEPTION 'Existem pagamentos pendentes.';
		END IF;
	END LOOP;

	RETURN NEW;
END;
$BODY$ LANGUAGE plpgsql;

CREATE TRIGGER check_customer_rentals
	BEFORE INSERT
	ON rental
	FOR EACH ROW
	EXECUTE PROCEDURE check_rentals();

INSERT INTO rental(rental_date, inventory_id, customer_id, return_date, staff_id)
VALUES(CURRENT_DATE, 9, 1, CURRENT_DATE + 5, 29);


--4
DO $$
BEGIN
	IF NOT EXISTS (
		SELECT 1 
		FROM information_schema.columns 
		WHERE table_name='staff_password_log'
	) THEN
		CREATE TABLE staff_password_log (
			id SERIAL PRIMARY KEY,
			staff_id INT REFERENCES staff,
			modify_date TIMESTAMP,
			prev_password VARCHAR(40)
		);
	END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION check_staff_password()
RETURNS TRIGGER AS
$BODY$
BEGIN
	IF(NEW.password <> OLD.password) THEN
		INSERT INTO staff_password_log(staff_id, modify_date, prev_password)
		VALUES(NEW.staff_id, NOW(), OLD.password);
	END IF;
	
	RETURN NULL;
END;
$BODY$ LANGUAGE plpgsql;

CREATE TRIGGER staff_password_changed
	AFTER UPDATE
	ON staff
	FOR EACH ROW
	EXECUTE PROCEDURE check_staff_password();

UPDATE staff
SET password = '123456789TesteLog'
WHERE staff_id = 27;

SELECT * FROM staff_password_log;