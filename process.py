import json
import tui

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


class Record:

    parent_country = None

    def __init__(self, parent_country, name, cases, deaths, recovered):
        self.parent_country = Record.parent_country
        self.name = name
        self.cases = cases
        self.deaths = deaths
        self.recovered = recovered

    def __str__(self):
        return f"{self.name} has a total of {self.cases} cases, {self.deaths} deaths and {self.recovered} recovered."

    def __repr__(self):
        return f"Country = {self.name}, cases = {self.cases}, deaths = {self.deaths}, recovered = {self.recovered}"


def summary(records):

    country_records = []
    region_records = []
    names = []

    for i in range(1, len(records)):
        if records[i][3] not in names:
            country_records.append(Record(None, records[i][3], int(records[i][5]), int(records[i][6]), int(records[i][7])))
            names.append(records[i][3])

        else:
            for r in country_records:
                if r.name == records[i][3]:
                    r.cases += int(records[i][5])
                    r.deaths += int(records[i][6])
                    r.recovered += int(records[i][7])
                    break

        if records[i][2] not in names:
            region_records.append(Record(records[i][3], records[i][2], int(records[i][5]), int(records[i][6]), int(records[i][7])))
            names.append(records[i][2])

        else:
            for r in region_records:
                if r.name == records[i][2]:
                    r.cases += int(records[i][5])
                    r.deaths += int(records[i][6])
                    r.recovered += int(records[i][7])
                    break

    return country_records, region_records


def export_data(records, export_option):

    if export_option == 1:
        tui.progress("Exporting all data", 0)
        del records[0]
        with open("All_Data.json", "w") as dump:
            json.dump(records, dump, indent = 1)
        tui.progress("Exporting all data", 100)

    elif export_option == 2:
        record_choice = tui.observation_country(records)
        dump_records = []
        if record_choice[0] == "c":
            del records[0]
            tui.progress("Exporting country data", 0)
            for i in range(len(records)):
                if records[i][3] in record_choice:
                    dump_records.append(records[i])
            with open("Country_Data.json", "w") as dump:
                json.dump(dump_records, dump, indent = 1)
            tui.progress("Exporting country data", 100)

        elif record_choice[0] == "r":
            del records[0]
            tui.progress("Exporting region data", 0)
            for i in range(len(records)):
                if records[i][2] in record_choice:
                    dump_records.append(records[i])
            with open("Region_Data.json", "w") as dump:
                json.dump(dump_records, dump, indent = 1)
            tui.progress("Exporting region data", 100)


def unique_places(place, records):

    if place == "c":
        countries_in_records = []
        for i in range(1, len(records)):
            if records[i][3] not in countries_in_records:
                countries_in_records.append(records[i][3])
        print(countries_in_records)
        return countries_in_records

    elif place == "r":
        regions_in_records = []
        for i in range(1, len(records)):
            if records[i][2] not in regions_in_records:
                regions_in_records.append(records[i][2])

        print(regions_in_records)
        return regions_in_records

    else:
        tui.error("Huh?")
