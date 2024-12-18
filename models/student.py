# import sqlite3

# class Student:
#     def __init__(self, name, age, year, student_id=None):
#         self.id = student_id
#         self.name = name
#         self.age = age
#         self.year = year

#     def save(self):
#         # Connect to the database
#         conn = sqlite3.connect('student_management.db')
#         cursor = conn.cursor()

#         if self.id is None:
#             # If no ID, insert new student
#             cursor.execute('''
#                 INSERT INTO students (name, age, year) 
#                 VALUES (?, ?, ?)
#             ''', (self.name, self.age, self.year))
#             self.id = cursor.lastrowid  # Retrieve the ID of the newly inserted row
#         else:
#             # If ID exists, update the existing student
#             cursor.execute('''
#                 UPDATE students 
#                 SET name = ?, age = ?, year = ? 
#                 WHERE id = ?
#             ''', (self.name, self.age, self.year, self.id))

#         conn.commit()
#         conn.close()

#     @staticmethod
#     def get_all():
#         conn = sqlite3.connect('student_management.db')
#         cursor = conn.cursor()

#         cursor.execute('SELECT * FROM students')
#         rows = cursor.fetchall()

#         students = []
#         for row in rows:
#             student = Student(row[1], row[2], row[3], row[0])  # row[0] is the id
#             students.append(student)

#         conn.close()
#         return students


import sqlite3

class Student:
    def __init__(self, id=None, name=None, age=None):
        self.id = id
        self.name = name
        self.age = age
    
    @staticmethod
    def get_all():
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        students = []
        for row in rows:
            student = Student(id=row[0], name=row[1], age=row[2])
            students.append(student)
        conn.close()
        return students
    
    @staticmethod
    def get_by_id(student_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Student(id=row[0], name=row[1], age=row[2])
        else:
            return None

    def save(self):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        
        if self.id is None:  # New student, insert into the table
            cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (self.name, self.age))
        else:  # Existing student, update their details
            cursor.execute("UPDATE students SET name = ?, age = ? WHERE id = ?", (self.name, self.age, self.id))
        
        conn.commit()
        conn.close()

    @staticmethod
    def delete(student_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()

    # Enroll the student in a course
    def enroll(self, course_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (self.id, course_id))
        conn.commit()
        conn.close()

    # Get all courses a student is enrolled in
    def get_enrolled_courses(self):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT c.id, c.course_title, c.course_duration 
            FROM courses c
            JOIN enrollments e ON c.id = e.course_id
            WHERE e.student_id = ?
        ''', (self.id,))
        courses = cursor.fetchall()
        conn.close()
        return courses
