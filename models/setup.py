# # # models/setup.py

# # import sqlite3

# # # Connect to SQLite database (it will create the database if it doesn't exist)
# # CONN = sqlite3.connect('student_management.db')
# # CURSOR = CONN.cursor()

# # def setup_db():
# #     """
# #     Setup the database schema (creating tables if they don't exist).
# #     """
# #     with open('models/schema.sql', 'r') as schema_file:
# #         sql = schema_file.read()
# #         CURSOR.executescript(sql)
# #         CONN.commit()


# import sqlite3

# # Create a new SQLite database or connect to an existing one
# conn = sqlite3.connect('student_management.db')
# cursor = conn.cursor()

# # Create the students table if it doesn't already exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL
#     )
# ''')

# # Create the courses table if it doesn't already exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS courses (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         course_title TEXT NOT NULL,
#         course_duration INTEGER NOT NULL
#     )
# ''')

# # Create the enrollments table to track student-course enrollments
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS enrollments (
#         student_id INTEGER NOT NULL,
#         course_id INTEGER NOT NULL,
#         PRIMARY KEY (student_id, course_id),
#         FOREIGN KEY (student_id) REFERENCES students (id),
#         FOREIGN KEY (course_id) REFERENCES courses (id)
#     )
# ''')

# conn.commit()
# conn.close()

# print("Database and tables created (if not exists).")

import sqlite3

def create_tables():
    conn = sqlite3.connect('student_management.db')
    cursor = conn.cursor()

    # Create students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)

    # Create courses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        course_title TEXT,
        course_duration INTEGER
    )
    """)

    # Create enrollments table (many-to-many relationship between students and courses)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id),
        PRIMARY KEY (student_id, course_id)
    )
    """)

    conn.commit()
    conn.close()

# Call create_tables to initialize the database when the application starts
create_tables()
