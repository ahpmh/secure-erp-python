from model.crm import crm
from view import terminal as view
import os

'''  a view-t csak a controller hívja meg, azzal amit a model return-öl
 pl view.print_table(amit a modell returnol és a controller hívja meg)'''

# itt lent run operation-ben és a feladatleírásban az 1 és 2 menüpont fel van cserélve.
# Melyik szerint csináljuk? -> a fileban lévőt használjuk.


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def list_customers():
    data = crm.list_customers()
    view.print_table(data)


def add_customer():
    headers = crm.HEADERS[1:]
    new_infos = view.get_inputs(headers)
    crm.add_customer(new_infos)
    view.print_table(crm.data_manager.read_table_from_file(crm.DATAFILE))


def update_customer():
    datas = crm.data_manager.read_table_from_file(crm.DATAFILE)
    header_for_id = crm.HEADERS[:1]
    headers_without_id = crm.HEADERS[1:]
    id_form_user = view.get_input(''.join(header_for_id))
    ids = [data[0] for data in datas]
    if id_form_user in ids:
        for data in datas:
            if data[0] == id_form_user:
                new_infos = view.get_inputs(headers_without_id)
                crm.update_customer(id_form_user, new_infos)
                view.print_table(
                    crm.data_manager.read_table_from_file(crm.DATAFILE))
    else:
        view.print_message(
            'There is no customer for this ID. If you want to add a new customer please select add customer option.')


def delete_customer():
    header = crm.HEADERS[:1]
    user_id = view. get_input(''.join(header))
    crm.delete_customer(user_id)
    view.print_table(crm.data_manager.read_table_from_file(crm.DATAFILE))


def get_subscribed_emails():  # Get the emails of subscribed customers.
    empty_row = "\n"
    subscribedMail = crm.get_subscribed_emails()
    view.print_general_results(
        subscribedMail, f"{empty_row}Email address of subscribed customer(s):{empty_row}")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


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
