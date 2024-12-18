# import sys
# from models.student import Student
# from models.course import Course
# from models.enrollment import Enrollment

# def main_menu():
#     print("Welcome to the Student Management System")
#     print("1. Create Student")
#     print("2. List Students")
#     print("3. Create Course")
#     print("4. List Courses")
#     print("5. Create Enrollment")
#     print("0. Exit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         create_student()
#     elif choice == "2":
#         list_students()
#     elif choice == "3":
#         create_course()
#     elif choice == "4":
#         list_courses()
#     elif choice == "5":
#         create_enrollment()
#     elif choice == "0":
#         sys.exit()
#     else:
#         print("Invalid choice, please try again.")
#         main_menu()

# def create_student():
#     name = input("Enter student's name: ")
#     age = int(input("Enter student's age: "))
#     year = int(input("Enter student's year: "))
#     student = Student(name=name, age=age, year=year)
#     student.save()
#     print(f"Student {name} added successfully!")
#     main_menu()

# def list_students():
#     students = Student.get_all()
#     for student in students:
#         print(f"{student.id}. {student.name} - {student.age} years old")
#     main_menu()

# def create_course():
#     course_title = input("Enter course title: ")
#     duration = int(input("Enter course duration (in hours): "))
#     course = Course(course_title=course_title, course_duration=duration)
#     course.save()
#     print(f"Course {course_title} created successfully!")
#     main_menu()

# def list_courses():
#     courses = Course.get_all()
#     for course in courses:
#         print(f"{course.id}. {course.course_title} - {course.course_duration} hours")
#     main_menu()

# def create_enrollment():
#     student_id = int(input("Enter student ID to enroll: "))
#     course_id = int(input("Enter course ID to enroll in: "))
#     enrollment = Enrollment(student_id=student_id, course_id=course_id)
#     enrollment.save()
#     print("Enrollment added successfully!")
#     main_menu()

# if __name__ == "__main__":
#     main_menu()


# import sqlite3
# from models.student import Student
# from models.course import Course

# def add_student():
#     name = input("Enter student name: ")
#     age = input("Enter student age: ")

#     try:
#         age = int(age)
#     except ValueError:
#         print("Invalid age. Please enter a number.")
#         return

#     student = Student(name=name, age=age)
#     student.save()
#     print(f"Student {name} added successfully!")

# def view_students():
#     students = Student.get_all()
#     if students:
#         print("List of Students:")
#         for student in students:
#             print(f"{student.id}. {student.name}, Age: {student.age}")
#             courses = student.get_enrolled_courses()
#             if courses:
#                 print("  Enrolled in courses:")
#                 for course in courses:
#                     print(f"    {course[1]} ({course[2]} hours)")
#             else:
#                 print("  Not enrolled in any courses.")
#     else:
#         print("No students found.")

# def edit_student():
#     student_id = input("Enter student ID to edit: ")

#     try:
#         student_id = int(student_id)
#     except ValueError:
#         print("Invalid ID. Please enter a number.")
#         return

#     student = Student.get_by_id(student_id)
    
#     if student:
#         print(f"Editing Student {student.id}: {student.name}, Age: {student.age}")
        
#         # Get the new details
#         new_name = input("Enter new name (leave blank to keep the current): ")
#         new_age = input("Enter new age (leave blank to keep the current): ")

#         if new_name:
#             student.name = new_name
#         if new_age:
#             try:
#                 student.age = int(new_age)
#             except ValueError:
#                 print("Invalid age. Please enter a valid number.")
#                 return

#         student.save()
#         print(f"Student {student.id} updated successfully!")
#     else:
#         print("Student not found.")

# def delete_student():
#     student_id = input("Enter student ID to delete: ")

#     try:
#         student_id = int(student_id)
#     except ValueError:
#         print("Invalid ID. Please enter a number.")
#         return

#     student = Student.get_by_id(student_id)

#     if student:
#         student.delete(student_id)
#         print(f"Student {student.id} deleted successfully!")
#     else:
#         print("Student not found.")

# def enroll_student():
#     student_id = input("Enter student ID to enroll: ")
#     course_id = input("Enter course ID to enroll in: ")

#     try:
#         student_id = int(student_id)
#         course_id = int(course_id)
#     except ValueError:
#         print("Invalid IDs. Please enter valid numbers.")
#         return

#     student = Student.get_by_id(student_id)
#     course = Course.get_by_id(course_id)

#     if student and course:
#         student.enroll(course_id)
#         print(f"Student {student.name} enrolled in {course.course_title}.")
#     else:
#         print("Student or Course not found.")

# def main_menu():
#     while True:
#         print("\nStudent Management System")
#         print("1. Add Student")
#         print("2. View Students")
#         print("3. Edit Student")
#         print("4. Delete Student")
#         print("5. Enroll Student in Course")
#         print("6. Exit")

#         choice = input("Choose an option: ")

#         if choice == '1':
#             add_student()
#         elif choice == '2':
#             view_students()
#         elif choice == '3':
#             edit_student()
#         elif choice == '4':
#             delete_student()
#         elif choice == '5':
#             enroll_student()
#         elif choice == '6':
#             print("Exiting the system...")
#             break
#         else:
#             print("Invalid option. Please try again.")

# if __name__ == "__main__":
#     main_menu()


from models import Student, Course
import sqlite3

def main_menu():
    print("Choose an option:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Enroll Student in Course")
    print("4. View Student Enrollments")
    print("5. Add Course")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        enroll_student()
    elif choice == '4':
        view_student_enrollments()
    elif choice == '5':
        create_course()
    elif choice == '6':
        exit()
    else:
        print("Invalid option. Please try again.")
        main_menu()

def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")

    try:
        age = int(age)
    except ValueError:
        print("Invalid age. Please enter a valid number.")
        return

    student = Student(name=name, age=age)
    student.save()
    print(f"Student '{student.name}' added successfully!")

def view_students():
    students = Student.all()
    if students:
        print("Students List:")
        for student in students:
            print(f"{student.id}. {student.name}, {student.age} years old")
    else:
        print("No students found.")

def enroll_student():
    student_id = input("Enter student ID to enroll: ")
    course_id = input("Enter course ID to enroll in: ")

    try:
        student_id = int(student_id)
        course_id = int(course_id)
    except ValueError:
        print("Invalid input. Please enter valid IDs.")
        return

    student = Student.get_by_id(student_id)
    if student:
        course = Course.get_by_id(course_id)
        if course:
            student.enroll(course_id)
            print(f"Student '{student.name}' enrolled in course '{course.course_title}'.")
        else:
            print("Course not found.")
    else:
        print("Student not found.")

def create_course():
    course_title = input("Enter course title: ")
    course_duration = input("Enter course duration (in hours): ")

    try:
        course_duration = int(course_duration)
    except ValueError:
        print("Invalid duration. Please enter a valid number.")
        return

    course = Course(course_title=course_title, course_duration=course_duration)
    course.save()
    print(f"Course '{course.course_title}' added successfully!")

def view_student_enrollments():
    student_id = input("Enter student ID to view enrollments: ")

    try:
        student_id = int(student_id)
    except ValueError:
        print("Invalid ID. Please enter a valid number.")
        return

    student = Student.get_by_id(student_id)
    if student:
        courses = student.view_enrollments()
        if courses:
            print(f"Student '{student.name}' is enrolled in the following courses:")
            for course in courses:
                print(course)
        else:
            print(f"Student '{student.name}' is not enrolled in any courses.")
    else:
        print("Student not found.")

# Call the main menu to start the program
main_menu()
