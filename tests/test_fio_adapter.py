import pytest
import importlib.util
from requests_cache import CachedSession
from fio_wrapper import FIO, EndpointNotImplemented
from fio_wrapper.exceptions import UnknownFIOResponse


@pytest.fixture()
def ftx_fio() -> FIO:
    return FIO()


def test_fio_adapter_version_notimplemented() -> None:
    with pytest.raises(EndpointNotImplemented):
        FIO(version="0.0.0")


def test_fio_adapter_requests_cache() -> None:
    adapter = FIO(config="tests/config_cache.yml")

    assert adapter.config.cache == True
    assert importlib.util.find_spec("requests_cache") is not None
    assert type(adapter.adapter._session) == CachedSession


def test_fio_adapter_blankinit() -> None:
    adapter = FIO()

    assert adapter.config.api_key == None
    assert adapter.config.version == "1.0.0"
    assert adapter.config.base_url == "https://rest.fnar.net"


def test_fio_adapter_custominit() -> None:
    adapter = FIO(api_key="foo", version="1.0.0", base_url="coo", ssl_verify=False)

    assert adapter.config.api_key == "foo"
    assert adapter.config.version == "1.0.0"
    assert adapter.config.base_url == "coo"


def test_fio_adapter_otherstatus(requests_mock) -> None:
    adapter = FIO().adapter
    url = "https://foo.foo"

    requests_mock.get(url, status_code=204)

    with pytest.raises(UnknownFIOResponse):
        (status, data) = adapter._do("get", url, err_codes=[300])


def test_fio_adapter_request_exceptions(requests_mock) -> None:
    import requests.exceptions

    adapter = FIO().adapter
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
