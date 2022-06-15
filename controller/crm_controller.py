from model.crm import crm
from view import terminal as view

# a view-t csak a controller hívja meg, azzal amit a model return-öl
#pl view.print_table(amit a modell returnol és a controller hívja meg)

''' itt lent run operation-ben és a feladatleírásban az 1 és 2 menüpont fel van cserélve.
Melyik szerint csináljuk? -> a fileban lévőt használjuk. '''


def list_customers(data):
    crm.list_customers()
    view.print_table(data)


def add_customer():
    pass
#  option 1 asks the user to type the name, email, and subscription status for a new customer.
# When the last field is filled in, a new customer is introduced with an random ID.


def update_customer():
    view.print_error_message("Not implemented yet.")
#  option 3 asks the user for the ID of a customer. If the ID belongs to an existing customer, the user enters new values for the name, email, and subscription status.
# When the last field is filled in, the customer fields are updated with the given values.


def delete_customer():
    view.print_error_message("Not implemented yet.")
#  option 4 asks the user for the ID of a customer.
# If the ID belongs to an existing customer, the customer is deleted from the database.


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")
#  Get the emails of subscribed customers.


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
            operation = view.get_input("select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)


if __name__ == '__main__':
    main()
