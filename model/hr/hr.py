""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
from datetime import date
from datetime import datetime
from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

list_of_employee = data_manager.read_table_from_file(DATAFILE)

def add_employee(new_employee):
    newID = util.generate_id() 
    new_employee.insert(0,newID) 
    list_of_employee.append(new_employee)
    data_manager.write_table_to_file(DATAFILE,list_of_employee)


def update_employee(employee_nr, updated_employee):
    newID = util.generate_id() 
    updated_employee.insert(0,newID) 
    list_of_employee[int(employee_nr)] = updated_employee
    data_manager.write_table_to_file(DATAFILE,list_of_employee)


def delete_employee(employee_to_delete):
    del list_of_employee[int(employee_to_delete)]
    data_manager.write_table_to_file(DATAFILE,list_of_employee)


def oldest_youngest_employee():
    date_of_birth = {}
    list_of_employees = data_manager.read_table_from_file(DATAFILE, separator=';')

    for employee in list_of_employees:
        date_of_birth[employee[1]] = datetime.strptime(employee[2], '%Y-%m-%d')

    today = datetime.today()
    youngest_employee = max(date_of_birth, key = lambda k: date_of_birth[k])
    oldest_employee = min(date_of_birth, key = lambda k: date_of_birth[k])
    youngest_emplyee_age = f'{(today.year - date_of_birth[youngest_employee].year)} years old'
    oldest_emplyee_age = f'{(today.year - date_of_birth[oldest_employee].year)} years old'

    return f'The oldest employee is {oldest_employee} ({oldest_emplyee_age}) and \
the youngest is {youngest_employee} ({youngest_emplyee_age}).'