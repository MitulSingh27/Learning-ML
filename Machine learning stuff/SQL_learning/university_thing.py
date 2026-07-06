"""| id | course_name      | duration |
   | -- | ---------------- | -------- |
   | 1  | Python           | 3 Months |
   | 2  | SQL              | 2 Months |
   | 3  | Machine Learning | 6 Months |
   | 4  | Data Structures  | 4 Months |
   | 5  | Web Development  | 5 Months |
Create the courses table.
Write a Python function add_courses().
Insert all 5 courses without repeating code.
Display the table."""


import psycopg
con=psycopg.connect(
    host="localhost",
    dbname="university_thing",
    user="postgres",
    password="12345"
)
cur=con.cursor()
print("connected")
'''
cur.execute("""CREATE TABLE students(
            id INT PRIMARY KEY,
            name VARCHAR(50),
            age INT);
            """)
print("table created")
cur.execute("""CREATE TABLE courses(
            id INT PRIMARY KEY,
            course_name VARCHAR(50),
            duration INT);
            """)
print("table created")
cur.execute("""CREATE TABLE enrollments(
            student_id INT PRIMARY KEY,
           course_id INT);
            """)
print("table created")
con.commit()
'''
def add_course():
    y='n'
    while True:
        id=int(input("enter course_id"))
        course_name=input("enter course name-")
        duration=int(input("enter time in months-"))
        try:
            cur.execute("""INSERT INTO courses(id,course_name,duration)
                        VALUES(%s,%s,%s)""",(id,course_name,duration))
        except Exception as e:
            con.rollback()
            print(e)
        y=input("do you want to add another course ? (y,n)-")
        if y=="n":
            break



def show_courses():
    cur.execute("""SELECT* FROM courses""")
    courses=cur.fetchall()
    for course in courses:
        print("course-\n",course)

def main():
   add_course()
   con.commit()
   show_courses()

main()
cur.close()
con.close()