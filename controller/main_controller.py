from view import terminal as view
from controller import crm_controller, sales_controller, hr_controller
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_module(option):
    clear()
    print("\n\n")
    print("You have chosen the following module from main menu:")
    if option == 1:
        crm_controller.menu()
    elif option == 2:
        sales_controller.menu()
    elif option == 3:
        hr_controller.menu()
    elif option == 0:
        clear()   
        return
    else:
        raise KeyError()


def display_menu():
    options = ["For Exit the program type: 00",
               "Customer Relationship Management (CRM)",
               "Sales",
               "Human Resources"]
    view.print_menu("Main menu", options)


def menu():
    option = None
    while option != '00':
        display_menu()
        try:
            print("\n\n")
            option = view.get_input("\nPlease select module number or 00 for quit:\n")                # label
            load_module(int(option))
        except KeyError:
            view.print_error_message("There is no such option!")    # error msg
        except ValueError:
            view.print_error_message("Please enter a number from the menu points!")      # error msg
    if option == '00':
        view.print_message("You have chosen to QUIT from the program. Good-bye!")
        exit()
