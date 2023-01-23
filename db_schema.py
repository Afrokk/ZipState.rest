import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="dataset",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

cursor = conn.cursor()

# TO-DO: Code DB Schema Here

conn.commit()
cursor.close()
conn.close()
