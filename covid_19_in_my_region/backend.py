import wget

import os.path, time, datetime
from datetime import datetime as dt
import csv23
from covid_19_in_my_region.regional_plot import RegionalPlot


def latest_csv_from_dgg():
    filename = "dgg_data.csv"
    today = dt.today().date()

    try:
        up_to_date = dt.fromtimestamp(os.path.getmtime(filename)).date() == today
    except OSError:
        up_to_date = False

    if up_to_date:
        print("Using cached data for today's date: " + str(today))
    else:
        os.remove(filename)
        wget.download("https://free.entryscape.com/store/360/resource/15", filename)
        print("Downloaded new data for today's date: " + str(today))

    return filename


def construct_regions(csv_file):
    # Last column:
    available_regions = [
        'blekinge', 'dalarna', 'gotland', 'gävleborg', 'halland', 'jämtland', 'jönköping', 'kalmar', 'kronoberg',
        'norrbotten', 'skåne', 'stockholm', 'södermanland', 'uppsala', 'värmland', 'västerbotten', 'västernorrland',
        'västmanland', 'västra_götaland', 'örebro', 'östergötland'
    ]

    regions = dict()
    for region_name in available_regions:
        regions[region_name] = RegionalPlot()

    with csv23.open_csv(csv_file) as reader:
        # Iterate the current row/day:
        for row in reversed(list(reader)[1:]):
            # total_cases = row[0]
            # acc_cases = row[1]
            novel_regional_cases = row[2:24]
            # novel_iva_cases = row[25]
            # acc_iva_cases = row[26]
            date = row[27]

            for i, region_name in enumerate(regions):
                regions[region_name].insert_data_point("\"" + date + " 00:00:00" + "\"", novel_regional_cases[i])

    return regions
