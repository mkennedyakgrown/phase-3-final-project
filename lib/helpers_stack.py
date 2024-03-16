# lib/helpers.py
from types import FunctionType as function
from models.__init__ import CONN, CURSOR

from models.teacher import Teacher
from models.student import Student
from models.student_class_name import Student_Class_Name
from models.teacher_class_name import Teacher_Class_Name
from models.class_name import Class_Name

menu_stack = []

def show_menu(menu_items):
    while True:
        ### Display menu ###
        print(menu_items["menu_text"])
        if len(menu_stack) > 0:
            print("    • Go Back")
        print("    • Exit Program")

        ### Get user choice ###
        choice = input("").lower()

        ### Process user choice ###
        if choice in menu_items and choice != "menu_text":
            menu_stack.append(menu_items)

            ### If the menu item is a dictionary, display the sub-menu ###
            if type(menu_items[choice]) == dict:
                show_menu(menu_items[choice])

            ### If the menu item is a function, call it ###
            elif type(menu_items[choice]) == function:
                menu_items[choice]()
                prev_menu = menu_stack.pop()
                show_menu(prev_menu)

            ### If the menu item is a list, call the function using parameters ###
            elif type(menu_items[choice]) == list:
                menu_items[choice][0](menu_items[choice][1], menu_items[choice][2])
                prev_menu = menu_stack.pop()
                show_menu(prev_menu)

        elif choice == "go back":
            if len(menu_stack) > 0:
                prev_menu = menu_stack.pop()
                show_menu(prev_menu)
            else:
                print("Cannot go back further.")
        elif choice == "exit" or choice == "quit" or choice == "exit program":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

### Admin actions ###
            
def search_teachers():
    print("Search teachers:")
    name = input("Enter name:")
    teacher = Teacher.find_by_name(name)
    classes = teacher.get_classes()
    students = teacher.get_students()
    print(teacher)
    print("Classes:")
    for item in classes:
        print(item)
    print("Students:")
    for item in students:
        print(item)

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
    print(f"******** List of all {table.capitalize()} ********")
    obj_list = cls.get_all()
    for item in obj_list:
        print(item)

def delete(cls, table):
    print(cls, table)

############# ADMIN MENUS #############

admin_teachers_info_menu = {
    "menu_text": """What info do you want to see?
    • List all teachers
    • Search teachers""",
    "list all teachers": [list_all, Teacher, "teachers"],
    "list teachers": [list_all, Teacher, "teachers"],
    "list": [list_all, Teacher, "teachers"],
    "search teachers": search_teachers,
    "search": search_teachers
}

admin_students_info_menu = {
    "menu_text": """What info do you want to see?
    • List all students
    • Search students""",
    "list all students": [list_all, Student, "students"],
    "list students": [list_all, Student, "students"],
    "list": [list_all, Student, "students"],
    "search students": search_students,
    "search": search_students
}

admin_classes_info_menu = {
    "menu_text": """What info do you want to see?
    • List all classes
    • Search classes""",
    "list all classes": [list_all, Class_Name, "class_names"],
    "list classes": [list_all, Class_Name, "class_names"],
    "list": [list_all, Class_Name, "class_names"],
    "search classes": search_classes,
    "search": search_classes
}
    
admin_info_menu = {
    "menu_text": """Get info on what:
    • Teachers
    • Students
    • Classes""",
    "teachers": admin_teachers_info_menu,
    "students": admin_students_info_menu,
    "classes": admin_classes_info_menu
}

admin_add_menu = {
    "menu_text": """Choose what to add:
    • Teacher
    • Student
    • Class""",
    "teachers": add_teacher,
    "students": add_student,
    "classes": add_class
}

admin_update_menu = {
    "menu_text": """Choose what to update:
    • Teacher
    • Student
    • Class""",
    "teachers": update_teacher,
    "students": update_student,
    "classes": update_class
}

admin_delete_menu = {
    "menu_text": """Choose what to delete:
    • Teacher
    • Student
    • Class""",
    "teacher": [delete, Teacher, "teachers"],
    "student": [delete, Student, "students"],
    "class": [delete, Class_Name, "class_names"]
}

admin_menu = {
    "menu_text": """Welcome, Admin! Select what to do:
    • Info (Teachers/Students/Classes)
    • Add (Teacher/Student/Class)
    • Update (Teacher/Student/Class)
    • Delete (Teacher/Student/Class)""",
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

############# TEACHER MENUS #############

teacher_menu = {
    "Write Report": write_report,
}

############# STUDENT MENUS #############

student_menu = {
    "View Reports": student_view_reports,
}

############# MAIN MENU #############

main_menu_text = """Choose your role:
    • Admin
    • Teacher
    • Student"""

main_menu = {
    "menu_text": main_menu_text,
    "admin": admin_menu,
    "teacher": teacher_menu,
    "student": student_menu
}