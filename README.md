# Simple CRUD – Python Desktop Application

A simple **CRUD (Create, Read, Update, Delete)** desktop application built with **Python**, featuring a graphical user interface and a local database.

This project was developed as a hands-on exercise to practice software structuring, object-oriented programming, and full data flow from user interface to database.

---

## 🧩 Features

- Create new employees
- Read a single employee by ID
- List all employees
- Update employee data
- Delete employees
- Graphical interface for all operations

---

## 🛠️ Technologies Used

- **Python**
- **Tkinter** – graphical user interface
- **SQLite** – local database
- **Object-Oriented Programming (OOP)**

---

## 🗂️ Project Structure

. <br>
├── App.py # Application entry point <br>
├── DatabaseManager.py # Database connection and lifecycle management <br>
├── Repository.py # Data access layer (CRUD operations) <br>
├── Models.py # Domain models <br>
├── gui/ <br>
│ ├── Forms.py # GUI windows and user interactions <br>
│ └── Styles.py # Centralized UI styles <br>
└── data.db # SQLite database <br>

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/simple-crud.git
   ```
2. Navigate to the project folder:

    ```bash
    cd simple-crud
    ```
3. Run the application:

    ```bash
    python App.py
    ```

No external dependencies are required.

## 🎯 Learning Goals
The main goals of this project were:

- Practice building a complete CRUD system
- Understand data flow between GUI, business logic, and database
- Apply object-oriented principles in a real project
- Learn when to prioritize structure and when to prioritize delivery-
- Finish and ship a functional application

## 📌 Notes
This project focuses on clarity and completeness, not production-level optimizations or advanced UI/UX patterns.
It was intentionally kept simple to reinforce core concepts.

## 👤 Author
Developed by Matheus Gana.