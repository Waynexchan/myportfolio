import psycopg2
import os

try:
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    cursor = conn.cursor()
    cursor.execute('SELECT 1')
    print('Connection successful')
except Exception as e:
    print(f'Error: {e}')
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
