import sqlite3

table_creation = "CREATE TABLE IF NOT EXISTS " \
                 "employees (id INTEGER PRIMARY KEY, name TEXT, role TEXT, salary REAL)"

try:
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute(table_creation)

except sqlite3.Error as e:
    print(f"Error: {e}")