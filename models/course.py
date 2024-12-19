import sqlite3

class Course:
    def __init__(self, course_title, course_duration, course_id=None):
        self.id = course_id  # Make sure id is passed, or set as None
        self.course_title = course_title
        self.course_duration = course_duration

    def save(self):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()

        if self.id is None:
            # If no id, insert a new course
            cursor.execute('''
                INSERT INTO courses (course_title, course_duration)
                VALUES (?, ?)
            ''', (self.course_title, self.course_duration))
            self.id = cursor.lastrowid  # Auto-generated ID
        else:
            # If id exists, update the existing course
            cursor.execute('''
                UPDATE courses
                SET course_title = ?, course_duration = ?
                WHERE id = ?
            ''', (self.course_title, self.course_duration, self.id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM courses')
        rows = cursor.fetchall()

        courses = []
        for row in rows:
            # Assuming the first column in each row is the id (index 0)
            course = Course(row[1], row[2], row[0])  # row[0] is the id
            courses.append(course)

        conn.close()
        return courses
