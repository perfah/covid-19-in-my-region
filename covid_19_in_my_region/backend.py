import wget

import os.path, time, datetime
from datetime import datetime as dt
import csv23
from covid_19_in_my_region.regional_plot import RegionalPlot

from flask import g


def get_regions():
    csv_file, updated = latest_csv_from_dgg()

    if updated or not hasattr(g, 'cached_regions'):
        g.cached_regions = construct_regions(csv_file)

    return g.cached_regions


def latest_csv_from_dgg():
    filename = "dgg_data.csv"
    today = dt.today().date()

    try:
        up_to_date = dt.fromtimestamp(os.path.getmtime(filename)).date() == today
    except OSError:
        up_to_date = False

    if up_to_date:
        print("Using cached csv-data for today's date: " + str(today))
    else:
        if os.path.exists(filename):
            os.remove(filename)

        print("Downloading new data for today's date: " + str(today) + "...")
        wget.download("https://free.entryscape.com/store/360/resource/15", filename)
        print("\nDone!")

    return filename, up_to_date


def construct_regions(csv_file):
    # Last column:
    available_regions = [
        'blekinge', 'dalarna', 'gotland', 'gävleborg', 'halland', 'jämtland', 'jönköping', 'kalmar', 'kronoberg',
        'norrbotten', 'skåne', 'stockholm', 'södermanland', 'uppsala', 'värmland', 'västerbotten', 'västernorrland',
        'västmanland', 'västra_götaland', 'örebro', 'östergötland'
    ]

    regions = dict()
    for region_name in available_regions:
        regions[region_name] = [], []

    with csv23.open_csv(csv_file) as reader:
        # Iterate the current row/day:
        for row in reversed(list(reader)[1:]):
            # total_cases = row[0]
            # acc_cases = row[1]
            novel_regional_cases = row[2:24]
            # novel_iva_cases = row[25]
            # acc_iva_cases = row[26]
            date = row[27]

            for i, reg in enumerate(regions):
                x, y = regions[reg]
                x.append(str(date + " 00:00:00"))
                y.append(int(novel_regional_cases[i]))

    return regions
