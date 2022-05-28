"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should display the title 'COVID-19 (January) Data'.
    The welcome message should contain dashes above and below the title.
    The number of dashes should be equivalent to the number of characters in the title.

    :return: Does not return anything.
    """

    # TODO: Your code here

    print("-----------------------------------")
    print("Welcome to covid data visualization")
    print("-----------------------------------")

def error(msg):
    """
    Task 2: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter 'msg' passed to this function

    :param msg: a string containing an error message
    :return: does not return anything
    """
    # TODO: Your code here

    print(msg)


def progress(operation, value):
    """
    Task 3: Display a message to indicate the progress of an operation.

    The function should display a message in the following format:
    '{operation} {status}.'

    Where {operation} is the value of the parameter passed to this function
    and
    {status} is 'has started' if the value of the parameter 'value' is 0
    {status} is 'is in progress ({value}% completed)' if the value of the parameter 'value' is between,
    but not including, 0 and 100
    {status} is 'has completed' if the value of the parameter 'value' is 100

    :param operation: a string indicating the operation being started
    :param value: an integer indicating the amount of progress made
    :return: does not return anything
    """
    # TODO: Your code here

    print(operation, value)


def menu(variant):
    """
    Task 4: Display a menu of options and read the user's response.

    If no value or a zero is supplied for the parameter 'variant' then a menu with the following options
    should be displayed:

    '[1] Process Data', '[2] Visualise Data', '[3] Export Data' and '[4] Exit'

    If the value of the parameter 'variant' is 1 then a menu with the following options should be displayed:

    '[1] Record by Serial Number', '[2] Records by Observation Date', '[3] Group Records by Country/Region,
    '[4] Summarise Records'

    If the value of the parameter 'variant' is 2 then a menu with the following options should be displayed:

    '[1] Country/Region Pie Chart', '[2] Observations Chart', '[3] Animated Summary'

    If the value of the parameter 'variant' is 3 then a menu with the following options should be displayed:

    '[1] All Data', '[2] Data for Specific Country/Region'

    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Process Data', 2 for 'Visualise Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed

    :return: nothing if invalid selection otherwise an integer for a valid selection
    """
    # TODO: Your code here

    userSelection = 0
    print("Please input what you'd like to do")
    print("[1] Process Data")
    print("[2] Visualize Data ")
    print("[3] Export Data")
    print("[4] Exit\n")

    selection = int((input("User Input: ")))
    if selection not in {1, 2, 3, 4}:
        error("Wrong input")

    if selection == 1:
        print("\n[1] Record by Serial Number")
        print("[2] Records by Observation Date")
        print("[3] Group Records by Country/Region")
        print("[4] Summarise Records")

        userSelection = int(input("\nUser Input: "))
        if userSelection not in {1, 2, 3, 4}:
            error("Wrong input")

    elif selection == 2:
        print("\n[1] Country/Region Pie Chart")
        print("[2] Observations Chart")
        print("[3] Animated Summary")

        userSelection = int(input("\nUser Input: "))
        if userSelection in {1, 2, 3}:
            pass
        else:
            error("Wrong input")

    elif selection == 3:
        print("\n[1] All Data")
        print("[2] Data for Specific Country/Region")

        userSelection = int(input("\nUser Input: "))
        if userSelection in {1, 2}:
            pass
        else:
            error("Wrong input")

    elif selection == 4:
        variant = selection
        return variant
    else:
        print("An unexpected error occurred in the file TUI.py")

    variant = selection * 10 + userSelection

    return variant


def total_records(num_records):
    f"""
    Task 5: Display the total number of records in the data set.
    
    The function should display a message in the following format:

    "There are {num_records} records in the data set."

    Where {num_records} is the value of the parameter passed to this function
    
    :param num_records: the total number of records in the data set
    :return: Does not return anything
    """
    # TODO: Your code here

    print(f"There are {num_records} records in the data set.")


def serial_number():
    """
    Task 6: Read in the serial number of a record and return the serial number.

    The function should ask the user to enter a serial number for a record e.g. 189
    The function should then read in and return the user's response as an integer.

    :return: the serial number for a record
    """
    # TODO: Your code here
    record_serial = int(input("Please enter the serial number for a record: "))
    return record_serial


def observation_dates(selected_date):
    """
    Task 7: Read in and return a list of observation dates.

    The function should ask the user to enter some observation dates
    This should be entered in the format dd/mm/yyyy where dd is two-digit day, mm is two digit month and yyyy is
    a four digit year e.g. 01/22/2020
    The function should return a list containing the specified observation dates.

    :return: a list of observation dates
    """
    # TODO: Your code here

    print("Please enter an observation day (please write single digit days and months with a zero e.g. 02):")

    day = input("Enter day")
    month = input("Enter month")
    year = input("Enter year")

    selected_date = day + "/" + month + "/" + year
    return selected_date


def display_record(record, cols = None):
    """
    Task 8: Display a record. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the record will be displayed.

    The parameter record is a list of values e.g. [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    The parameter cols is a list of column indexes e.g. [0,3,5]
    The function should display a list of values.
    The displayed list should only consist of those values whose column index is in cols.

    E.g. if cols is [1,3] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    ['01/22/2020','Mainland China']

    E.g. if cols is [0,1,4] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    [1,'01/22/2020','1/22/2020 17:00']

    E.g. if cols is an empty list or None then all the values will be displayed
    [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]

    :param record: A list of data values for a record
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here

    record_serial = serial_number()

    multiple_cols = input("Would you like to print all the columns? (y, n) ")

    if multiple_cols.lower() == "n":
        col_length = int(input("How many columns would you like to print? \nUser input: "))
        cols = []
        print("Which of those columns would you like to print? \nUser input: ")
        tempVal = 0
        while col_length != tempVal:
            tempInput = int(input())
            if tempInput in range(8):
                cols.append(tempInput)
                tempVal += 1
            else:
                print("Wrong input")
    elif multiple_cols.lower() == "y":
        pass
    else:
        error("Wrong Input!")

    lst = list()

    if cols:
        for i in cols:
            lst.append(record[i])
        return lst
    else:
        return lst



def display_records(record_by_date = None, record_by_serial = None, record_by_country = None):
    """
    Task 9: Display each record in the specified list of records.
    Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for a record will be displayed.

    The function should have two parameters as follows:

    records     which is a list of records where each record itself is a list of data values.
    cols        this is a list of integer values that represent column indexes.
                the default value for this is None.

    You will need to add these parameters to the function definition.

    The function should iterate through each record in records and display the record.

    Each record should be displayed as a list of values e.g. [1,01/22/2020,Anhui,Mainland China,1/22/2020 17:00,1,0,0]
    Only the columns whose indexes are included in cols should be displayed for each record.

    If cols is an empty list or None then all values for the record should be displayed.

    :param records: A list of records
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here

    if record_by_serial == True:
        record_choice = serial_number()
        display_record(record, cols = None)
    elif record_by_date == True:
        pass
    elif record_by_country == True:
        pass
    else:
        error("Unexpected error occurred, cannot record by given selection")
        exit()


    recordAmount = int(input("How many records to display by given index? Type 0 if you wish to display all records "))
    if recordAmount == 0:
        displayAllRecords = True

    num_cols = int(input("How many columns should be displayed for given index (0 if you want to display all the information for given record): "))
    displayAllInfo = False
    loops = 0

    if num_cols == 0:
        displayAllInfo = True

    if not displayAllInfo:
        while loops != num_cols:
            selection = int(input("Please enter selected column: "))
            if selection in {0, 1, 2, 3, 4, 5, 6, 7}:
                cols.append(selection)
                loops += 1
            else:
                print("Selection outside of given range")

    for i in range(recordAmount):
        display_record(displayAllInfo)
