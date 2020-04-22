from covid_19_in_my_region.backend import latest_csv_from_dgg
from covid_19_in_my_region import app
import covid_19_in_my_region.backend as backend
from flask import request, jsonify

from flask import render_template
from flask import g


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/fetch_data", methods=['GET'])
def fetch_data():
    # Request args:
    region = request.args.get('region').replace("'", "")

    regions = backend.get_regions()
    x, y = regions[region]

    y_acc = []
    for i in range(len(y)):
        y_acc.append((y_acc[i-1] if i > 0 else 0) + y[i])

    return jsonify({"region": region, "x": x, "y": y, "y_acc": y_acc})
