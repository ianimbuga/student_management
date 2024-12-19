import sys
from models.student import Student
from models.course import Course
from models.enrollment import Enrollment

def main_menu():
    print("Welcome to the Student Management System")
    print("1. Create Student")
    print("2. List Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Create Course")
    print("6. List Courses")
    print("7. Update Course")
    print("8. Delete Course")
    print("9. Create Enrollment")
    print("0. Exit")

    choice = input("Choose an option: ")

    # if choice == "1":
    #     create_student()
    # elif choice == "2":
    #     list_students()
    # elif choice == "3":
    #     update_student()  
    # elif choice == "4":
    #     delete_student()  
    # elif choice == "5":
    #     create_course()
    # elif choice == "6":
    #     list_courses()
    # elif choice == "7":
    #     update_course()  
    # elif choice == "8":
    #     delete_course()  
    # elif choice == "9":
    #     create_enrollment()
    # elif choice == "0":
    #     sys.exit()
    # else:
        # print("Invalid choice, please try again.")
        # main_menu()

def create_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    year = int(input("Enter student's year: "))
    student = Student(name=name, age=age, year=year)
    student.save()
    print(f"Student {name} added successfully!")
    main_menu()

def list_students():
    students = Student.get_all()
    for student in students:
        print(f"{student.id}. {student.name} - {student.age} years old")
    main_menu()

def update_student():
    student_id = int(input("Enter the student ID to update: "))
    student = Student.find_by_id(student_id)

    if student:
        print(f"Current details - Name: {student.name}, Age: {student.age}, Year: {student.year}")
        
        name = input("Enter new name (leave blank to keep current): ")
        age = input("Enter new age (leave blank to keep current): ")
        year = input("Enter new year (leave blank to keep current): ")

        student.update(name or None, int(age) if age else None, int(year) if year else None)
        print("Student details updated successfully!")
    else:
        print("Student not found.")
    main_menu()

def delete_student():
    student_id = int(input("Enter the student ID to delete: "))
    student = Student.find_by_id(student_id)

    if student:
        student.delete()
        print("Student deleted successfully!")
    else:
        print("Student not found.")
    main_menu()

def create_course():
    course_title = input("Enter course title: ")
    duration = int(input("Enter course duration (in hours): "))
    course = Course(course_title=course_title, course_duration=duration)
    course.save()
    print(f"Course {course_title} created successfully!")
    main_menu()

def list_courses():
    courses = Course.get_all()
    for course in courses:
        print(f"{course.id}. {course.course_title} - {course.course_duration} hours")
    main_menu()

def update_course():
    course_id = int(input("Enter the course ID to update: "))
    course = Course.find_by_id(course_id)

    if course:
        print(f"Current details - Course Title: {course.course_title}, Duration: {course.course_duration} hours")
        
        title = input("Enter new title (leave blank to keep current): ")
        duration = input("Enter new duration (leave blank to keep current): ")

        course.course_title = title or course.course_title
        course.course_duration = int(duration) if duration else course.course_duration

        course.save()
        print("Course details updated successfully!")
    else:
        print("Course not found.")
    main_menu()

def delete_course():
    course_id = int(input("Enter the course ID to delete: "))
    course = Course.find_by_id(course_id)

    if course:
        course.delete()
        print("Course deleted successfully!")
    else:
        print("Course not found.")
    main_menu()

def create_enrollment():
    student_id = int(input("Enter student ID to enroll: "))
    course_id = int(input("Enter course ID to enroll in: "))
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    enrollment.save()
    print("Enrollment added successfully!")
    main_menu()

if __name__ == "__main__":
    main_menu()
