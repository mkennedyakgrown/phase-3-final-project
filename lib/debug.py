#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb


# ipdb.set_trace()

def debug():
    from models.teacher_class_name import Teacher_Class_Name
    from models.teacher import Teacher
    from models.class_name import Class_Name
    from models.student import Student
    from models.student_class_name import Student_Class_Name
    from models.teacher_class_name import Teacher_Class_Name
    from models.report import Report
    from text_editor_form import TextEditorApplication

    # sql = """DELETE FROM teacher_class_names
    # WHERE teacher_id > 10
    # """

    # CURSOR.execute(sql)
    # CONN.commit()

    name = "ballet 4"
    print(name.title())
    obj = Class_Name.find_by_name(name.title())
    print(obj)
    teachers = Class_Name.get_teachers(obj)
    print(teachers)
    students = Class_Name.get_students(obj)
    for student in students:
        print(student)
    classes = Student.get_classes(obj)
    for cls in classes:
        print(cls)
    report_text = Report.find_by_ids(obj.id, 2, 2).text
    TextEditorApplication.update_text(report_text)
    TextEditorApplication().run()
    report = TextEditorApplication.get_text()
    print(report)
    new_report = Report.create(report, obj.id, 2, 3)
    print(new_report)

    # for cls in classes:
    #     print(cls.name)
    #     print(Student_Class_Name.find_by_class_name_id_and_student_id(cls.id, obj.id))

    # teacher = Teacher.find_by_id(2)
    # print(teacher)
    # reports = teacher.get_reports()
    # for report in reports:
    #     print(report)

    

debug()