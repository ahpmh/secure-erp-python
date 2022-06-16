from model.sales import sales
from view import terminal as view
import datetime
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def list_transactions():
    view.print_table(sales.get_data_from_file())


def add_transaction():
    headers = sales.HEADERS[1:]
    new_infos = view.get_inputs(headers)
    sales.add_tranzaction(new_infos)
    view.print_table(sales.data_manager.read_table_from_file(sales.DATAFILE))


def update_transaction():
    datas = sales.data_manager.read_table_from_file(sales.DATAFILE)
    header_for_id = sales.HEADERS[:1]
    headers_without_id = sales.HEADERS[1:]
    id_form_user = view.get_input(''.join(header_for_id))
    IDs = [data[0] for data in datas]
    if id_form_user in IDs:
        for data in datas:
            if data[0] == id_form_user:
                new_infos = view.get_inputs(headers_without_id)
                sales.updating_employee(id_form_user, new_infos)
                view.print_table(
                    sales.data_manager.read_table_from_file(sales.DATAFILE))
    else:
        view.print_message(
            'There are no customer with this ID. If you want to add a new customer please select add customer option.')


def delete_transaction():
    header = sales.HEADERS[:1]
    user_id = view. get_input(''.join(header))
    sales.delete_customer(user_id)
    view.print_table(sales.data_manager.read_table_from_file(sales.DATAFILE))


def get_biggest_revenue_transaction():
    view.print_general_results(sales.get_biggest_revenue_transaction(
    ), 'This is the biggest revenue transaction.')


def get_biggest_revenue_product():
    view.print_general_results(
        sales.get_biggest_revenue_product(), 'This is the biggest revenue product.')


def count_transactions_between():
    dates = view.get_inputs(['Type the start date', 'Type the end date'])
    start_date = datetime.date.fromisoformat(dates[0])
    end_date = datetime.date.fromisoformat(dates[1])
    view.print_general_results(sales.count_transactions_between(
        start_date, end_date), 'The number of transactions')


def sum_transactions_between():
    dates = view.get_inputs(['Type the start date', 'Type the end date'])
    start_date = datetime.date.fromisoformat(dates[0])
    end_date = datetime.date.fromisoformat(dates[1])
    view.print_general_results(sales.sum_transactions_between(
        start_date, end_date), 'The sum of transactions')


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Please select an operation:\n")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
    clear()
