import csv
import pymysql
import os

class Employee:
    def __init__(self):
        self.file = "employee.csv"

        con = pymysql.connect(
            host="localhost",
            user="root",
            password="masa25#ade",
            database="employee"
        )

        with con:
            with con.cursor() as cur:
                cur.execute("SELECT * FROM employee")
                data = cur.fetchall()

        with open(self.file, "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
                "emp_id", "name", "department", "salary", "email"
            ])

            writer.writerows(data)

    def read(self):
        with open(self.file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    def create(self):
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = input("Enter Salary: ")
        email = input("Enter Email: ")

        with open(self.file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id, name, dept, salary, email])

        print("Employee added!")

    def update(self):
        id = input("Enter Employee ID: ")
        name = input("Enter New Name: ")

        rows = []

        with open(self.file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == id:
                    row[1] = name
                rows.append(row)
        with open(self.file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print("Employee updated!")

    def delete(self):
        id = input("Enter Employee ID: ")

        rows = []
        with open(self.file, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                if row[0] != id:
                    rows.append(row)

        with open(self.file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print("Employee deleted!")

emp = Employee()

while True:
    print("""
1. Create Employee
2. Read Employees
3. Update Employee
4. Delete Employee
5. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        emp.create()
    elif choice == "2":
        emp.read()
    elif choice == "3":
        emp.update()
    elif choice == "4":
        emp.delete()
    elif choice == "5":
        break
    else:
        print("Invalid choice")