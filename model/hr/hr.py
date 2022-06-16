""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
# unuse codpart,if runs without it, will be deleted:  from datetime import date
from datetime import datetime
from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["ID", "NAME", "DATE OF BIRTH", "DEPARTMENT", "CLEARANCE"]


list_of_employee = data_manager.read_table_from_file(DATAFILE)


def add_employee(new_employee):
    data = data_manager.read_table_from_file(DATAFILE)
    new_id = util.generate_id()
    new_employee.insert(0, new_id)
    new_data = data + [new_employee]
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


def delete_employee(id_input):
    datas = data_manager.read_table_from_file(DATAFILE)
    counter = 0
    for data in datas:
        if data[0] == id_input:
            datas.pop(counter)
        counter += 1
    data_manager.write_table_to_file(DATAFILE, datas)


def oldest_youngest_employee():
    date_of_birth = {}
    list_of_employees = data_manager.read_table_from_file(
        DATAFILE, separator=';')

    for employee in list_of_employees:
        date_of_birth[employee[1]] = datetime.strptime(employee[2], '%Y-%m-%d')

    today = datetime.today()
    youngest_employee = max(date_of_birth, key=lambda k: date_of_birth[k])
    oldest_employee = min(date_of_birth, key=lambda k: date_of_birth[k])
    youngest_emplyee_age = f'{(today.year - date_of_birth[youngest_employee].year)} years old'
    oldest_emplyee_age = f'{(today.year - date_of_birth[oldest_employee].year)} years old'

    return f'The oldest employee is {oldest_employee} ({oldest_emplyee_age}) and \
the youngest is {youngest_employee} ({youngest_emplyee_age}).'


def list_of_employees():
    data = data_manager.read_table_from_file(DATAFILE)
    data.insert(0, HEADERS)
    return data


def average_age(birth_date):
    pass


def birthdays_next():
    pass


def count_employees_clearance_from_input(data_from_cust):
    data = data_manager.read_table_from_file(DATAFILE)
    counter = 0
    for element in data:
        if data_from_cust <= element[4]:
            counter += 1
    return counter


def get_number_of_employees_per_department():
    pass
