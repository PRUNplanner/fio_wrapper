import pytest
from pyfio import FIOAdapter, FIO, EndpointNotImplemented


@pytest.fixture()
def ftx_fio() -> FIO:
    return FIO()


def test_fio_adapter_version_notimplemented() -> None:
    with pytest.raises(EndpointNotImplemented):
        FIO(version="0.0.0")


def test_fio_adapter_blankinit() -> None:
    adapter = FIOAdapter()

    assert adapter.api_key == ""
    assert adapter.version == "1.0.0"
    assert adapter.base_url == "https://rest.fnar.net"


def test_fio_adapter_custominit() -> None:
    adapter = FIOAdapter(api_key="foo", version="moo", base_url="coo", ssl_verify=False)

    assert adapter.api_key == "foo"
    assert adapter.version == "moo"
    assert adapter.base_url == "coo"


def test_fio_adapter_otherstatus(requests_mock) -> None:
    adapter = FIOAdapter()
    url = "https://foo.foo"

    requests_mock.get(url, status_code=204)
    (status, data) = adapter._do("get", url, err_codes=[300])

    assert status == 204
    assert data == None


def test_fio_adapter_request_exceptions(requests_mock) -> None:
    import requests.exceptions

    adapter = FIOAdapter()
    url = "https://foo.foo"

    with pytest.raises(requests.exceptions.Timeout):
        requests_mock.get(url, exc=requests.exceptions.Timeout)
        adapter._do("get", url)

    with pytest.raises(requests.exceptions.TooManyRedirects):
        requests_mock.get(url, exc=requests.exceptions.TooManyRedirects)
        adapter._do("get", url)

    with pytest.raises(SystemExit):
        requests_mock.get(url, exc=requests.exceptions.RequestException)
        adapter._do("get", url)
