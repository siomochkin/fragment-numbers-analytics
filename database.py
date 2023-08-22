import psycopg2
from config import settings as s

try:
    connection = psycopg2.connect(
        database=s.DB_NAME, 
        host=s.DB_HOST,
        user=s.DB_USER,
        password=s.DB_PASSWORD, 
        port=s.DB_PORT)
    
    connection.autocommit = True
    
    # Create table numbers
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE numbers(
                id SERIAL PRIMARY KEY,
                data TIMESTAMPTZ NOT NULL,
                price NUMERIC(8,2) NOT NULL,
                ton  NUMERIC(8,5) NOT NULL,
                phone VARCHAR(50) NOT NULL, 
                status VARCHAR(50) NOT NULL,
                remaining_time VARCHAR(50) NOT NULL
                );"""
        )
        
        print(f"Server version: {cursor.fetchone()}")
    
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL::", error)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')
