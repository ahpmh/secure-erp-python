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
    '''Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)'''


def print_message(message):
    '''Args:
        message: str - the message'''
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


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
    final_printTable = (len(table[0])*(column_width + 5)) * '-'
    for row in table:
        print(final_printTable.rjust(100))
        row = " | ".join(element.center(column_width + 2) for element in row)
        print(row.rjust(100))
    print(final_printTable.rjust(100))


"""Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    nl = '\n\n'
    inp = int(input(f"{nl}Please {label} : "))
    return inp


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    inps = input(f"Please {labels} :\n")
    return inps


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"Error:{ message}")
