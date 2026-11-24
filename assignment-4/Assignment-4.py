
import pandas as pd
import pymysql
from sqlalchemy import create_engine

con = pymysql.connect(
    host="localhost",
    user="root",
    password="masa25#ade",
    database="employee"
)

engine = create_engine("mysql+pymysql://root:masa25%23ade@localhost/employee")

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employee(
emp_id INT PRIMARY KEY,
name VARCHAR(100),
department VARCHAR(100),
salary FLOAT,
email VARCHAR(100))
""")
con.commit()

def add():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    email = input("Enter Email: ")

    df = pd.DataFrame([[id, name, dept, salary, email]],
        columns=["emp_id", "name", "department", "salary", "email"])

    df.to_sql("employee", engine, if_exists="append", index=False)
    print("Employee Added!")

def display():
    df = pd.read_sql("SELECT * FROM employee", con)
    print(df)

def avg():
    df = pd.read_sql("SELECT salary FROM employee", con)
    print("Average Salary:", df["salary"].mean())

def update():
    id = int(input("Enter ID: "))
    name = input("Enter New Name: ")

    cur.execute("UPDATE employee SET name=%s WHERE emp_id=%s", (name, id))
    con.commit()
    print("Updated!")

def delete():
    id = int(input("Enter ID: "))

    cur.execute("DELETE FROM employee WHERE emp_id=%s", (id,))
    con.commit()
    print("Deleted!")

while True:
    print("""
1. Add
2. Display
3. Average Salary
4. Update
5. Delete
6. Exit
""")

    ch = input("Enter choice: ")

    if ch == "1":
        add()
    elif ch == "2":
        display()
    elif ch == "3":
        avg()
    elif ch == "4":
        update()
    elif ch == "5":
        delete()
    elif ch == "6":
        break
    else:
        print("Invalid Choice")

con.close()
