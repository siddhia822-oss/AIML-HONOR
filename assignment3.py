import sqlite3

class Employee:

    def __init__(self):
        self.db = "employee.db"

    def create(self):
        try:
            with sqlite3.connect(self.db) as con:
                con.execute(
                    "INSERT INTO employee VALUES (?, ?, ?, ?, ?)",
                    (
                        input("ID: "),
                        input("Name: "),
                        input("Department: "),
                        input("Salary: "),
                        input("Email: ")
                    )
                )
            print("Employee added")
        except Exception as e:
            print("Error:", e)

    def read(self):
        try:
            with sqlite3.connect(self.db) as con:
                rows = con.execute("SELECT * FROM employee").fetchall()

            for row in rows:
                print(row)

        except Exception as e:
            print("Error:", e)

    def update(self):
        try:
            id = input("Enter ID: ")
            name = input("Enter new name: ")

            with sqlite3.connect(self.db) as con:
                con.execute(
                    "UPDATE employee SET name=? WHERE id=?",
                    (name, id)
                )

            print("Updated")

        except Exception as e:
            print("Error:", e)

    def delete(self):
        try:
            id = input("Enter ID: ")

            with sqlite3.connect(self.db) as con:
                con.execute(
                    "DELETE FROM employee WHERE id=?",
                    (id,)
                )

            print("Deleted")

        except Exception as e:
            print("Error:", e)


emp = Employee()

while True:
    print("\n1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

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