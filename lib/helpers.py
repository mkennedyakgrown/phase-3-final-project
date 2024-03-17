# lib/helpers.py
from models.__init__ import CONN, CURSOR

from models.teacher import Teacher
from models.student import Student
from models.student_class_name import Student_Class_Name
from models.teacher_class_name import Teacher_Class_Name
from models.class_name import Class_Name

### Admin actions ###
            
def search_teachers():
    print("Search teachers:")
    name = input("Enter name:")
    teacher = Teacher.find_by_name(name.title())
    if teacher:
        classes = teacher.get_classes()
        students = teacher.get_students()
        print("********")
        print(teacher)
        print("Classes:")
        for item in classes:
            print(item)
        print("Students:")
        for item in students:
            print(item)
        print("********")
    else:
        print("********")
        print(f"Teacher {name} not found")
        print("********")

def search_students():
    print("Search students:")
    name = input("Enter name:").capitalize()
    student = Student.find_by_name(name.title())
    if student:
        classes = student.get_classes()
        print("********")
        print(student)
        print("Classes:")
        for item in classes:
            print(item)
        print("********")
    else:
        print("********")
        print(f"Student {name} not found")
        print("********")

def search_classes():
    print("Search classes")
    name = input("Enter name:").capitalize()
    class_name = Class_Name.find_by_name(name.title())
    if class_name:
        teachers = class_name.get_teachers()
        print("********")
        print("Teacher(s):")
        for item in teachers:
            print(item)
        students = class_name.get_students()
        print("Student(s):")
        for item in students:
            print(item)
        print("********")
    else:
        print("********")
        print(f"Class {name} not found")
        print("********")

def add_teacher():
    print("Add teacher:")
    print("********")
    name = ""
    while True:
        name = input("Enter new teacher name:")
        if name:
            break
        else:
            print("Name cannot be blank")
    classes_list = Class_Name.get_all()
    classes = []
    while True:
        print("********")
        print("Classes Available:")
        for item in classes_list:
            print(item.name)
        print("********")
        print("Assigned Classes:")
        for item in classes:
            if item:
                print(item.name)
        print("********")
        class_name = input("Enter class name (or blank to stop):")
        if class_name:
            new_class = Class_Name.find_by_name(class_name.title())
            if new_class:
                classes.append(new_class)
            else:
                print(f"Class {class_name} not found")
        else:
            break
    teacher = Teacher(name.title())
    teacher.save()
    for item in classes:
        teacher_class_name = Teacher_Class_Name(item.id, teacher.id)
        teacher_class_name.save()
    print("********")
    print("New Teacher Added:")
    print(teacher)
    print(teacher.get_classes())
    print("********")

def add_student():
    print("Add student:")
    print("********")
    name = ""
    while True:
        name = input("Enter new student name:")
        if name:
            break
        else:
            print("Name cannot be blank")
    classes_list = Class_Name.get_all()
    classes = []
    while True:
        print("********")
        print("Classes Available:")
        for item in classes_list:
            print(item.name)
        print("********")
        print("Assigned Classes:")
        for item in classes:
            if item:
                print(item.name)
        print("********")
        class_name = input("Enter class name (or blank to stop):")
        if class_name:
            new_class = Class_Name.find_by_name(class_name.title())
            if new_class:
                classes.append(new_class)
            else:
                print(f"Class {class_name} not found")
        else:
            break
    student = Student(name.title())
    student.save()
    for item in classes:
        student_class_name = Student_Class_Name(item.id, student.id)
        student_class_name.save()
    print("********")
    print("New Student Added:")
    print(student)
    print(student.get_classes())
    print("********")

def add_class():
    print("Add Class:")

def update_teacher():
    print("Update teacher:")

def update_student():
    print("Update student:")

def update_class():
    print("Update Class:")

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
    print("****************************************")

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
    "teacher": add_teacher,
    "student": add_student,
    "class": add_class
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