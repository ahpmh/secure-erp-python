# test

from model import data_manager

DATAFILE = "model/sales/sales.csv"
HEADERS = ["ID", "CUSTOMER", "PRODUCT", "PRICE", "DATE"]

def get_data_from_file():
    data = data_manager.read_table_from_file(DATAFILE)
    data.insert(0, HEADERS)
    return data

def get_dict():
    data = get_data_from_file()
    data.pop(0)
    empty_folder = ("valami", 0)
    csv_items = {}
    for i in data:
        if i[2] in csv_items.keys():
            csv_items[i[2]] += float(data[3])
        else:
            csv_items.update({i[2]: float(data[3])})
    for k, v in csv_items.items():
        if v > empty_folder[1]:
            empty_folder = (k, v)
    return empty_folder

def main():
    get_dict()

if __name__ == '__main__':
    main()