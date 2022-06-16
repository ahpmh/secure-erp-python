""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util
import datetime

DATAFILE = "model/sales/sales.csv"
HEADERS = ["ID", "CUSTOMER", "PRODUCT", "PRICE", "DATE"]


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
    date_time = input('Please type the transaction date (YYYY-MM-DD): ')
    price = input('Please type the price: ')

    new_transaction.append(id)
    new_transaction.append(custumer_id)
    new_transaction.append(product)
    new_transaction.append(price)
    new_transaction.append(date_time)

    data.append(new_transaction)

    write_to_file(data)

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

def count_transactions_between(from_date, to_date):
    data = get_data_from_file()
    data.pop(0)
    counter = 0
    for element in data:
        transaction_date = datetime.date.fromisoformat(element[4])
        if from_date < transaction_date < to_date:
            counter += 1
    return counter



        

