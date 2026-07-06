import psycopg

conn=psycopg.connect(
    host="localhost",
    dbname="learning_sql",
    user="postgres",
    password="12345"
)
cur=conn.cursor()
print("connected succcesfully")
conn.close()