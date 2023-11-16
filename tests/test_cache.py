import pytest
from fio_wrapper import FIO, Config
from fio_wrapper.exceptions import UnknownConfig


@pytest.fixture(scope="class")
def standard_config() -> Config:
    fio = FIO()
    return fio.adapter.config


def test_cache_data_merge(standard_config: Config) -> None:
    config = standard_config

    # merge list
    a = {"l": [1, 2, 3]}
    b = {"l": [4]}

    merged = config.data_merge(a, b)
    assert merged["l"] == [1, 2, 3, 4]

    # append list
    a = {"l": [1, 2, 3]}
    b = {"l": 4}
    merged = config.data_merge(a, b)
    assert merged["l"] == [1, 2, 3, 4]

    # can't merge non-dict
    a = {"l": {"foo": "moo"}}
    b = {"l": 1}
    with pytest.raises(Exception):
        config.data_merge(a, b)

    # can only merge Dict, None, str, int, float
    a = standard_config
    b = {"l": 1}
    with pytest.raises(Exception):
        config.data_merge(a, b)


def test_cache_properties(standard_config: Config) -> None:
    config = standard_config

    config._application = "foo"
    assert config.application == "foo"

    config._timeout = 5
    assert config.timeout == 5

    config._ssl_verify = None
    assert config.ssl_verify == True


def test_cache_get(standard_config: Config) -> None:
    with pytest.raises(UnknownConfig):
        standard_config.get("foo", "moo")


def test_cache_get_url(standard_config: Config) -> None:
    config = standard_config

    config.data["cache"]["urls"] = {
        "*/material/*": 3600,
        "*/exchange/all": "NEVER_EXPIRE",
        "*/exchange/full": "DO_NOT_CACHE",
    }

    with pytest.raises(UnknownConfig):
        config.get_url("foo")


def test_cache_url_expirations_with_requests_cache_installed(
    standard_config, monkeypatch
):
    monkeypatch.setattr("importlib.util.find_spec", lambda x: True)
    monkeypatch.setattr("requests_cache.DO_NOT_CACHE", 1)
    monkeypatch.setattr("requests_cache.NEVER_EXPIRE", 2)

    standard_config.data = {
        "cache": {
            "enabled": True,
            "urls": {
                "url1": 10,
                "url2": "NEVER_EXPIRE",
                "url3": "DO_NOT_CACHE",
                "url4": "unknown_value",
            },
        }
    }

    result = standard_config.cache_url_expirations()

    expected_result = {
        "url1": 10,
        "url2": 2,  # Converted from "NEVER_EXPIRE"
        "url3": 1,  # Converted from "DO_NOT_CACHE"
    }

    assert result == expected_result


def test_cache_url_expirations_with_requests_cache_not_installed(
    standard_config, monkeypatch
):
    monkeypatch.setattr("importlib.util.find_spec", lambda x: None)

    standard_config.data = {
        "cache": {
            "enabled": True,
            "urls": {
                "url1": 10,
                "url2": "NEVER_EXPIRE",
                "url3": "DO_NOT_CACHE",
                "url4": "unknown_value",
            },
        }
    }

    result = standard_config.cache_url_expirations()

    assert result == {}


def test_cache_url_expirations_with_cache_disabled(standard_config, monkeypatch):
    monkeypatch.setattr("importlib.util.find_spec", lambda x: True)

    standard_config.data = {
        "cache": {
            "enabled": False,
            "urls": {
                "url1": 10,
                "url2": "NEVER_EXPIRE",
                "url3": "DO_NOT_CACHE",
                "url4": "unknown_value",
            },
        }
    }

    result = standard_config.cache_url_expirations()

    assert result == {}
