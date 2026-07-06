import psycopg
con=psycopg.connect(
    host='localhost',
    dbname='learning_sql',
    user='postgres',
    password='12345'
)
cur=con.cursor()

cur.execute("""
INSERT INTO students (name, age, course)
VALUES (%s, %s, %s)
""", ("Mitul Singh", 20, "Python + SQL"))

cur.execute("""
            SELECT column_name FROM information_schema.columns WHERE table_name='students'""")

for column in cur.fetchall():
    print(column)

con.commit()
print("student added")
cur.close()
con.close()