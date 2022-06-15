#    adatmanipuláció csak a modelben!!!
# a view-t csak a controller hívja meg

""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util
from view import terminal as view


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


# data_manager.read_table_from_file(DATAFILE)


def list_customers():
    data = data_manager.read_table_from_file(DATAFILE)
    return data


def add_customer():
    data = data_manager.read_table_from_file(DATAFILE)
    data.append(view.get_input(label))
    data_manager.write_table_to_file(DATAFILE, data)


def update_customer():
    data = data_manager.read_table_from_file(DATAFILE)
    # if in database update, else ez a felhasználó nincs az adatbázisban kívanod hozzáadni? add_customer
    view.get_inputs(labels)
    data_manager.write_table_to_file(DATAFILE, data)


def delete_customer():
    data = data_manager.read_table_from_file(DATAFILE)
    # del data(ahol találta sor)
    data_manager.write_table_to_file(DATAFILE, data)


def get_subscribed_emails():
    data = data_manager.read_table_from_file(DATAFILE)
    #  if 1, else
    view.print_general_results(result, label)
