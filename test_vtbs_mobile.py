import pytest
from Fixtures.FlatFixture import FlatFixture


@pytest.fixture
def fix(request):
    product = request.config.getoption("--product")
    fixture = None
    if product == "Flat":
        fixture = FlatFixture()
    return fixture


def test_vtbs_mobile(fix):
    fix.open_mobile_page()
    fix.fill_mobile_frame()
    input()

