import pandas as pd
import pymysql

con = pymysql.connect(
    host="localhost",
    user="root",
    password="masa25#ade",
    database="employee"
)

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employee(
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary FLOAT,
    email VARCHAR(100)
)
""")
con.commit()


def add():
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")
    email = input("Enter Email: ")

    cur.execute(
        "INSERT INTO employee VALUES(%s,%s,%s,%s,%s)",
        (id, name, dept, salary, email)
    )
    con.commit()
    print("Employee added!")


def display():
    data = pd.read_sql("SELECT * FROM employee", con)
    print(data)


def average():
    data = pd.read_sql("SELECT salary FROM employee", con)

    if len(data) == 0:
        print("No employees found")
    else:
        print("Average Salary:", data["salary"].mean())


def update():
    id = input("Enter Employee ID: ")
    name = input("Enter new name: ")

    cur.execute(
        "UPDATE employee SET name=%s WHERE emp_id=%s",
        (name, id)
    )
    con.commit()
    print("Employee updated!")


def delete():
    id = input("Enter Employee ID: ")

    cur.execute(
        "DELETE FROM employee WHERE emp_id=%s",
        (id,)
    )
    con.commit()
    print("Employee deleted!")


while True:
    print("""
1. Add Employee
2. View Employees
3. Average Salary
4. Update Employee
5. Delete Employee
6. Exit
""")

    choice = input("Enter choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        display()
    elif choice == "3":
        average()
    elif choice == "4":
        update()
    elif choice == "5":
        delete()
    elif choice == "6":
        break
    else:
        print("Invalid choice")

con.close()