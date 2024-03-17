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

    teacher_name = "Dr. Brown"
    teacher = Teacher.find_by_name(teacher_name)
    print(teacher)
    teacher_classes = Teacher.get_classes(teacher)
    print(teacher_classes)
    teacher_students = Teacher.get_students(teacher)
    print(teacher_students)

debug()