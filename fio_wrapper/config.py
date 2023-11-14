import os
import logging
from configparser import ConfigParser, NoSectionError, NoOptionError
from typing import Optional, List

from fio_wrapper.exceptions import UnknownConfig

logger = logging.getLogger(__name__)


class Config:
    """FIO Wrapper configuration class

    Attributes:
        _api_key (str, optional): FIO API key
        _version (str, optional): FIO API version
        _application (str, optional): Application name
        _base_url (str, optional): FIO base url
        _timeout (float, optional): FIO generic timeout
        _ssl_verify (bool, optional): Request ssl verification

        data (ConfigParser): Configuration Parser

    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        version: Optional[str] = None,
        application: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: Optional[float] = 10.0,
        ssl_verify: Optional[bool] = True,
        user_config: Optional[str] = None,
    ) -> None:
        """Initializes the configuration

        Args:
            api_key (Optional[str]): FIO API key. Defaults to None.
            version (Optional[str]): FIO API version. Defaults to None.
            application (Optional[str]): Application name. Defaults to None.
            base_url (Optional[str]): FIO base url. Defaults to None.
            timeout (Optional[float]): FIO generic timeout. Defaults to 10.0.
            ssl_verify (Optional[bool]): Request ssl verification. Defaults to True.
            user_config (Optional[str]): User configuration file. Defaults to None.
        """
        # FIO instantiation overwrites
        self._api_key = api_key
        self._version = version
        self._application = application
        self._base_url = base_url
        self._timeout = timeout
        self._ssl_verify = ssl_verify

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
        """Gets the versions information from config

        Raises:
            SystemExit: No list of available FIO versions provided

        Returns:
            List[str]: List of versions
        """
        try:
            return self.data.getlist("FIO", "versions")
        except Exception as exc:
            raise SystemExit("No list of available FIO versions provided") from exc

    def api_key(self) -> str:
        """Gets the FIO API key

        Returns:
            str: FIO API key or None
        """
        if self._api_key is not None:
            return self._api_key

        try:
            return self.get("FIO", "api_key")
        except UnknownConfig:
            # API Key can be blank
            return None

    def version(self) -> str:
        """Gets the FIO version specified

        Raises:
            UnknownConfig: No version setting found

        Returns:
            str: FIO API version
        """
        if self._version is not None:
            return self._version

        try:
            return self.get("FIO", "version")
        except Exception as exc:
            raise UnknownConfig("No version setting found") from exc

    def application(self) -> str:
        """Gets the application name

        Raises:
            UnknownConfig: No application setting found

        Returns:
            str: Application name
        """
        if self._application is not None:
            return self._application

        try:
            return self.get("FIO", "application")
        except (NoSectionError, NoOptionError) as exc:
            raise UnknownConfig("No application setting found") from exc

    def base_url(self) -> str:
        """Gets the FIO base url

        Raises:
            UnknownConfig: No base_url setting found

        Returns:
            str: FIO base url
        """
        if self._base_url is not None:
            return self._base_url

        try:
            return self.get("FIO", "base_url")
        except Exception as exc:
            raise UnknownConfig("No base_url setting found") from exc

    def timeout(self) -> float:
        """Gets the timeout parameter

        Raises:
            UnknownConfig: No timeout setting found

        Returns:
            float: Timeout parameter
        """
        if self._timeout is not None:
            return self._timeout

        try:
            # timeout value must be float
            return float(self.get("FIO", "timeout"))
        except Exception as exc:
            raise UnknownConfig("No timeout setting found") from exc

    def ssl_verify(self) -> float:
        """Gets the ssl verification parameter

        Raises:
            UnknownConfig: No ssl_verify setting found

        Returns:
            float: Seconds as float of request timeout
        """
        if self._ssl_verify is not None:
            return self._ssl_verify

        try:
            return bool(self.get("FIO", "ssl_verify"))
        except Exception as exc:
            raise UnknownConfig("No ssl_verify setting found") from exc

    def get(self, section: str, option: str) -> str:
        """Gets a configuration element

        Args:
            section (str): Configuration section
            option (str): Configuration option

        Raises:
            UnknownConfig: Configuration not found

        Returns:
            str: Configuration element
        """
        logger.debug("get(): %s | %s", section, option)
        try:
            return self.data.get(section, option)
        except (NoSectionError, NoOptionError) as exc:
            raise UnknownConfig() from exc

    def get_versioned(self, section: str, option: str) -> str:
        """Gets a versioned configuration element

        Args:
            section (str): Configuration section
            option (str): Configuration option

        Returns:
            str: Versioned configuration element (e.g., 1.0.0_base)
        """
        option = f"{self.version()}_{option}"

        logger.debug("get_versioned(): %s | %s", section, option)

        return self.get(section, option)
