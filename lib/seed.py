#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.teacher import Teacher
from models.student import Student
from models.class_name import Class_Name

def seed_database():
    Teacher.drop_table()
    Student.drop_table()
    Class_Name.drop_table()
    Teacher.create_table()
    Student.create_table()
    Class_Name.create_table()

    # Create seede data
    Teacher.create("Dr. Smith")
    Teacher.create("Dr. Jones")
    Teacher.create("Dr. Brown")
    Teacher.create("Dr. Miller")
    Teacher.create("Dr. Wilson")
    Teacher.create("Dr. Davis")
    Student.create("John Smith")
    Student.create("Jane Smith")
    Student.create("John Doe")
    Student.create("Jane Doe")
    Student.create("Richard Johnson")
    Student.create("Sarah Davis")
    Student.create("Michael Thompson")
    Student.create("Emily Anderson")
    Class_Name.create("Ballet 4")
    Class_Name.create("Tap 5")
    Class_Name.create("Ballet Partnering")
    Class_Name.create("Jazz/Lyrical 2")
    Class_Name.create("Latin Rhythm/Ballroom")
    Class_Name.create("Hip Hop 8")
    Class_Name.create("Adv. Clogging")
    Class_Name.create("Pointe 1")
    
    

seed_database()
print("Database seeded.")