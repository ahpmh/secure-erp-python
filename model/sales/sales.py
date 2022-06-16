""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["ID", "CUSTOMER", "PRODUCT", "PRICE", "DATE"]


def get_data_from_file():
    data = data_manager.read_table_from_file(DATAFILE)
    data.insert(0, HEADERS)
    return data


def add_tranzaction(new_info):
    data = data_manager.read_table_from_file(DATAFILE)
    new_id = util.generate_id()
    new_info.insert(0, new_id)
    new_data = data + [new_info]
    data_manager.write_table_to_file(DATAFILE, new_data)


def get_biggest_revenue_transaction():
    data = get_data_from_file()
    data.pop(0)
    biggest_transaction = data[0]
    for transaction in data:
        if float(transaction[3]) > float(biggest_transaction[3]):
            biggest_transaction = transaction
    return biggest_transaction

def get_biggest_revenue_product():
    data = get_data_from_file()
    data.pop(0)
    items = {}
    biggest_revenue = ("empty", 0)
    for element in data:
        if element[2] in items.keys():
            items[element[2]] += float(element[3])
        else:
            items.update({element[2]: float(element[3])})
    for produce_name, produce_price in items.items():
        if produce_price > biggest_revenue[1]:
            biggest_revenue = (produce_name, produce_price)
    return biggest_revenue
