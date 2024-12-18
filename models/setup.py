# models/setup.py

import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
CONN = sqlite3.connect('student_management.db')
CURSOR = CONN.cursor()

def setup_db():
    """
    Setup the database schema (creating tables if they don't exist).
    """
    with open('models/schema.sql', 'r') as schema_file:
        sql = schema_file.read()
        CURSOR.executescript(sql)
        CONN.commit()
