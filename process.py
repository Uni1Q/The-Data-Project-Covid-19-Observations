import json
from tui import *
"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""

# TODO: Your code here

def summary(records):
    countries_in_records = []
    regions_in_records = []
    for i in range(1 ,len(records)):
        if records[i][3] not in countries_in_records:
            countries_in_records.append(records[i][3])
        elif records[i][2] not in regions_in_records:
            regions_in_records.append(records[i][2])



def export_data(records, export_option):

    if export_option == 1:
        progress("Exporting all data", " 0%\n")
        del records[0]
        with open("All_Data.json", "w") as dump:
            json.dump(records, dump, indent = 2)
        progress("Exporting all data", " 100%\n")

    elif export_option == 2:
        record_choice = observation_country()
        dump_records = []
        if record_choice[0] == "c":
            progress("Exporting country data", " 0%\n")
            for i in range(len(records)):
                if records[i][3] in record_choice:
                    dump_records.append(records[i])
            print(dump_records)
            with open("Country_Data.json", "w") as dump:
                json.dump(dump_records, dump, indent = 2)
            progress("Exporting country data", " 100%\n")

        elif record_choice[0] == "r":
            progress("Exporting region data", " 0%\n")
            for i in range(len(records)):
                if records[i][3] in record_choice:
                    dump_records.append(records[i])
            with open("Region_Data.json", "w") as dump:
                json.dump(dump_records, dump, indent = 2)
            progress("Exporting region data", " 100%\n")
