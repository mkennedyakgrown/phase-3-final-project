# lib/helpers.py

from models.teacher import Teacher
from models.student import Student
from models.student_class_name import Student_Class_Name
from models.teacher_class_name import Teacher_Class_Name
from models.class_name import Class_Name


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
        "add teacher": [add, Teacher, "teachers"],
        "add student": [add, Student, "students"],
        "add class": [add, Class_Name, "class_names"],
        "update teacher": [update, Teacher, "teachers"],
        "update student": [update, Student, "students"],
        "update class": [update, Class_Name, "class_names"],
        "delete teacher": [delete, Teacher, "teachers"],
        "delete student": [delete, Student, "students"],
        "delete class": [delete, Class_Name, "class_names"]
    }
    choice = input("").lower()
    if choice in choices:
        choices[choice][0](choices[choice][1], choices[choice][2])
    elif choice in nav_choices:
        nav_choices[choice]()
    elif choice in action_menus:
        action_menus[choice]()
    else:
        print("Invalid choice. Please try again.")


def add_menu():
    print("""Choose what to add:
    • Teacher
    • Student
    • Class
    • Go Back
    • Exit Program
    """)

    choices = {
        "teacher": [Teacher, "teachers"],
        "student": [Student, "students"],
        "class": [Class_Name, "class_names"]
    }
    choice = input("").lower()
    if choice in choices:
        add(choices[choice][0], choices[choice][1])
    elif choice in nav_choices:
        nav_choices[choice]()
    else:
        print("Invalid choice. Please try again.")

def add(cls, table):
    print(cls, table)

def update_menu():
    print("""Choose what to update:
    • Teacher
    • Student
    • Class
    • Go Back
    • Exit Program
    """)

    choices = {
        "teacher": [Teacher, "teachers"],
        "student": [Student, "students"],
        "class": [Class_Name, "class_names"]
    }
    choice = input("").lower()
    if choice in choices:
        update(choices[choice][0], choices[choice][1])
    elif choice in nav_choices:
        nav_choices[choice]()
    else:
        print("Invalid choice. Please try again.")

def update(cls, table):
    print(cls, table)

def delete_menu():
    print("""Choose what to delete:
    • Teacher
    • Student
    • Class
    • Go Back
    • Exit Program
    """)

    choices = {
        "teacher": [Teacher, "teachers"],
        "student": [Student, "students"],
        "class": [Class_Name, "class_names"]
    }
    choice = input("").lower()
    if choice in choices:
        delete(choices[choice][0], choices[choice][1])
    elif choice in nav_choices:
        nav_choices[choice]()
    else:
        print("Invalid choice. Please try again.")

def delete(cls, table):
    print(cls, table)

def teacher_menu():
    print("Teacher menu:")


def student_menu():
    print("Student menu:")
        
def go_back():
    pass

def exit_program():
    print("Goodbye!")
    exit()
    
nav_choices = {
    "go back" : go_back,
    "exit" : exit_program
}

action_menus = {
    "add": add_menu,
    "update": update_menu,
    "delete": delete_menu
}