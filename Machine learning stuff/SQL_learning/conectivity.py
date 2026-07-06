import psycopg
con=psycopg.connect(
    host='localhost',
    dbname='learning_sql',
    user='postgres',
    password='12345'
)
cur=con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students
            id serial PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            course VARCHAR(50)
            );""")

con.commit()
print("table created")
cur.close()
con.close()