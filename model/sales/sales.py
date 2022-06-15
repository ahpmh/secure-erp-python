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
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def get_data_from_file():
    data = data_manager.read_table_from_file(DATAFILE)
    data.insert(0, HEADERS)
    return data

def write_to_file(plus_data):
    plus_data.pop(0)
    data_manager.write_table_to_file(DATAFILE, plus_data)

def get_id():
    id = util.generate_id()
    return id

def add_transaction():
    data = get_data_from_file()
    new_transaction = []
    id = get_id()
    custumer_id = get_id()
    product = input("Please type the product name: ")
    date_time = input('Please type the transaction date (YYYY-MM-DD): ' )
    price = float(input('Please type the price: '))

    

