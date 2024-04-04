# lib/helpers.py

from models.__init__ import CONN, CURSOR
from models.teacher import Teacher
from models.student import Student
from models.student_class_name import Student_Class_Name
# from models.teacher_class_name import Teacher_Class_Name
from models.class_name import Class_Name
from models.report import Report

### Admin actions ###
            
def search_teachers(name=""):
    print("Search teachers:")
    if name == "":
        name = input("Enter name (blank to exit):")
    if name == "":
        return
    teacher = Teacher.find_by_name(name.title())
    if teacher:
        classes = teacher.get_classes()
        students = teacher.get_students()
        print("********")
        print(teacher)
        print("Classes:")
        for item in classes:
            print(f"    * {item.name}")
        print("Students:")
        for item in students:
            print(f"    * {item.name}")
        print("********")
    else:
        print("********")
        print(f"Teacher {name} not found")
        print("********")

def search_students(name=""):
    print("Search students (blank to exit):")
    if name == "":
        name = input("Enter name:").capitalize()
    if name == "":
        return
    student = Student.find_by_name(name.title())
    if student:
        classes = student.get_classes()
        print("********")
        print(student)
        print("Classes:")
        for item in classes:
            print(f"    * {item.name}")
            print(f"        Teacher: {item.get_teacher_name()}")
        print("********")
    else:
        print("********")
        print(f"Student {name} not found")
        print("********")

def search_classes():
    print("Search classes")
    name = input("Enter name (blank to exit):").capitalize()
    if name == "":
        return
    class_name = Class_Name.find_by_name(name.title())
    if class_name:
        print("********")
        print("Teacher:")
        print(f"    * {class_name.get_teacher_name()}")
        students = class_name.get_students()
        print("Student(s):")
        for item in students:
            print(f"    * {item.name}")
        print("********")
    else:
        print("********")
        print(f"Class {name} not found")
        print("********")

def add_student():
    print("Add Student:")
    print("********")
    name = select_name(Student)
    if name == "":
        return
    student = Student(name.title())
    student.save()
    student_add_classes(student)
    print("********")
    print(f"New Student Added:")
    print(student)
    print("Classes:")
    classes = student.get_classes()
    for item in classes:
        print("    * ", item)
        print("      * Teacher:", item.get_teacher_name())
    print("********")

def add_teacher():
    print("Add Teacher:")
    print("********")
    name = select_name(Teacher)
    if name == "":
        return
    teacher = Teacher(name.title())
    teacher.save()
    teacher_add_classes(teacher)
    print("********")
    print(f"New Teacher Added:")
    print(teacher)
    print("Classes:")
    classes = teacher.get_classes()
    for item in classes:
        print("    * ", item)
    print("Students:")
    students = teacher.get_students()
    for item in students:
        print("    * ", item)
    print("********")

def add_class_name():
    print("Add Class:")
    print("********")
    name = select_name(Class_Name)
    if name == "":
        return
    print("********")
    teacher = select_obj(Teacher)
    if not teacher:
        class_name = Class_Name(name.title())
    else:
        class_name = Class_Name(name.title(), teacher.id)
    class_name.save()
    students = add_objs(Student, class_name)
    print("********")
    print(f"New Class Added:")
    print(class_name)
    print("Teacher:")
    teacher = class_name.get_teacher()
    if teacher:
        print("    * ", teacher)
    else:
        print("    * None")
    print("Students:")
    students = class_name.get_students()
    for item in students:
        print("    * ", item)

# def add_obj(cls):
#     print(f"Add {cls.__name__}:")
#     print("********")
#     name = select_name(cls)
#     if name == "":
#         return
#     obj = cls(name.title())
#     obj.save()
#     if cls is Teacher or cls is Student:
#         add_objs(Class_Name, obj)
#     if cls is Class_Name:
#         add_objs(Teacher, obj)
#         add_objs(Student, obj)
#     print("********")
#     print(f"New {cls.__name__} Added:")
#     print(obj)
#     if cls is Teacher:
#         print("Teachers:")
#         classes = obj.get_classes()
#         students = obj.get_students()
#         print("Classes:")
#         for item in classes:
#             print("    * ", item)
#         print("Students:")
#         for item in students:
#             print("    * ", item)
#     if cls is Student:
#         print("Classes:")
#         classes = obj.get_classes()
#         for item in classes:
#             print("    * ", item)
#     if cls is Class_Name:
#         print("Teacher:")
#         print("    * ", obj.get_teacher().name)
#         students = obj.get_students()
#         print("Students:")
#         for item in students:
#             print("    * ", item)
#     print("********")

def admin_search_reports(cls):
    if cls is Class_Name:
        class_name = select_obj(cls)
        if class_name is None:
            return
        student = select_obj(Student, class_name.get_students())
        if student is None:
            return
    elif cls is Teacher:
        teacher = select_obj(cls)
        if teacher is None:
            return
        class_name = select_obj(Class_Name, teacher.get_classes())
        if class_name is None:
            return
        student = select_obj(Student, class_name.get_students())
        if student is None:
            return
    elif cls is Student:
        student = select_obj(cls)
        if student is None:
            return
        class_name = select_obj(Class_Name, student.get_classes())
        if class_name is None:
            return
    report = Report.find_by_ids(class_name.id, student.id)
    if report:
        print(report)
    else:
        print("No reports found")

def admin_remaining_reports():
    print("Remaining reports:")
    classes = Class_Name.get_all()
    for class_name in classes:
        students = class_name.get_students()
        reports = Report.get_class_reports(class_name.id)
        print(f"Class {class_name.name}:")
        print(f"Teacher {class_name.get_teacher_name()}:")
        for student in students:
            if student.id not in [report.student_id for report in reports]:
                print(f"    * {student.name}")
        print("********")
        

### Teacher actions ###

def teacher_info():
    print("Please select a teacher:")
    teacher = select_obj(Teacher)
    if teacher is None:
        return
    search_teachers(teacher.name)

def teacher_update_info():
    print("Please select a teacher:")
    teacher = select_obj(Teacher)
    if teacher is None:
        return
    print("********")
    update_obj(Teacher, teacher)

def teacher_view_reports():
    teacher = select_obj(Teacher)
    if teacher is None:
        return
    reports = teacher.get_reports()
    for item in reports:
        print(f"Class: {Class_Name.find_by_id(item.class_name_id).name}, Student: {Student.find_by_id(item.student_id).name}")
        print(f"Report: {item.text}")
    if reports == []:
        print("No reports found")

def teacher_write_report():
    from curses_text_editor import enter_text_editor, get_text
    teacher = select_obj(Teacher)
    if teacher is None:
        return
    class_name = select_obj(Class_Name, teacher.get_classes())
    if class_name is None:
        return
    student = select_obj(Student, class_name.get_students())
    if student is None:
        return
    report = Report.find_by_ids(class_name.id, student.id)
    if report is not None:
        enter_text_editor(report.text)
        report.text = get_text()
        report.update()
        print(f"Report updated: {report}")
    else:
        enter_text_editor()
        report = get_text()
        new_report = Report.create(report, class_name.id, student.id)
        print(f"Report created: {new_report}")

def teacher_delete_report():
    teacher = select_obj(Teacher)
    if teacher is None:
        return
    class_name = select_obj(Class_Name, teacher.get_classes())
    if class_name is None:
        return
    student = select_obj(Student, class_name.get_students())
    if student is None:
        return
    report = Report.find_by_ids(class_name.id, student.id)
    if report is not None:
        report.delete()
        print(f"Report deleted: {report}")
    else:
        print(f"Report not found: {report}")

def teacher_remaining_reports():
    teacher = select_obj(Teacher)
    if teacher is None:
        return
    classes = teacher.get_classes()
    reports = teacher.get_reports()
    for cls in classes:
        class_students = cls.get_students()
        print(f"{cls.name} Reports Remaining:")
        for student in class_students:
            if student.id not in [report.student_id for report in reports]:
                print(f"    * {student.name}")
        print("********")


### Student actions ###

def student_view_reports():
    student = select_obj(Student)
    if student is None:
        return
    reports = student.get_reports()
    print("********")
    for item in reports:
        class_name = Class_Name.find_by_id(item.class_name_id)
        print(f"Class: {class_name.name}, Teacher: {class_name.get_teacher_name()}")
        print(f"Report: {item.text}")
    if reports == []:
        print("No reports found")
    print("********")

def student_info():
    print("Please select a student:")
    student = select_obj(Student)
    if student is None:
        return
    search_students(student.name)

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
    name = input(f"Enter {cls.__name__} name to delete (or blank to exit):")
    if name == "":
        return
    obj = cls.find_by_name(name.title())
    if obj:
        obj.delete()
        print(f"{cls.__name__} {name} deleted")
    else:
        print(f"{cls.__name__} {name} not found")
    print("********")

def select_name(cls):
    while True:
        name = input(f"Enter {cls.__name__} name (blank to exit):")
        if cls.find_by_name(name.title()):
            print(f"{cls.__name__} {name} already exists")
            name = ""
        elif name == "exit":
            print("Exiting...")
            exit()
        elif name == "":
            break
        else:
            break
    return name

def update_name(obj):
    new_name = input("Enter new name (or blank to keep current):")
    if new_name:
        obj.name = new_name.title()
        obj.update()

def update_obj(cls, obj=None):
    print("Update " + cls.__name__ + ":")
    if obj is None:
        print("********")
        obj = select_obj(cls)
        if obj is None:
            return
    print("********")
    print(f"Updating {obj.name}")
    while True:
        if cls is Student:
            print("""What do you want to update?:
    • Name
    • Add Classes
    • Remove Classes
    • Exit""")
            choice = input("Select:").lower()
            if choice == "name":
                update_name(obj)
            elif choice == "add classes" or choice == "add":
                add_objs(Class_Name, obj)
            elif choice == "remove classes" or choice == "remove":
                remove_objs(Class_Name, obj)
            elif choice == "exit":
                break
        elif cls is Teacher:
            print("""What do you want to update?:
    • Name
    • Add Classes
    • Remove Classes
    • Exit""")
            choice = input("Select:").lower()
            if choice == "name":
                update_name(obj)
            elif choice == "add classes" or choice == "add":
                teacher_add_classes(obj)
            elif choice == "remove classes" or choice == "remove":
                teacher_remove_classes(obj)
            elif choice == "exit":
                break
        elif cls is Class_Name:
            print("""What do you want to update?:
    • Name""")
            if obj.teacher_id == 0:
                print("    • Add Teacher")
            if obj.teacher_id != 0:
                print("    • Remove Teacher")
            print("""    • Add Students
    • Remove Students
    • Exit""")
            choice = input("Select:").lower()
            if choice == "name":
                update_name(obj)
            elif choice == "add teacher":
                class_name_add_teacher(obj)
            elif choice == "remove teacher":
                obj.teacher_id = 0
                obj.update()
                print("Teacher removed")
            elif choice == "add students":
                add_objs(Student, obj)
            elif choice == "remove students":
                remove_objs(Student, obj)
            elif choice == "exit":
                break

def select_obj(cls, obj_list=[]):
    if obj_list == []:
        obj_list = cls.get_all()
    while True:
        print("********")
        print(f"List of {cls.__name__}s:")
        for item in obj_list:
            print(item.name)
        print("********")
        name = input("Enter name to select (blank to exit):")
        if name == "":
            obj = None
            break
        elif name:
            obj = cls.find_by_name(name.title())
            if obj:
                break
            else:
                print(f"{cls.__name__} {name} not found")
        else:
            break
    return obj

def class_name_add_teacher(class_name):
    teachers_list = Teacher.get_all()
    while True:
        print("********")
        print("Teachers Available:")
        for item in teachers_list:
            print(item.name)
        print("********")
        name = input("Enter teacher name to add to class (or blank to stop):")
        if name:
            teacher = Teacher.find_by_name(name.title())
            if teacher:
                class_name.teacher_id = teacher.id
                class_name.update()
                break
            else:
                print(f"Teacher {name} not found")
        else:
            break

def student_add_classes(student):
    classes_list = Class_Name.get_all()
    enrolled_classes = student.get_classes()
    new_classes = []
    while True:
        print("********")
        print("Classes Available:")
        for item in classes_list:
            print(item.name)
        print("********")
        if len(enrolled_classes) > 0:
            print("Classes Enrolled:")
            for item in enrolled_classes:
                print(item.name)
        name = input("Enter class name to add to enrollment (or blank to stop):")
        if name:
            class_name = Class_Name.find_by_name(name.title())
            if class_name:
                new_classes.append(class_name)
                enrolled_classes.append(class_name)
            else:
                print(f"Class {name} not found")
        else:
            break
    
    for item in new_classes:
            if Student_Class_Name.find_by_class_name_id_and_student_id(item.id, student.id) is None:
                student_class_name = Student_Class_Name(item.id, student.id)
                student_class_name.save()

def teacher_add_classes(teacher):
    classes_list = Class_Name.get_all()
    classes_list = [class_name for class_name in classes_list if class_name.teacher_id == 0]
    new_classes = []
    while True:
        print("********")
        print("Classes Available:")
        for item in classes_list:
            print(item.name)
        print("********")
        name = input("Enter class name to add to enrollment (or blank to stop):")
        if name:
            class_name = Class_Name.find_by_name(name.title())
            if class_name:
                new_classes.append(class_name)
            else:
                print(f"Class {name} not found")
        else:
            break

    for item in new_classes:
        item.teacher_id = teacher.id
        item.update()

def add_objs(cls, obj):
    obj_list = cls.get_all()
    objs = set([])
    if cls is Student and obj:
        objs = set(obj.get_students())
    elif cls is Class_Name and type(obj) is Teacher:
        objs = set(obj.get_classes())
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

    if type(obj) is Student:
        for item in objs:
            if Student_Class_Name.find_by_class_name_id_and_student_id(item.id, obj.id) is None:
                student_class_name = Student_Class_Name(item.id, obj.id)
                student_class_name.save()
    if type(obj) is Class_Name:
        for item in objs:
            if Student_Class_Name.find_by_class_name_id_and_student_id(obj.id, item.id) is None:
                student_class_name = Student_Class_Name(obj.id, item.id)
                student_class_name.save()

def teacher_remove_classes(teacher):
    while True:
        print("********")
        print("Classes Available:")
        classes_list = teacher.get_classes()
        for item in classes_list:
            print(item.name)
        print("********")
        name = input("Enter class name to remove from enrollment (or blank to stop):")
        if name:
            class_name = Class_Name.find_by_name(name.title())
            if class_name:
                class_name.teacher_id = 0
                class_name.update()
            else:
                print(f"Class {name} not found")
        else:
            break

def remove_objs(cls, obj):
    curr_objs = set([])
    if cls is Student:
        curr_objs = set(obj.get_students())
    elif cls is Teacher:
        curr_objs = set(obj.get_teachers())
    elif cls is Class_Name:
        curr_objs = set(obj.get_classes())
    remove_objs_set = set([])
    while True:
        print("********")
        print(f"Current {cls.__name__}s:")
        for item in curr_objs:
            if item:
                print(item.name)
        print("********")
        name = input(f"Enter {cls.__name__.lower()} name to REMOVE (or blank to stop):")
        if name:
            new_obj = cls.find_by_name(name.title())
            if new_obj is not None:
                curr_objs.discard(new_obj)
                remove_objs_set.add(new_obj)
            else:
                print(f"{cls.__name__} {name} not found")
        else:
            break
    
    if type(obj) is Student:
        for item in remove_objs_set:
            Student_Class_Name.find_by_class_name_id_and_student_id(item.id, obj.id).delete()
    
    return

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

admin_search_reports_menu = {
    "menu_text": """How do you want to search reports?
    • Search by Teacher
    • Search by Class
    • Search by Student""",
    "search by teacher": [admin_search_reports, Teacher],
    "teacher": [admin_search_reports, Teacher],
    "search by class": [admin_search_reports, Class_Name],
    "class": [admin_search_reports, Class_Name],
    "search by student": [admin_search_reports, Student],
    "student": [admin_search_reports, Student]
}

admin_reports_info_menu = {
    "menu_text": """What info do you want to see?
    • List all reports
    • Search reports
    • View remaining reports""",
    "list all reports": [list_all, Report, "reports"],
    "list reports": [list_all, Report, "reports"],
    "list": [list_all, Report, "reports"],
    "search reports": admin_search_reports_menu,
    "search": admin_search_reports_menu,
    "view remaining reports": admin_remaining_reports,
    "view remaining": admin_remaining_reports,
    "remaining": admin_remaining_reports,
    "remaining reports": admin_remaining_reports
}
    
admin_info_menu = {
    "menu_text": """Get info on what:
    • Teachers
    • Students
    • Classes
    • Reports""",
    "teachers": admin_teachers_info_menu,
    "students": admin_students_info_menu,
    "classes": admin_classes_info_menu,
    "reports": admin_reports_info_menu
}

admin_add_menu = {
    "menu_text": """Choose what to add:
    • Teacher
    • Student
    • Class""",
    "teacher": add_teacher,
    "student": add_student,
    "class": add_class_name
}

admin_update_menu = {
    "menu_text": """Choose what to update:
    • Teacher
    • Student
    • Class""",
    "teacher": [update_obj, Teacher],
    "student": [update_obj, Student],
    "class": [update_obj, Class_Name]
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
    • Info (Teachers/Students/Classes/Reports)
    • Add (Teacher/Student/Class)
    • Update (Teacher/Student/Class)
    • Delete (Teacher/Student/Class)""",
    "info": admin_info_menu,
    "teachers info": admin_teachers_info_menu,
    "students info": admin_students_info_menu,
    "classes info": admin_classes_info_menu,
    "reports info": admin_reports_info_menu,
    "add": admin_add_menu,
    "add teacher": add_teacher,
    "add student": add_student,
    "add class": add_class_name,
    "update": admin_update_menu,
    "update teacher": [update_obj, Teacher],
    "update student": [update_obj, Student],
    "update class": [update_obj, Class_Name],
    "delete": admin_delete_menu,
    "delete teacher": [delete_row, Teacher, "teachers"],
    "delete student": [delete_row, Student, "students"],
    "delete class": [delete_row, Class_Name, "class_names"]
}

############# TEACHER MENUS #############

teacher_menu = {
    "menu_text": """Welcome, Teacher! Select what to do:
    • View Info
    • Update Info
    • View Reports
    • Write or Update Report
    • Delete Report
    • View Remaining Reports""",
    "view info": teacher_info,
    "update info": teacher_update_info,
    "view reports": teacher_view_reports,
    "write report": teacher_write_report,
    "write": teacher_write_report,
    "update report": teacher_write_report,
    "delete report": teacher_delete_report,
    "view remaining reports": teacher_remaining_reports,
    "remaining reports": teacher_remaining_reports,
    "view remaining": teacher_remaining_reports
}

############# STUDENT MENUS #############

student_menu = {
    "menu_text": """Welcome, Student! Select what to do:
    • View Info
    • View Reports""",
    "view info": student_info,
    "info": student_info,
    "view reports": student_view_reports,
    "reports": student_view_reports
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