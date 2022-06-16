from model.hr import hr
from view import terminal as view


def list_employees():
    data = hr.list_of_employees()
    view.print_table(data)


def add_employee():
    headers = hr.HEADERS[1:]
    new_info = view.get_inputs(headers)
    hr.add_employee(new_info)
    view.print_table(hr.data_manager.read_table_from_file(hr.DATAFILE))


def update_employee():
    datas = hr.data_manager.read_table_from_file(hr.DATAFILE)
    header_for_id = hr.HEADERS[:1]
    headers_without_id = hr.HEADERS[1:]
    id_form_user = view.get_input(''.join(header_for_id))
    IDs = [data[0] for data in datas]
    if id_form_user in IDs:
        for data in datas:
            if data[0] == id_form_user:
                new_infos = view.get_inputs(headers_without_id)
                hr.updating_employee(id_form_user, new_infos)
                view.print_table(
                    hr.data_manager.read_table_from_file(hr.DATAFILE))
    else:
        view.print_message(
            'There is no customer with this ID. If you want to add a new customer please select add customer option.')


def delete_employee():
    header = hr.HEADERS[:1]
    user_id = view.get_input(''.join(header))
    hr.delete_employee(user_id)
    view.print_table(hr.data_manager.read_table_from_file(hr.DATAFILE))


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Please select an operation:\n")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
