#DatabaseManager.py
import sqlite3

class DatabaseManager():
    def __init__(self, path):
        self.path = path
        self.connection = None
        self.cursor = None

        self.setup_db()

    def setup_db(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                role TEXT,
                salary REAL
            )
        """)

        self.connection.commit()
        self.connection.close()
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
            self.connection.close()