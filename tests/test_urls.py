import pytest
from pyfio.urls import URLs


@pytest.fixture
def url() -> URLs:
    return URLs(base_url="foo")


def test_url_base(url):
    assert url.base_url == "foo"


def test_material_url(url):
    assert url.material_url() == "foo/material"
