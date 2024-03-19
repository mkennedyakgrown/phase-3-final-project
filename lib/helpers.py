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
    name = select_name(Teacher)
    teacher = Teacher(name.title())
    teacher.save()
    classes = select_objs(Class_Name, teacher)
    for item in classes:
        teacher_class_name = Teacher_Class_Name(item.id, teacher.id)
        teacher_class_name.save()
    print("********")
    print("New Teacher Added:")
    print(teacher)
    print("Classes:")
    for item in classes:
        print("    * ", item)
    students = teacher.get_students()
    print("Students:")
    for item in students:
        print("    * ", item)
    print("********")

def add_student():
    print("Add student:")
    print("********")
    name = select_name(Student)
    student = Student(name.title())
    student.save()
    classes = select_objs(Class_Name, student)
    for item in classes:
        student_class_name = Student_Class_Name(item.id, student.id)
        student_class_name.save()
    print("********")
    print("New Student Added:")
    print(student)
    classes = student.get_classes()
    print("Classes:")
    for item in classes:
        print("    * ", item)
    print("********")

def add_class():
    print("Add Class:")
    print("********")
    name = select_name(Class_Name)
    class_ = Class_Name(name.title())
    class_.save()
    teachers = select_objs(Teacher, class_)
    students = select_objs(Student, class_)
    for item in teachers:
        teacher_class_name = Teacher_Class_Name(class_.id, item.id)
        teacher_class_name.save()
    for item in students:
        student_class_name = Student_Class_Name(class_.id, item.id)
        student_class_name.save()
    print("********")
    print("New Class Added:")
    print(class_)
    print("Teachers:")
    for item in teachers:
        print("    * ", item)
    print("Students:")
    for item in students:
        print("    * ", item)
    print("********")

def update_teacher():
    print("Update teacher:")
    print("********")
    name = ""
    teachers = Teacher.get_all()
    while True:
        print("********")
        print("Teachers Available:")
        for item in teachers:
            print(item.name)
        print("********")
        name = input("Select Teacher to update:")
        if Teacher.find_by_name(name.title()):
            break
        elif name == "exit":
            print("Exiting...")
            exit()
        else:
            print(f"Teacher {name} not found")
            name = ""
    teacher = Teacher.find_by_name(name.title())
    print("********")
    print(f"Updating Teacher {teacher.name}...")
    update_name(teacher)
    print("********")
    classes = select_objs(Class_Name, teacher)
    classes = remove_classes(teacher, classes)
    for item in classes:
        if Teacher_Class_Name.find_by_class_name_id_and_teacher_id(item.id, teacher.id) is None:
            teacher_class_name = Teacher_Class_Name(item.id, teacher.id)
            teacher_class_name.save()
    print("********")
    print(f"Teacher {teacher.name} Updated:")
    print(teacher)
    classes = teacher.get_classes()
    students = teacher.get_students()
    print("Classes:")
    for item in classes:
        print("    * ", item.name)
    print("Students:")
    for item in students:
        print("    * ", item.name)
    
    print("********")

def update_student():
    print("Update student:")
    print("********")
    student = select_obj(Student)
    print("********")
    print(f"Updating Student {student.name}...")
    update_name(student)
    print("********")
    classes = select_objs(Class_Name, student)
    classes = remove_classes(student, classes)
    for item in classes:
        if Student_Class_Name.find_by_class_name_id_and_student_id(item.id, student.id) is None:
            student_class_name = Student_Class_Name(item.id, student.id)
            student_class_name.save()
    print("********")
    print(f"Student {student.name} Updated:")
    print(student)
    classes = student.get_classes()
    print ("Classes:")
    for item in classes:
        print("    * ", item.name)
    print("********")

def update_class():
    print("Update Class:")
    print("********")
    class_name = select_obj(Class_Name)
    print("********")
    print(f"Updating Class {class_name.name}...")
    update_name(class_name)
    print("********")
    teachers = select_objs(Teacher, class_name)
    teachers = remove_teachers(class_name, teachers)
    students = select_objs(Student, class_name)
    students = remove_students(class_name, students)
    for item in teachers:
        if Teacher_Class_Name.find_by_class_name_id_and_teacher_id(class_name.id, item.id) is None:
            teacher_class_name = Teacher_Class_Name(class_name.id, item.id)
            teacher_class_name.save()
    for item in students:
        if Student_Class_Name.find_by_class_name_id_and_student_id(class_name.id, item.id) is None:
            student_class_name = Student_Class_Name(class_name.id, item.id)
            student_class_name.save()
    print("********")
    print(f"Class {class_name.name} Updated:")
    print(class_name)
    teachers = class_name.get_teachers()
    students = class_name.get_students()
    print("Teachers:")
    for item in teachers:
        print("    * ", item.name)
    print("Students:")
    for item in students:
        print("    * ", item.name)
    print("********")

### Teacher actions ###
    
def write_report(teacher):
    print(teacher)

def teacher_view_reports(teacher):
    print(teacher)

def teacher_view_classes(teacher):
    print(teacher)

def teacher_view_students(teacher):
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

def delete_row(cls, row):
    print("********")
    print(f"Available {cls.__name__}s:")
    obj_list = cls.get_all()
    for item in obj_list:
        print(item)
    print("********")
    name = input(f"Enter {cls.__name__} name to delete:")
    obj = cls.find_by_name(name.title())
    if obj:
        obj.delete()
        print(f"{cls.__name__} {name} deleted")
    else:
        print(f"{cls.__name__} {name} not found")
    print("********")

def select_name(cls):
    while True:
        name = input(f"Enter {cls.__name__} name:")
        if cls.find_by_name(name.title()):
            print(f"{cls.__name__} {name} already exists")
            name = ""
        elif name == "exit":
            print("Exiting...")
            exit()
        elif name == "":
            print("Name cannot be blank")
        else:
            break
    return name

def update_name(obj):
    new_name = input("Enter new name (or blank to keep current):")
    if new_name:
        obj.name = new_name.title()
        obj.save()

def select_obj(cls):
    obj_list = cls.get_all()
    while True:
        print("********")
        print(f"List of {cls.__name__}s:")
        for item in obj_list:
            print(item.name)
        print("********")
        name = input("Enter name to select:")
        if name:
            obj = cls.find_by_name(name.title())
            if obj:
                break
            else:
                print(f"{cls.__name__} {name} not found")
        else:
            break
    return obj

def select_objs(cls, obj):
    obj_list = cls.get_all()
    objs = set([])
    if cls is Student and obj:
        objs = set(obj.get_students())
    elif cls is Teacher and obj:
        objs = set(obj.get_teachers())
    elif cls is Class_Name and obj:
        objs = set(obj.get_classes())
    while True:
        print("********")
        print(f"{cls.__name__}s Available:")
        for item in obj_list:
            print(item.name)
        print("********")
        print(f"Selected {cls.__name__}s:")
        for item in objs:
            if item:
                print(item.name)
        print("********")
        name = input("Enter class name to ADD to enrollment (or blank to stop):")
        if name:
            new_obj = cls.find_by_name(name.title())
            if new_obj:
                objs.add(new_obj)
            else:
                print(f"{cls.__name__} {name} not found")
        else:
            break

    return objs

def remove_students(obj, students):
    curr_students = set(students)
    remove_students_set = set([])
    while True:
        print("********")
        print("Current Students:")
        for item in curr_students:
            if item:
                print(item.name)
        print("********")
        name = input("Enter student name to REMOVE from class (or blank to stop):")
        if name:
            new_student = Student.find_by_name(name.title())
            if new_student:
                curr_students.discard(new_student)
                remove_students_set.add(new_student)
            else:
                print(f"Student {name} not found")
        else:
            break
    
    for item in remove_students_set:
        Student_Class_Name.find_by_class_name_id_and_student_id(obj.id, item.id).delete()

    return curr_students

def remove_teachers(obj, teachers):
    curr_teachers = set(teachers)
    remove_teachers_set = set([])
    while True:
        print("********")
        print("Current Teachers:")
        for item in curr_teachers:
            if item:
                print(item.name)
        print("********")
        teacher_name = input("Enter teacher name to REMOVE from class (or blank to stop):")
        if teacher_name:
            new_teacher = Teacher.find_by_name(teacher_name.title())
            if new_teacher:
                curr_teachers.discard(new_teacher)
                remove_teachers_set.add(new_teacher)
            else:
                print(f"Teacher {teacher_name} not found")
        else:
            break
    
    for item in remove_teachers_set:
        Teacher_Class_Name.find_by_class_name_id_and_teacher_id(obj.id, item.id).delete()

    return curr_teachers

def remove_classes(obj, classes):
    curr_classes = set(classes)
    remove_classes_set = set([])
    while True:
        print("********")
        print("Current Classes:")
        for item in curr_classes:
            if item:
                print(item.name)
        print("********")
        name = input("Enter class name to REMOVE from enrollment (or blank to stop):")
        if name:
            new_class = Class_Name.find_by_name(name.title())
            if new_class:
                curr_classes.discard(new_class)
                remove_classes_set.add(new_class)
            else:
                print(f"Class {name} not found")
        else:
            break
    
    for item in remove_classes_set:
        if type(obj) == Student:
            Student_Class_Name.find_by_class_name_id_and_student_id(item.id, obj.id).delete()
        if type(obj) == Teacher:
            Teacher_Class_Name.find_by_class_name_id_and_teacher_id(item.id, obj.id).delete()

    return curr_classes

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
    "teacher": update_teacher,
    "student": update_student,
    "class": update_class
}

admin_delete_menu = {
    "menu_text": """Choose what to delete:
    • Teacher
    • Student
    • Class""",
    "teacher": [delete_row, Teacher, "teachers"],
    "student": [delete_row, Student, "students"],
    "class": [delete_row, Class_Name, "class_names"]
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
    "delete teacher": [delete_row, Teacher, "teachers"],
    "delete student": [delete_row, Student, "students"],
    "delete class": [delete_row, Class_Name, "class_names"]
}

############# TEACHER MENUS #############

teacher_info_menu = {
    "menu_text": """What info do you want to view?
    • View Classes
    • View Students""",
    "view classes": teacher_view_classes,
    "classes": teacher_view_classes,
    "view students": teacher_view_students,
    "students": teacher_view_students
}

teacher_update_info_menu = {
    "menu_text": """What info do you want to update?
    • Update Name
    • Update Classes""",
    "update name": select_name,
    "name": select_name
}

teacher_menu = {
    "menu_text": """Welcome, Teacher! Select what to do:
    • View Info
    • Update Info
    • Write Report""",
    "view info": teacher_info_menu,
    "view": teacher_info_menu,
    "update info": teacher_update_info_menu,
    "update": teacher_update_info_menu,
    "view reports": teacher_view_reports,
    "write report": write_report,
}

############# STUDENT MENUS #############

student_menu = {
    "view reports": student_view_reports,
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