"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


def read_csv(csv_file):
    """
    Функция открывает файл и записывает в список
    """
    with open(csv_file, encoding='UTF=8') as f:
        reader = csv.reader(f)
        next(reader)
        list_row = []
        for row in reader:
            list_row.append(row)
    return list_row


customer_rows = read_csv("north_data/customers_data.csv")
customers_data = []
for i in customer_rows:
    customers_data.append(i)

employees_rows = read_csv("north_data/employees_data.csv")
employees_data = []
for i in employees_rows:
    employees_data.append(i)

orders_rows = read_csv("north_data/orders_data.csv")
orders_data = []
for i in orders_rows:
    orders_data.append(i)


with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
) as conn:
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", employees_data)
        cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", customers_data)
        cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", orders_data)

conn.close()

