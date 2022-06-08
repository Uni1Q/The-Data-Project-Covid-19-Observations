import matplotlib.pyplot as plt
import tui
import process as prc

"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here


def pie_chart(records):

    visual_choice = tui.visual_country()

    country_records, region_records = prc.summary(records)

    if visual_choice == "c":
        fig, axs = plt.subplots()
        country_values = []
        country_labels = []
        total = 0

        for country in country_records:
            country_values.append(country.cases)
            country_labels.append(country.name)
            total += country.cases

        plt.title("Country cases")
        plt.pie(country_values, autopct='%.1f%%')
        plt.legend(labels = country_labels, loc = "upper right", bbox_to_anchor=(1.5, 1.15))

    elif visual_choice == "r":

        fig, (ax1, ax2) = plt.subplots(2)

        region_values = []
        region_labels = []
        china_values = []
        china_labels = []
        total_china = 0
        total_else = 0


        for region in region_records:
            if region.name == "":
                continue
            elif region.name == "Unknown":
                continue
            if region.parent != "Mainland China":
                region_values.append(region.cases)
                region_labels.append(region.name)
                total_else += region.cases
            else:
                china_values.append(region.cases)
                china_labels.append(region.name)
                total_china += region.cases

        plt.title("Region cases")
        ax1.pie(china_values, labels = china_labels, autopct='%.1f%%')
        ax1.set_xlabel(f"Total cases for Mainland China - {total_china}")
        ax2.pie(region_values, labels = region_labels, autopct='%.1f%%')
        ax2.set_xlabel(f"Total cases for all the countries - {total_else}")
        plt.tight_layout()

    plt.show()


def bar_chart(records):
    pass


def animate(records):
    pass
