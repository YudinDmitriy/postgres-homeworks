-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar NOT NULL,
	last_name varchar,
	title varchar,
	birth_date DATE,
	notes varchar
);

CREATE TABLE customers
(
	customer_id varchar,
	company_name varchar,
	contact_name varchar
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar,
	employee_id int NOT NULL,
	order_date date,
	ship_city varchar
)

--Проверка таблиц
SELECT * FROM employees
SELECT * FROM customers
SELECT * FROM orders
