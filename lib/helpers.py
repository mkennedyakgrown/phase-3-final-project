# lib/helpers.py

import click

from models.teacher import Teacher
from models.student import Student
from models.student_class_name import Student_Class_Name
from models.teacher_class_name import Teacher_Class_Name
from models.class_name import Class_Name

@click.command()
def go_back():
    pass

@click.command()
def exit_program():
    print("Goodbye!")
    exit()

@click.command()
def admin_menu():
    click.echo("""
Welcome, Admin!
Choose an action:
    • Add (Teacher/Student/Class)
    • Update (Teacher/Student/Class)
    • Delete (Teacher/Student/Class)
    • Go Back
    • Exit Program
    """)

    choices = {
        "add": "admin_add",
        "add teacher": admin_group,
        "add student": admin_group,
        "add class": admin_group,
        "update": admin_group,
        "update teacher": admin_group,
        "update student": admin_group,
        "update class": admin_group,
        "delete": admin_group,
        "delete teacher": admin_group,
        "delete student": admin_group,
        "delete class": admin_group,
        "go back": "go_back",
        "exit": "exit_program"
    }
    choice = click.prompt("", type=str).lower()
    if choice in choices:
        admin_group(args = choices[choice])
    else:
        print("Invalid choice. Please try again.")


@click.group()
def admin_group():
    pass

admin_group.add_command(go_back)
admin_group.add_command(exit_program)

@admin_group.command()
def admin_add():
    pass



@click.command()
def teacher_menu():
    click.echo("Teacher menu:")

@click.command()
def student_menu():
    click.echo("Student menu:")

