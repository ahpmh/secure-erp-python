#    adatmanipuláció csak a modelben!!!
# a view-t csak a controller hívja meg
# Only model files import data_manager. Model files do not import the view at all.
""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["ID", "NAME", "EMAIL", "SUBSCRIBED"]


def list_customers():
    data = data_manager.read_table_from_file(DATAFILE)
    data.insert(0, HEADERS)
    return data


def add_customer():
    data = data_manager.read_table_from_file(DATAFILE)
    new_cust = data.append
    new_ID = util.generate_id()
    data.insert(0, new_ID)
    return new_cust

def update_customer():
    # data = data_manager.read_table_from_file(DATAFILE)
    # cust = input("Please type the email of the customer you would like to update: ")
    # if cust not in data:

    #     data_manager.write_table_to_file(data, cust)
    # else:
    #     print("This email cannot be found in our database, please use Add customer!")
    # return 
    # if in database update, else ez a felhasználó nincs az adatbázisban kívanod hozzáadni? add_customer
    pass

def delete_customer():
    # data = data_manager.read_table_from_file(DATAFILE)
    # # del data(ahol találta sor)
    # data_manager.write_table_to_file(DATAFILE, data)
    pass


def get_subscribed_emails():
    # data = data_manager.read_table_from_file(DATAFILE)
    # #  if 1, else
    # view.print_general_results(result, label)
    pass
