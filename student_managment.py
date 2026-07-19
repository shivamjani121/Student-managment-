import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    marks REAL NOT NULL
)
""")
conn.commit()


# ---------------- Functions ---------------- #

def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (roll, name, course, marks)
        )
        conn.commit()
        print("\nStudent Added Successfully!\n")

    except sqlite3.IntegrityError:
        print("\nRoll Number already exists!\n")


def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if not records:
        print("\nNo Student Records Found.\n")
        return

    print("\n{:<10}{:<25}{:<20}{:<10}".format(
        "Roll", "Name", "Course", "Marks"))
    print("-"*65)

    for row in records:
        print("{:<10}{:<25}{:<20}{:<10}".format(
            row[0], row[1], row[2], row[3]))


def search_student():
    roll = int(input("Enter Roll Number: "))

    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("----------------------")
        print("Roll :", student[0])
        print("Name :", student[1])
        print("Course :", student[2])
        print("Marks :", student[3])
    else:
        print("\nStudent Not Found!")


def update_student():
    roll = int(input("Enter Roll Number to Update: "))

    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    if cursor.fetchone() is None:
        print("Student Not Found!")
        return

    name = input("Enter New Name: ")
    course = input("Enter New Course: ")
    marks = float(input("Enter New Marks: "))

    cursor.execute("""
        UPDATE students
        SET name=?, course=?, marks=?
        WHERE roll=?
    """, (name, course, marks, roll))

    conn.commit()
    print("\nStudent Updated Successfully!\n")


def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))

    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    if cursor.fetchone() is None:
        print("Student Not Found!")
        return

    cursor.execute("DELETE FROM students WHERE roll=?", (roll,))
    conn.commit()

    print("\nStudent Deleted Successfully!\n")


# ---------------- Main Menu ---------------- #

while True:

    print("""
==============================
 STUDENT MANAGEMENT SYSTEM
==============================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
==============================
""")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!\n")

conn.close()
