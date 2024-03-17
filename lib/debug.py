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

    sql = """DROP TABLE IF EXISTS student_class_name
     """

    CURSOR.execute(sql)
    CONN.commit()

    name = "Jameson Filliam"
    print(name.title())
    obj = Teacher.find_by_name(name.title())
    print(obj)
    # teachers = Class_Name.get_teachers(obj)
    # print(teachers)
    # students = Teacher.get_students(obj)
    # print(students)
    classes = Teacher.get_classes(obj)
    print(classes)

debug()