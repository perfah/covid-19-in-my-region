from covid_19_in_my_region.backend import latest_csv_from_dgg
from covid_19_in_my_region import app
import covid_19_in_my_region.backend as backend
from flask import request

from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/stockholm")
def stockholm_proof_of_concept():
    print("Plotting stockholm data")
    region = "stockholm"
    dgg_file = backend.latest_csv_from_dgg()
    regions = backend.construct_regions(dgg_file)
    return render_template('graph_plot.html', X=regions[region].format_x(), Y=regions[region].format_y())


@app.route("/vg")
def vg_proof_of_concept():
    print("Plotting vg data")
    region = "västra_götaland"
    dgg_file = backend.latest_csv_from_dgg()
    regions = backend.construct_regions(dgg_file)
    return render_template('graph_plot.html', X=regions[region].format_x(), Y=regions[region].format_y())
