#name,age,course

import psycopg
con=psycopg.connect(
    host="localhost",
    dbname="learning_sql",
    user="postgres",
    password="12345"
)
cur=con.cursor()
print("connected")

def add_student():
    name=input("enter name-")
    age=int(input("enter age-"))
    course=input("enter course-")
    try:
        cur.execute("""INSERT INTO students(name,age,course)
                VALUES(%s,%s,%s)""",(name,age,course))
        
        con.commit()
        print("student added")

    except Exception as e:
        con.rollback()
        print(e)

def show_students():
    try:
        cur.execute("SELECT * FROM students")
        students=cur.fetchall()
        for student in students:
            print(student)

        con.commit()
        print("student list-")
    except Exception as e:
        con.rollback()
        print(e)     

def main():
      add_student()
      show_students()

main()

cur.close()
con.close()
