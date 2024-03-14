#!/usr/bin/env python3

from helpers import (
    exit_program,
    admin_menu,
    teacher_menu,
    student_menu
)


def admin():
    admin_menu()
    main()

def teacher():
    print("Teacher menu:")
    main()

def student():
    print("Student menu:")
    main()

def exit():
    exit_program()
    
def main():
    menu = {
        "admin": admin,
        "teacher": teacher,
        "student": student,
        "exit": exit
    }
    while True:
        print("Choose role:")
        for key in menu:
            print(f"    • {key.capitalize()}")
        choice = input("").lower()
        if choice in menu:
            menu[choice]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# Program flow:
    # 
    # Ask for role options:
    #     * Admin (Add/Delete/Update Teachers, Students, Classes)
    #     * Teacher (Write/Update/View Reports)
    #     * Student (View Reports)?
    #     * Exit
    #
    ########################### 
    #
    # If Admin:
    #     * Teachers Information
    #         * List Teachers
    #             * Print list of teachers
    #                 * Return to Teachers Information
    #         * Search Teachers
    #             * Get input for name
    #                 * Query database for teacher(s)
    #                 * Select a Teacher to view
    #                     * Print Teacher Information (Name, Classes, Students)
    #                         * Update Teacher
    #                         * Delete Teacher
    #     * Students Information
    #         * List Students
    #             * Print list of students
    #                 * Return to Students Information
    #         * Search Students
    #             * Get input for name
    #                 * Query database for student(s)
    #                 * Select a Student to view
    #                     * Print Student Information (Name, Classes, Teachers)
    #                         * Update Student
    #                         * Delete Student
    #     * Classes Information
    #         * List Classes
    #             * Print list of classes
    #                 * Return to Classes Information
    #         * Search Classes
    #             * Get input for name
    #                 * Query database for class(s)
    #                 * Select a Class to view
    #                     * Print Class Information (Name, Teachers, Students)
    #                         * Update Class
    #                         * Delete Class
    #     * Add Teacher
    #         * Get input for name
    #             * Start loop for adding classes
    #                 (Print list of available classes)
    #                 * Get input for classes
    #                     * Loop
    #     * Add Student
    #         * Get input for name
    #             * Start loop for adding classes
    #                 (Print list of available classes)
    #                 * Get input for classes
    #                     * Loop
    #     * Add Class
    #         * Get input for name
    #             * Start loop for adding teachers
    #                 (Print list of available teachers)
    #                 * Get input for teacher(s)
    #                     * Start loop for adding students
    #                         (Print list of available students)
    #                         * Get input for one student
    #                             * Loop
    #     * Delete Teacher
    #         (Print list of teachers)
    #         * Select Teacher
    #             * Ask for confirmation
    #                 * Delete Teacher
    #     * Delete Student
    #         (Print list of students)
    #         * Select Student
    #             * Ask for confirmation
    #                 * Delete Student
    #     * Delete Class
    #         (Print list of classes)
    #         * Select Class_Name
    #             * Ask for confirmation
    #                 * Delete Class
    #     * Update Teacher
    #         (Print list of teachers)
    #         * Select Teacher
    #             * Get input for name
    #                 * Start loop for adding classes
    #                     (Print list of available classes)
    #                     * Get input for one class
    #                         * Loop
    #     * Update Student
    #         (Print list of students)
    #         * Select Student
    #             * Get input for name
    #                 * Start loop for adding classes
    #                     (Print list of available classes)
    #                     * Get input for one class
    #                         * Loop
    #     * Update Class
    #         (Print list of classes)
    #         * Select Class_Name
    #             * Get input for name
    #                 * Start loop for adding teachers
    #                     (Print list of available teachers)
    #                     * Get input for teacher(s)
    #                         * Start loop for adding students
    #                             (Print list of available students)
    #                             * Get input for one student
    #                                 * Loop
    #     * Go Back
    #     * Exit
    #
    ########################### 
    #
    # If Teacher:
    #     * Write Report
    #         * Select Class_Name
    #             (Print list of students in that class)
    #             * Select Class
    #                 * Get input for report (implement text editor?)
    #             * Select Student
    #                 * Get input for report (implement text editor?)
    #     * Update Report
    #         * Select Class_Name
    #             (Print list of students in that class)
    #             * Select Class
    #                 * Get input for report (implement text editor?)
    #             * Select Student
    #                 (Print report for that class and student)
    #                 * Get input for report (implement text editor?)
    #     * View Reports
    #         * Select Class_Name
    #             (Print Class Report)
    #             (Print list of students in that class)
    #             * Select Student
    #     * Delete Report
    #         * Select Class_Name
    #             (Print list of students in that class)
    #             * Select Student
    #     * Reports Remaining
    #         (Print list of Classes and Students without reports)
    #     * Go Back
    #     * Exit
    #
    ########################### 
    #
    # If Student:
    #     * View Report
    #         (Print list of enrolled classes)
    #         * Select Class_Name
    #             (Print report for that class)
    #             if no report:
    #                 (Print "No report available")
    #     * Go Back
    #     * Exit
    