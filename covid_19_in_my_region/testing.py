from threading import Thread

import covid_19_in_my_region.backend as backend

from covid_19_in_my_region import app


def test_regions_exist():
    with app.app_context():
        regions = backend.get_regions()
        assert len(regions) > 0


def test_fetch_data():
    with app.test_client() as c:
        for region in backend.available_regions:
            json_result = c.get('/fetch_data?region=' + region).get_json()
            assert json_result["region"] == region
            assert len(json_result["x"]) > 0
            assert len(json_result["x"]) == len(json_result["y"])
            assert len(json_result["y"]) == len(json_result["y_acc"])
