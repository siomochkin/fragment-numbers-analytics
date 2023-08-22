import psycopg2
from config import settings as s

try:
    conn = psycopg2.connect(
        dbname=s.DB_NAME, host=s.DB_HOST, user=s.DB_USER, password=s.DB_PASSWORD, port=s.DB_PORT)
    print(conn.get_dsn_parameters(), "\n")
    conn.close()
except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL::", error)
    