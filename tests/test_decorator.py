import pytest
from fio_wrapper import FIO, NoAPIKeyProvided
from fio_wrapper.exceptions import NotAuthenticated


@pytest.fixture()
def fio_nokey() -> FIO:
    return FIO()


@pytest.fixture()
def fio_key() -> FIO:
    return FIO(api_key="foo")


def test_apikey_required_keyerror(fio_nokey: FIO) -> None:
    with pytest.raises(NoAPIKeyProvided):
        fio_nokey.Sites.get(username="foo")


def test_apikey_required_none(fio_nokey: FIO) -> None:
    fio_nokey.Sites.adapter = None

    with pytest.raises(SystemExit):
        fio_nokey.Sites.get(username="foo")


def test_apikey_required_wrapped(requests_mock, fio_key: FIO) -> None:
    requests_mock.get(fio_key.urls.sites_get_url(username="foo"), status_code=401)

    with pytest.raises(NotAuthenticated):
        fio_key.Sites.get(username="foo")
