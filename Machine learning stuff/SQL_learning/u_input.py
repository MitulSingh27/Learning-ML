import psycopg
con=psycopg.connect(
    host='localhost',
    dbname='learning_sql',
    user='postgres',
    password='12345'
)
cur=con.cursor()

name=input("enter name-")
age=int(input("enter age-"))
course=input("enter course-")

cur.execute("""INSERT INTO students (name,age,course)
            VALUES (%s,%s,%s)""",(name,age,course))

con.commit()
print("student added")
cur.execute("SELECT * FROM students")
students=cur.fetchall()
print("\nStudents:")
for student in students:
    print(student)
#whatever we did was very inefficient, what if we have 10000 rows of data, cant print everything

cur.execute("""
INSERT INTO students(name, age, course)
VALUES (%s, %s, %s)
RETURNING *
""", (name, age, course))
student = cur.fetchone()
con.commit()
print(student)

cur.close()
con.close()