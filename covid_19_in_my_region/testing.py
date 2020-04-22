import covid_19_in_my_region.backend as backend


def test_regions_exist():
    dgg_file = backend.latest_csv_from_dgg()
    regions = backend.construct_regions(dgg_file)
    assert len(regions) > 0
