#!/usr/bin/env python3
# lib/debug.py

import ipdb 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Student, Enrollment, Course
Base =declarative_base()
if __name__=='__main__':
    engine= create_engine('sqlite:///students_database.db')
    Base.metadata.create_all(engine)


    Session = sessionmaker(bind= engine)
    session = Session()

    Student
    
    Enrollment

    Course



ipdb.set_trace()