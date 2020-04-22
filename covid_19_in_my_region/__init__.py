from covid_19_in_my_region.backend import get_regions
from flask import Flask


def create_app():
    inner_app = Flask(__name__)

    with inner_app.app_context():
        get_regions()

    return inner_app


app = create_app()

import covid_19_in_my_region.routes
