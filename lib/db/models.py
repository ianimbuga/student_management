from sqlalchemy import Column, String, Integer, ForeignKey, Table, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base =declarative_base()

class Student(Base):
    __tablename__= 'students'
    id= Column(Integer(),primary_key=True)
    name= Column(String())
    age= Column(Integer())
    year= Column(Integer())

    def __repr__(self):
        return f"Student {self.name} {self.age} {self.year}"
    
    @classmethod
    def view_students(cls, session):
        # Query to fetch all students
        return session.query(cls).all()
    
class Course(Base):
    __tablename__='courses'
    id= Column(Integer(), primary_key=True)
    course_title= Column(String())
    course_duration= Column(Integer())


    def __repr__(self):
     return f"Course {self.course_title} {self.course_duration}"
    
    @classmethod
    def view_courses(cls, session):
        # Query to fetch all courses
        return session.query(cls).all()

class Enrollment(Base):
   __tablename__='enrollments'
   id=Column(Integer, primary_key= True)
   student_id = Column(Integer(), ForeignKey('students.id'))
   course_id = Column(Integer, ForeignKey('courses.id'))

   def __repr__(self):
      return f"Enrollment {self.student_id} {self.course_id}"
   

engine= create_engine('sqlite:///students_database.db')
Base.metadata.create_all(engine)

Session= sessionmaker(bind=engine)
session=Session()
