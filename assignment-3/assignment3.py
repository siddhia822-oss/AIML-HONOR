import pymysql

class Employee:

    def __init__(self):
        self.db = {
            "host": "localhost",
            "user": "root",
            "password": "masa25#ade",
            "database": "employee"
        }

        with pymysql.connect(**self.db) as con:
            with con.cursor() as cur:
                cur.execute("""
                CREATE TABLE IF NOT EXISTS employee(
                    id INT PRIMARY KEY,
                    name VARCHAR(100),
                    department VARCHAR(100),
                    salary FLOAT,
                    email VARCHAR(100)
                )
                """)
            con.commit()

    def create(self):
        try:
            with pymysql.connect(**self.db) as con:
                with con.cursor() as cur:
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

        except Exception as e:
            print("Error:", e)

    def read(self):
        try:
            with pymysql.connect(**self.db) as con:
                with con.cursor() as cur:
                    cur.execute("SELECT * FROM employee")
                    rows = cur.fetchall()

            for row in rows:
                print(row)

        except Exception as e:
            print("Error:", e)

    def update(self):
        try:
            with pymysql.connect(**self.db) as con:
                with con.cursor() as cur:
                    id = input("Enter ID: ")
                    name = input("Enter New Name: ")

                    cur.execute(
                        "UPDATE employee SET name=%s WHERE id=%s",
                        (name, id)
                    )

                con.commit()

            print("Employee updated!")

        except Exception as e:
            print("Error:", e)

    def delete(self):
        try:
            with pymysql.connect(**self.db) as con:
                with con.cursor() as cur:
                    id = input("Enter ID: ")

                    cur.execute(
                        "DELETE FROM employee WHERE id=%s",
                        (id,)
                    )

                con.commit()

            print("Employee deleted!")

        except Exception as e:
            print("Error:", e)


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
        print("Goodbye!")
        break

    else:
        print("Invalid choice")