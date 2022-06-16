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


def add_tranzaction(new_info):
    data = data_manager.read_table_from_file(DATAFILE)
    new_id = util.generate_id()
    new_info.insert(0, new_id)
    new_data = data + [new_info]
    data_manager.write_table_to_file(DATAFILE, new_data)


def updating_employee(id_input, new_infos):
    datas = data_manager.read_table_from_file(DATAFILE)
    updated_data = []
    for data in datas:
        if data[0] == id_input:
            new_infos.insert(0, data[0])
            data = new_infos
        updated_data.append(data)
    print(updated_data)
    data_manager.write_table_to_file(DATAFILE, updated_data)
    return updated_data


def delete_transaction(id_input):
    datas = data_manager.read_table_from_file(DATAFILE)
    counter = 0
    for data in datas:
        if data[0] == id_input:
            datas.pop(counter)
        counter += 1
    data_manager.write_table_to_file(DATAFILE, datas)


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


def sum_transactions_between(from_date, to_date):
    data = get_data_from_file()
    data.pop(0)
    sum_price_between_two_dates = 0
    for element in data:
        transaction_date = datetime.date.fromisoformat(element[4])
        if from_date < transaction_date < to_date:
            sum_price_between_two_dates += float(element[3])
    return sum_price_between_two_dates
