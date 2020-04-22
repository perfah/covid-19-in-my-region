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
    region = request.args.get('region')
    accumulate = request.args.get('acc')

    regions = backend.get_regions()
    x, y = regions[region]

    if accumulate == 'true':
        y_mod = []
        for i in range(len(y)):
            y_mod.append((y_mod[i-1] if i > 0 else 0) + y[i])

        return jsonify({"region": region, "x": x, "y": y_mod, "acc": "true"})
    else:
        return jsonify({"region": region, "x": x, "y": y, "acc": "false"})
