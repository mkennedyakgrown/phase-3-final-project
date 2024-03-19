#!/usr/bin/env python3


from types import FunctionType as function

from helpers import (
    main_menu
)

menu_stack = []

def show_menu(menu_items):
    while True:
        ### Display menu ###
        print(menu_items["menu_text"])
        if len(menu_stack) > 0:
            print("    • Go Back")
        print("    • Exit Program")

        ### Get user choice ###
        choice = input("").lower()

        ### Process user choice ###
        if choice in menu_items and choice != "menu_text":
            menu_stack.append(menu_items)

            ### If the menu item is a dictionary, display the sub-menu ###
            if type(menu_items[choice]) == dict:
                show_menu(menu_items[choice])

            ### If the menu item is a function, call it ###
            elif type(menu_items[choice]) == function:
                menu_items[choice]()
                prev_menu = menu_stack.pop()
                show_menu(prev_menu)

            ### If the menu item is a list, call the function using parameters ###
            elif type(menu_items[choice]) == list and len(menu_items[choice]) == 2:
                menu_items[choice][0](menu_items[choice][1])
                prev_menu = menu_stack.pop()
                show_menu(prev_menu)

            ### If the menu item is a list, call the function using parameters ###
            elif type(menu_items[choice]) == list and len(menu_items[choice]) == 3:
                menu_items[choice][0](menu_items[choice][1], menu_items[choice][2])
                prev_menu = menu_stack.pop()
                show_menu(prev_menu)

        elif choice == "go back":
            if len(menu_stack) > 0:
                prev_menu = menu_stack.pop()
                show_menu(prev_menu)
            else:
                print("Cannot go back further.")
        elif choice == "exit" or choice == "quit" or choice == "exit program":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    show_menu(main_menu)

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
    #     * View Information
    #         * View Classes
    #         * View Students
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
    