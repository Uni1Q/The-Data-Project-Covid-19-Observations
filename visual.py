import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

    country_records, region_records = prc.summary(records)
    region_records = sorted(region_records)
    country_records = sorted(country_records)

    place_choice, exclude_china = tui.bar_choice()

    fig = plt.figure(figsize=(10, 5))

    top_places = []
    top_place_data = []
    count = 0

    if place_choice == "c":
        if exclude_china == "n":
            for country in country_records:
                if count == 5:
                    break
                top_places.append(country.name)
                top_place_data.append(country.cases)
                count += 1
            plt.title("Top 5 countries by cases")
        elif exclude_china == "y":
            for country in country_records:
                if count == 5:
                    break
                if country.name != "Mainland China":
                    top_places.append(country.name)
                    top_place_data.append(country.cases)
                    count += 1
            plt.title("Top 5 countries by cases (excluding China)")

    elif place_choice == "r":
        if exclude_china == "n":
            for region in region_records:
                if count == 5:
                    break
                if region.name != "":
                    top_places.append(region.name)
                    top_place_data.append(region.cases)
                    count += 1
            plt.title("Top 5 regions by cases")
        elif exclude_china == "y":
            for region in region_records:
                if count == 5:
                    break
                if region.parent != "Mainland China" and region.name != "":
                    top_places.append(region.name)
                    top_place_data.append(region.cases)
                    count += 1
            plt.title("Top 5 regions by cases (excluding China)")

    plt.bar(top_places, top_place_data, color = "#87eab1")

    plt.xlabel("Countries")
    plt.ylabel("Cases")
    plt.show()


def animate_graph(records):

    country_records, region_records = prc.summary(records)
    visual_choice, place_choice, place = tui.visual_selection(records)

    global fig, ax
    fig, ax = plt.subplots()

    updates = []
    total = 0
    total_for_update = 0
    global y_data, x_labels
    y_data = []
    x_labels = []

    if place_choice == "a":
        if visual_choice == "c":

            for date in country_records:
                if date.last_update not in updates:
                    updates.append([date.last_update])
            dates = [i for n, i in enumerate(updates) if i not in updates[:n]]
            for i in range(len(dates)):
                for j in range(len(records)):
                    if dates[i][0] == records[j][4]:
                        total_for_update += int(records[j][5])
                dates[i].append(total_for_update)

            for i in range(len(dates)):
                y_data.append(dates[i][1])
            for i in range(len(dates)):
                x_labels.append(dates[i][0])

            all_cases_for_countries_animation = animation.FuncAnimation(fig, animate, frames=len(dates), interval=100, repeat=False)

        elif visual_choice == "d":

            for date in country_records:
                if date.last_update not in updates:
                    updates.append([date.last_update])
            dates = [i for n, i in enumerate(updates) if i not in updates[:n]]

            for i in range(len(dates)):
                for j in range(len(records)):
                    if dates[i][0] == records[j][4]:
                        total_for_update += int(records[j][6])
                dates[i].append(total_for_update)

            for i in range(len(dates)):
                y_data.append(dates[i][1])
            for i in range(len(dates)):
                x_labels.append(dates[i][0])

            all_deaths_for_countries_animation = animation.FuncAnimation(fig, animate, frames=len(dates), interval=100, repeat=False)

        elif visual_choice == "r":

            for date in country_records:
                if date.last_update not in updates:
                    updates.append([date.last_update])
            dates = [i for n, i in enumerate(updates) if i not in updates[:n]]

            for i in range(len(dates)):
                for j in range(len(records)):
                    if dates[i][0] == records[j][4]:
                        total_for_update += int(records[j][7])
                dates[i].append(total_for_update)

            for i in range(len(dates)):
                y_data.append(dates[i][1])
            for i in range(len(dates)):
                x_labels.append(dates[i][0])

            all_recoveries_for_countries_animation = animation.FuncAnimation(fig, animate, frames=len(dates), interval=100, repeat=False)

    elif place_choice == "c":
        if visual_choice == "c":
            pass

        elif visual_choice == "d":
            pass

        elif visual_choice == "r":
            pass

    elif place_choice == "r":
        if visual_choice == "c":
            pass

        elif visual_choice == "d":
            pass

        elif visual_choice == "r":
            pass

    plt.show()
    '''if visual_choice == "c":
        for cases in country_records:
            total += cases.cases

        for date in country_records:
            if date.last_update not in updates:
                updates.append([date.last_update])
        dates = [i for n, i in enumerate(updates) if i not in updates[:n]]

        for i in range(len(dates)):
            for j in range(len(records)):
                if dates[i][0] == records[j][4]:
                    total_for_update += int(records[j][5])
            dates[i].append(total_for_update)

        global y_data
        y_data = []
        global x_labels
        x_labels = []
        for i in range(len(dates)):
            y_data.append(dates[i][1])
        for i in range(len(dates)):
            x_labels.append(dates[i][0])

        cases_animation = animation.FuncAnimation(fig, animate, frames = len(dates), interval = 100, repeat = False)
        plt.show()

    elif visual_choice == "d":
        for deaths in country_records:
            total += deaths.deaths

        for date in country_records:
            if date.last_update not in updates:
                updates.append([date.last_update])

        for i in range(len(updates)):
            for j in range(len(records)):
                if updates[i][0] == records[j][4]:
                    total_for_update += int(records[j][6])
            updates[i].append(total_for_update)
            total_for_update = 0

        dates = [ii for n, ii in enumerate(updates) if ii not in updates[:n]]

    elif visual_choice == "r":
        for recoveries in country_records:
            total += recoveries.recovered

        for date in country_records:
            if date.last_update not in updates:
                updates.append([date.last_update])

        for i in range(len(updates)):
            for j in range(len(records)):
                if updates[i][0] == records[j][4]:
                    total_for_update += int(records[j][7])
            updates[i].append(total_for_update)
            total_for_update = 0

        dates = [ii for n, ii in enumerate(updates) if ii not in updates[:n]]'''

x1 = []
y1 = []


def animate(frame):

    x1.append(x_labels[frame])
    y1.append(y_data[frame])

    ax.plot(x1, y1, "r--")
