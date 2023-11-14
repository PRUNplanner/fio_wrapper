import os
import logging
from configparser import ConfigParser, NoSectionError, NoOptionError
from typing import Optional, List

from fio_wrapper.exceptions import UnknownConfig

logger = logging.getLogger(__name__)


class Config:
    def __init__(
        self,
        api_key: Optional[str],
        version: Optional[str],
        application: Optional[str],
        base_url: Optional[str],
        timeout: Optional[float],
        user_config: Optional[str],
    ):
        # FIO instantiation overwrites
        self._api_key = api_key
        self._version = version
        self._application = application
        self._base_url = base_url
        self._timeout = timeout

        # converters
        converters = {"list": lambda x: [i.strip() for i in x.split(",")]}

        # initialize data
        # ConfigParser handles succession by order of read()
        self.data: ConfigParser = ConfigParser(converters=converters)
        self.data.read(os.path.join(os.path.dirname(__file__), "base.ini"))

        # user config
        if user_config is not None:
            self.data.read(user_config)

    def versions(self) -> List[str]:
        try:
            return self.data.getlist("FIO", "versions")
        except Exception as exc:
            raise SystemExit("No list of available FIO versions provided") from exc

    def api_key(self) -> str:
        if self._api_key is not None:
            return self._api_key

        try:
            return self.get("FIO", "api_key")
        except UnknownConfig:
            # API Key can be blank
            return None

    def version(self) -> str:
        if self._version is not None:
            return self._version

        try:
            return self.get("FIO", "version")
        except Exception as exc:
            raise UnknownConfig("No version setting found") from exc

    def application(self) -> str:
        if self._application is not None:
            return self._application

        try:
            return self.get("FIO", "application")
        except (NoSectionError, NoOptionError) as exc:
            raise UnknownConfig("No application setting found") from exc

    def base_url(self) -> str:
        if self._base_url is not None:
            return self._base_url

        try:
            return self.get("FIO", "base_url")
        except Exception as exc:
            raise UnknownConfig("No base_url setting found") from exc

    def timeout(self) -> float:
        if self._timeout is not None:
            return self._timeout

        try:
            # timeout value must be float
            return float(self.get("FIO", "timeout"))
        except Exception as exc:
            raise UnknownConfig("No timeout setting found") from exc

    def get(self, section: str, option: str) -> str:
        logger.debug("get(): %s | %s", section, option)
        try:
            return self.data.get(section, option)
        except (NoSectionError, NoOptionError) as exc:
            raise UnknownConfig() from exc

    def get_versioned(self, section: str, option: str) -> str:
        option = f"{self.version()}_{option}"

        logger.debug("get_versioned(): %s | %s", section, option)

        return self.get(section, option)
