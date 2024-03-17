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

    sql = """DROP TABLE IF EXISTS student_class_name
     """

    CURSOR.execute(sql)
    CONN.commit()

    name = "nick pearson"
    print(name.title())
    obj = Student.find_by_name(name.title())
    print(obj)
    # teachers = Class_Name.get_teachers(obj)
    # print(teachers)
    # students = Teacher.get_students(obj)
    # for student in students:
    #     print(student)
    classes = Student.get_classes(obj)
    for cls in classes:
        print(cls)

    for cls in classes:
        print(cls.name)
        print(Student_Class_Name.find_by_class_name_id_and_student_id(cls.id, obj.id))

debug()