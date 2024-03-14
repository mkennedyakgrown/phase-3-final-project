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

### Admin actions ###
            
def search_teachers():
    print("Search teachers")

def search_students():
    print("Search students")

def search_classes():
    print("Search classes")

def add_teacher():
    print("Add teacher")

def add_student():
    print("Add student")

def add_class():
    print("Add Class")

def update_teacher():
    print("Update teacher")

def update_student():
    print("Update student")

def update_class():
    print("Update Class")

### Teacher actions ###
    
def write_report(teacher):
    print(teacher)

### Student actions ###

def student_view_reports(student):
    print(student)

### Reuseable actions ###

def list_all(cls, table):
    print(cls, table)

def delete(cls, table):
    print(cls, table)

############# ADMIN MENUS #############

admin_teachers_info_menu = {
    "list teachers": [list_all, Teacher, "teachers"],
    "search teachers": search_teachers
}

admin_students_info_menu = {
    "list students": [list_all, Student, "students"],
    "search students": search_students
}

admin_classes_info_menu = {
    "list classes": [list_all, Class_Name, "class_names"],
    "search classes": search_classes
}
    
admin_info_menu = {
    "teachers info": admin_teachers_info_menu,
    "students info": admin_students_info_menu,
    "classes info": admin_classes_info_menu
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

admin_menu = {
    "info": admin_info_menu,
    "teachers info": admin_teachers_info_menu,
    "students info": admin_students_info_menu,
    "classes info": admin_classes_info_menu,
    "add": admin_add_menu,
    "add teacher": add_teacher,
    "add student": add_student,
    "add class": add_class,
    "update": admin_update_menu,
    "update teacher": update_teacher,
    "update student": update_student,
    "update class": update_class,
    "delete": admin_delete_menu,
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

############# TEACHER MENUS #############

teacher_menu = {
    "Write Report": write_report,
}

############# STUDENT MENUS #############

student_menu = {
    "View Reports": student_view_reports,
}

############# MISC MENUS #############

nav_choices = {
    "admin": admin_menu,
    "teacher": teacher_menu,
    "student": student_menu
}