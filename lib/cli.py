# cli.py
from models import session, Student, Course, Enrollment

def validate_input(prompt, data_type, condition):
    while True:
        try:
            value = data_type(input(prompt))
            if condition(value):
                return value
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input type. Please enter a valid value.")

def is_positive(value):
    return value>0

# Create a new student and save to the database
def create_student():
    name = input("Enter student's name: ")
    age = validate_input("Enter student's age: ", int, is_positive)
    year = validate_input("Enter student's year: ", int, is_positive)
    # id = validate_input("Enter student id", int, is_positive)

    #  Create the student object and add it to the session.
    student = Student(name=name, age=age, year=year)
    session.add(student)
    session.commit()
    print(f"Student {name} added successfully!")
 
# List all students in the database.
def list_students():
    students = Student.view_students(session)  # Fetch students from the database
    if students:
        for student in students:
            # Use dot notation to access attributes
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}")
    else:
        print("No students found.")

def is_positive_integer(value):
    return isinstance(value, int) and value > 0

# Deleting a student from the database.
def delete_student_by_id():
    student_id = validate_input("Enter student's ID to delete: ", int, condition=is_positive_integer)
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student {student_id} deleted successfully!")
    else:
        print(f"No student found with ID {student_id}.")
          


# Create a new course and save to the database.
def create_course():
    course_title = input("Enter course title: ")
    course_duration = validate_input("Enter course duration (hours): ", int, is_positive)
    #course_id = validate_input("Enter the course id:",int, is_positive )
    course = Course(course_title=course_title, course_duration=course_duration)
    session.add(course)
    session.commit()
    print(f"Course {course_title} added successfully!")

# List all courses in the database.
def list_courses():
    courses = Course.view_courses(session)  # Fetch courses from the database
    if courses:
        for course in courses:
            # Use dot notation to access attributes
            print(f"ID: {course.id}, Title: {course.course_title}, Duration: {course.course_duration}")
    else:
        print("No courses found.")


# Deleting a course from the database.
def delete_course_by_id():
    course_id =validate_input("Enter course ID to delete: ", int, condition=is_positive_integer)
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        session.delete(course)
        session.commit()
        print(f"Course {course_id} deleted successfully!")
    else:
        print(f"No course found with ID {course_id}.")


# Displays the main menu and handles user options.
def main_menu():
    options = {
         '1': ('Create Student', create_student),
    '2': ('List Students', list_students),
    '3': ('Delete Student', delete_student_by_id),
    '4': ('Create Course', create_course),
    '5': ('List Courses', list_courses),
    '6': ('Delete Course', delete_course_by_id),
    '0': ('Exit', exit)
    }

    while True:
        print("\nMain Menu:")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        
        choice = input("Choose an option: ")
        if choice in options:
            options[choice][1]()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()