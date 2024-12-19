import sqlite3

class Student:
    def __init__(self, name, age, year, student_id=None):
        self.id = student_id
        self.name = name
        self.age = age
        self.year = year

    def save(self):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute('''
                INSERT INTO students (name, age, year) 
                VALUES (?, ?, ?)
            ''', (self.name, self.age, self.year))
            self.id = cursor.lastrowid  
        else:
    
            cursor.execute('''
                UPDATE students 
                SET name = ?, age = ?, year = ? 
                WHERE id = ?
            ''', (self.name, self.age, self.year, self.id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM students')
        rows = cursor.fetchall()

        students = []
        for row in rows:
            student = Student(row[1], row[2], row[3], row[0])  
            students.append(student)

        conn.close()
        return students
