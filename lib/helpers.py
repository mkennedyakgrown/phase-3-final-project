# lib/helpers.py
import click

from models.teacher import Teacher
from models.student import Student
from lib.models.student_class_name import Student_Class_Name
from lib.models.teacher_class_name import Teacher_Class_Name
from lib.models.class_name import Class_Name
from models.report import Report

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
