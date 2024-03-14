# lib/helpers.py

from models.teacher import Teacher
from models.student import Student
from models.student_class_name import Student_Class_Name
from models.teacher_class_name import Teacher_Class_Name
from models.class_name import Class_Name

def show_menu(menu_items, menu_text):
    while True:
        print(menu_text)
        for key in menu_items:
            print(f"    • {key.capitalize()}")
        choice = input("").lower()
        if choice in menu_items:
            menu_items[choice]()
        else:
            print("Invalid choice. Please try again.")

def list_all(cls, table):
    print(cls, table)

def search_teachers(cls, table):
    print(cls, table)

def search_students(cls, table):
    print(cls, table)

def search_classes(cls, table):
    print(cls, table)

def add_teacher(cls, table):
    print(cls, table)

def add_student(cls, table):
    print(cls, table)

def add_class(cls, table):
    print(cls, table)

def update_teacher(cls, table):
    print(cls, table)

def update_student(cls, table):
    print(cls, table)

def update_class(cls, table):
    print(cls, table)

def delete(cls, table):
    print(cls, table)

admin_menu = {
    "teachers info": teachers_info_menu,
    "students info": students_info_menu,
    "classes info": classes_info_menu,
    "add teacher": add_teacher,
    "add student": add_student,
    "add class": add_class,
    "update teacher": update_teacher,
    "update student": update_student,
    "update class": update_class,
    "delete teacher": [delete, Teacher, "teachers"],
    "delete student": [delete, Student, "students"],
    "delete class": [delete, Class_Name, "class_names"]
}

admin_menu_text = """Welcome, Admin! Select what to do:
    • List (Teachers/Students/Classes)
    • Add (Teacher/Student/Class)
    • Update (Teacher/Student/Class)
    • Delete (Teacher/Student/Class)
    • Go Back
    • Exit Program
    """

admin_teachers_info_menu = {
    "list teachers": [list_all, Teacher, "teachers"],
    "search teachers": search_teachers
}

admin_add_menu = {
    "teachers": add_teacher,
    "students": add_student,
    "classes": add_class
}

admin_update_menu = {
    "teachers": update_teacher,
    "students": update_student,
    "classes": update_class
}

admin_delete_menu = {
    "teachers": [delete, Teacher, "teachers"],
    "students": [delete, Student, "students"],
    "classes": [delete, Class_Name, "class_names"]
}

teacher_menu = {
    "Write Report": write_report_menu,
}

student_menu = {
    "View Reports": view_report_menu,
}

nav_choices = {
    "admin": admin_menu,
    "teacher": teacher_menu,
    "student": student_menu
}