import covid_19_in_my_region.backend as backend

from covid_19_in_my_region import app


def test_regions_exist():
    with app.app_context():
        regions = backend.get_regions()
        assert len(regions) > 0
