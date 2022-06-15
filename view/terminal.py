import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu(title, list_options):
    title = title.upper()
    print("\n\n")
    print(title.center(95))
    print()
    counter = 0
    for option in list_options:
        print(str(counter).rjust(50), option)
        counter += 1


def print_message(message):
    print(message)


def print_general_results(result, label):
    if isinstance(result, (int) ):
        print(f'{label}: {result}')
    elif isinstance(result, (float)):
        two_decimal_float = round(result, 2)
        print(f'{label}: {two_decimal_float}')
    elif isinstance(result, (list, tuple)):
        print(f'{label}')
        for item in result:
            print(item, end='; ')
    elif isinstance(result, (dict)):
        print(f'{label}')
        for key, value in result.items():
            print(f'{key}; {value}', end='; ')


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    length_list = [len(element) for row in table for element in row]
    column_width = max(length_list)
    separator_between_rows = (len(table[0])*(column_width + 5)) * '-'
    for row in table:
        print(separator_between_rows.rjust(100))
        row = " | ".join(element.center(column_width + 2) for element in row)
        print(row.rjust(98))
    print(separator_between_rows.rjust(100))


"""Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """

    inp = input(f"{label}: ")
    return inp


def get_inputs(labels):
    new_data = []
    for label in labels:
        get_lable = input(label + ': ')
        new_data.append(get_lable)
    return new_data



def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"Error:{ message}")
