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


def add_customer(new_info):
    data = data_manager.read_table_from_file(DATAFILE)
    new_id = util.generate_id()
    new_info.insert(0, new_id)
    new_data = data + [new_info]
    data_manager.write_table_to_file(DATAFILE, new_data)
    return new_data

    '''new_cust = data.append
    new_ID = util.generate_id()
    data.insert(0, new_ID)
    return new_cust'''


def update_customer(id_input, new_infos):
    datas = data_manager.read_table_from_file(DATAFILE)
    nemtom = [data[0] for data in datas]
    updated_data = []
    if id_input in nemtom:
        for data in datas:
            if data[0] == id_input:
                new_infos.insert(0, data[0])
                data = new_infos
            updated_data.append(data)
    else:
        print('There are no customer with that ID.')
    data_manager.write_table_to_file(DATAFILE, updated_data)
    return updated_data


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
