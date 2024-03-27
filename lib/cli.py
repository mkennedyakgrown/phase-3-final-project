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