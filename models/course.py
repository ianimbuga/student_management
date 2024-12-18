# # models/course.py

# from models.setup import CURSOR, CONN

# class Course:
#     all = {}

#     def __init__(self, course_title, course_duration):
#         self.course_title = course_title
#         self.course_duration = course_duration

#     def __repr__(self):
#         return f"{self.course_title} ({self.course_duration} hours)"

#     def save(self):
#         sql = """
#             INSERT INTO courses (course_title, course_duration)
#             VALUES (?, ?)
#         """
#         CURSOR.execute(sql, (self.course_title, self.course_duration))
#         CONN.commit()
#         self.id = CURSOR.lastrowid
#         type(self).all[self.id] = self

#     @classmethod
#     def create(cls, course_title, course_duration):
#         course = cls(course_title, course_duration)
#         course.save()
#         return course

#     @classmethod
#     def get_all(cls):
#         sql = "SELECT * FROM courses"
#         rows = CURSOR.execute(sql).fetchall()
#         return [cls(row[1], row[2]) for row in rows]

#     @classmethod
#     def find_by_id(cls, course_id):
#         sql = "SELECT * FROM courses WHERE id = ?"
#         row = CURSOR.execute(sql, (course_id,)).fetchone()
#         if row:
#             return cls(row[1], row[2])

#     def update(self):
#         sql = """
#             UPDATE courses
#             SET course_title = ?, course_duration = ?
#             WHERE id = ?
#         """
#         CURSOR.execute(sql, (self.course_title, self.course_duration, self.id))
#         CONN.commit()

#     def delete(self):
#         sql = "DELETE FROM courses WHERE id = ?"
#         CURSOR.execute(sql, (self.id,))
#         CONN.commit()
#         del type(self).all[self.id]


# import sqlite3

# class Course:
#     def __init__(self, course_title, course_duration, course_id=None):
#         self.id = course_id  # Make sure id is passed, or set as None
#         self.course_title = course_title
#         self.course_duration = course_duration

#     def save(self):
#         conn = sqlite3.connect('student_management.db')
#         cursor = conn.cursor()

#         if self.id is None:
#             # If no id, insert a new course
#             cursor.execute('''
#                 INSERT INTO courses (course_title, course_duration)
#                 VALUES (?, ?)
#             ''', (self.course_title, self.course_duration))
#             self.id = cursor.lastrowid  # Auto-generated ID
#         else:
#             # If id exists, update the existing course
#             cursor.execute('''
#                 UPDATE courses
#                 SET course_title = ?, course_duration = ?
#                 WHERE id = ?
#             ''', (self.course_title, self.course_duration, self.id))

#         conn.commit()
#         conn.close()

#     @staticmethod
#     def get_all():
#         conn = sqlite3.connect('student_management.db')
#         cursor = conn.cursor()

#         cursor.execute('SELECT * FROM courses')
#         rows = cursor.fetchall()

#         courses = []
#         for row in rows:
#             # Assuming the first column in each row is the id (index 0)
#             course = Course(row[1], row[2], row[0])  # row[0] is the id
#             courses.append(course)

#         conn.close()
#         return courses


import sqlite3

class Course:
    def __init__(self, id=None, course_title=None, course_duration=None):
        self.id = id
        self.course_title = course_title
        self.course_duration = course_duration
    
    @staticmethod
    def get_all():
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses")
        rows = cursor.fetchall()
        courses = []
        for row in rows:
            course = Course(id=row[0], course_title=row[1], course_duration=row[2])
            courses.append(course)
        conn.close()
        return courses

    @staticmethod
    def get_by_id(course_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Course(id=row[0], course_title=row[1], course_duration=row[2])
        else:
            return None

    def save(self):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()

        if self.id is None:  # New course, insert into the table
            cursor.execute("INSERT INTO courses (course_title, course_duration) VALUES (?, ?)", (self.course_title, self.course_duration))
        else:  # Existing course, update it
            cursor.execute("UPDATE courses SET course_title = ?, course_duration = ? WHERE id = ?", (self.course_title, self.course_duration, self.id))

        conn.commit()
        conn.close()

    @staticmethod
    def delete(course_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        conn.commit()
        conn.close()
