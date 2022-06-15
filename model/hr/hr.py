""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def list_names():
    hr_info = data_manager.read_table_from_file(DATAFILE)
    hr_infos = []
    for info in hr_info:
        infos = {
            HEADERS[0]: info[0],
            HEADERS[1]: info[1],
            HEADERS[2]: info[2],
            HEADERS[3]: info[3],
            HEADERS[4]: info[4]
        }
        hr_infos.append(infos)
    return hr_infos


def list_employes():
    data = data_manager.read_table_from_file(DATAFILE)
    data.insert(0, HEADERS)
    return data


print(list_employes())
