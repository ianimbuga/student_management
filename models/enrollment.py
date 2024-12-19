# models/enrollment.py

from models.setup import CURSOR, CONN

class Enrollment:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

    def save(self):
        sql = """
            INSERT INTO enrollments (student_id, course_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.student_id, self.course_id))
        CONN.commit()

    @classmethod
    def create(cls, student_id, course_id):
        enrollment = cls(student_id, course_id)
        enrollment.save()
        return enrollment

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM enrollments"
        rows = CURSOR.execute(sql).fetchall()
        return [cls(row[1], row[2]) for row in rows]

    @classmethod
    def find_by_id(cls, enrollment_id):
        sql = "SELECT * FROM enrollments WHERE id = ?"
        row = CURSOR.execute(sql, (enrollment_id,)).fetchone()
        if row:
            return cls(row[1], row[2])

    def delete(self):
        sql = "DELETE FROM enrollments WHERE student_id = ? AND course_id = ?"
        CURSOR.execute(sql, (self.student_id, self.course_id))
        CONN.commit()
