import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="localhost"
)

cur = conn.cursor()

table_create_query = sql.SQL(
    """
    CREATE TABLE IF NOT EXISTS patients (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(50),
        date_of_birth DATE,
        gender VARCHAR(10)
    );
    """
)

cur.execute(table_create_query)
conn.commit()
