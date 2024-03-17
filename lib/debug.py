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

    print(Class_Name.find_by_id(3))
    print(Student.find_by_id(2))

    name = "john smith"
    print(name.title())
    obj = Student.find_by_name(name.title())
    print(obj)
    classes = Student.get_classes(obj)
    print(classes)
    # students = Teacher.get_students(obj)
    # print(students)

debug()