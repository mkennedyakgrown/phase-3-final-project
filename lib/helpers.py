# lib/helpers.py

from models.teacher import Teacher
from models.student import Student
from models.student_class_name import Student_Class_Name
from models.teacher_class_name import Teacher_Class_Name
from models.class_name import Class_Name

def go_back():
    pass

def exit_program():
    print("Goodbye!")
    exit()


def adminadd():
    print("Admin Add")


def teacher_menu():
    print("Teacher menu:")


def student_menu():
    print("Student menu:")

def admin_menu():
    print("""
Welcome, Admin!
Choose an action:
    • Add (Teacher/Student/Class)
    • Update (Teacher/Student/Class)
    • Delete (Teacher/Student/Class)
    • Go Back
    • Exit Program
    """)

    choices = {
        "add": "adminadd",
        "add teacher": admingroup,
        "add student": admingroup,
        "add class": admingroup,
        "update": admingroup,
        "update teacher": admingroup,
        "update student": admingroup,
        "update class": admingroup,
        "delete": admingroup,
        "delete teacher": admingroup,
        "delete student": admingroup,
        "delete class": admingroup,
        "go back": "go_back",
        "exit": "exit_program"
    }
    choice = input("").lower()
    if choice in choices:
        pass
    else:
        print("Invalid choice. Please try again.")
