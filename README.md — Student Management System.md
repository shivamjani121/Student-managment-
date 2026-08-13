# Student Management System

A **Python-based Student Management System** built using **SQLite** that allows users to manage student records through a simple command-line interface.

The system performs complete **CRUD (Create, Read, Update, Delete)** operations and stores student information permanently in an SQLite database.

## 🚀 Features

- Add new student records
- View all students
- Search students by roll number
- Update existing student information
- Delete student records
- SQLite database integration
- Automatic database and table creation
- Primary key validation for roll numbers
- Basic error handling
- Interactive command-line menu

## 🛠️ Technologies Used

- **Python 3**
- **SQLite3**
- Python `sqlite3` module

## 📚 Database Structure

The project uses an SQLite database named:

```text
students.db
```

The `students` table contains the following fields:

| Field | Data Type | Description |
|---|---|---|
| `roll` | INTEGER | Unique student roll number |
| `name` | TEXT | Student name |
| `course` | TEXT | Student's course |
| `marks` | REAL | Student's marks |

The `roll` field is used as the **Primary Key**, which means every student must have a unique roll number.

## 🔄 CRUD Operations

The project demonstrates the four basic database operations:

### Create

Add a new student to the database.

```text
Roll Number
Name
Course
Marks
```

### Read

View all student records or search for a particular student using their roll number.

### Update

Modify the name, course, and marks of an existing student.

### Delete

Remove a student record from the database.

## 📊 Project Workflow

```text
          Start Program
                │
                ▼
       Connect to SQLite
                │
                ▼
       Create Database/Table
                │
                ▼
          Main Menu
                │
      ┌─────────┼─────────┐
      ▼         ▼         ▼
     Add       View      Search
      │         │         │
      └─────────┼─────────┘
                │
          Update / Delete
                │
                ▼
        Save Changes
                │
                ▼
              Exit
```

## 📁 Project Structure

```text
student-management-system/
│
├── student_management.py
├── README.md
├── .gitignore
└── students.db
```

> **Note:** `students.db` is created automatically when the program is executed. It is recommended not to upload a database containing real or personal student information to GitHub.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/student-management-system.git
```

### 2. Open the project folder

```bash
cd student-management-system
```

### 3. Run the program

```bash
python student_management.py
```

The SQLite database and `students` table will be created automatically when the program runs.

## 💻 Example Menu

```text
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

Enter Your Choice:
```

## ➕ Example: Adding a Student

```text
Enter Roll Number: 101
Enter Name: Rahul
Enter Course: B.Tech CSE
Enter Marks: 85.5

Student Added Successfully!
```

## 🔍 Example: Searching a Student

```text
Enter Roll Number: 101

Student Found
----------------------
Roll : 101
Name : Rahul
Course : B.Tech CSE
Marks : 85.5
```

## 🗄️ SQLite Database

SQLite is a lightweight, serverless database that stores the entire database in a single file.

This project uses Python's built-in `sqlite3` module, so no separate database server installation is required.

## 🔐 Data Safety

The project is designed for learning purposes.

Do not upload databases containing:

- Real student information
- Personal information
- Sensitive academic records
- Passwords or confidential data

For a public GitHub repository, add the database file to `.gitignore`:

```text
students.db
```

## 🔮 Future Improvements

Possible improvements for future versions:

- Add student email and phone number
- Add student date of birth
- Add attendance management
- Add subject-wise marks
- Calculate grades automatically
- Add sorting and filtering
- Add input validation
- Add GUI using Tkinter
- Add web interface using Flask or Streamlit
- Add login/authentication
- Export student records to CSV or Excel
- Add database backup functionality

## 🎯 Learning Objectives

This project was developed to understand:

- Python functions
- User input handling
- Conditional statements
- Loops
- Exception handling
- SQLite database connectivity
- SQL queries
- CRUD operations
- Primary keys
- Database transactions
- Building menu-driven applications

## 👨‍💻 Author

**Shivam Singh Jani**

B.Tech Computer Science Engineering  
AI/ML Enthusiast | Python | SQL | Machine Learning

## ⭐ Project Purpose

This project demonstrates how Python can be integrated with a relational database to build a simple but functional **Student Management System**.

It is intended as an educational project to demonstrate practical knowledge of **Python, SQL, database management, and CRUD operations**.