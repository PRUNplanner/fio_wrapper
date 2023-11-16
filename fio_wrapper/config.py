import os
import logging
import yaml
import importlib.util
from typing import Optional
from typing import List
from typing import Dict
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

    # https://stackoverflow.com/a/15836901
    def data_merge(self, a, b):
        """merges b into a and return merged result

        Args:
            a (Dict): First dictionary
            b (Dict): Second dictionary

        NOTE:
            tuples and arbitrary objects are not handled as it is totally ambiguous what should happen
        """
        key = None
        # ## debug output
        # sys.stderr.write("DEBUG: %s to %s\n" %(b,a))
        try:
            if (
                a is None
                or isinstance(a, str)
                or isinstance(a, int)
                or isinstance(a, float)
            ):
                # border case for first run or if a is a primitive
                a = b
            elif isinstance(a, list):
                # lists can be only appended
                if isinstance(b, list):
                    # merge lists
                    a.extend(b)
                else:
                    # append to list
                    a.append(b)
            elif isinstance(a, dict):
                # dicts must be merged
                if isinstance(b, dict):
                    for key in b:
                        if key in a:
                            a[key] = self.data_merge(a[key], b[key])
                        else:
                            a[key] = b[key]
                else:
                    raise Exception(
                        'Cannot merge non-dict "%s" into dict "%s"' % (b, a)
                    )
            else:
                raise Exception('NOT IMPLEMENTED "%s" into "%s"' % (b, a))
        except TypeError as e:
            raise Exception(
                'TypeError "%s" in key "%s" when merging "%s" into "%s"'
                % (e, key, b, a)
            )
        return a

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

        # initialize data
        self._base_file = os.path.join(os.path.dirname(__file__), "base.yml")

        # base configuration
        with open(self._base_file, "r") as base_file:
            self.data = yaml.safe_load(base_file)

        # user config, if provided
        if user_config is not None:
            with open(user_config, "r") as user_file:
                user = yaml.safe_load(user_file)

                # self.data = self.dict_merge(self.data, user)
                self.data = self.data_merge(self.data, user)

    @property
    def versions(self) -> List[str]:
        """Gets the versions information from config

        Raises:
            SystemExit: No list of available FIO versions provided

        Returns:
            List[str]: List of versions
        """
        try:
            return self.data["fio"]["versions"]
        except Exception as exc:
            raise SystemExit("No list of available FIO versions provided") from exc

    @property
    def api_key(self) -> str:
        """Gets the FIO API key

        Returns:
            str: FIO API key or None
        """
        if self._api_key is not None:
            return self._api_key

        try:
            return self.data["fio"]["api_key"]
        except KeyError:
            # API Key can be blank
            return None

    @property
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
            return self.data["fio"]["version"]
        except Exception as exc:
            raise UnknownConfig("No version setting found") from exc

    @property
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
            return self.get("fio", "application")
        except KeyError as exc:
            raise UnknownConfig("No application setting found") from exc

    @property
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
            return self.data["fio"]["base_url"]
        except KeyError as exc:
            raise UnknownConfig("No base_url setting found") from exc

    @property
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
            return self.data["fio"]["timeout"]
        except KeyError as exc:
            raise UnknownConfig("No timeout setting found") from exc

    @property
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
            return self.data["fio"]["ssl_verify"]
        except KeyError as exc:
            raise UnknownConfig("No ssl_verify setting found") from exc

    @property
    def cache(self) -> bool:
        """Gets the cache usage status

        Returns:
            bool: Cache used, true or false
        """
        return self.data["cache"]["enabled"]

    @property
    def cache_default_expire(self) -> int:
        """Gets the cache default expiration time

        Returns:
            int: Expiration time in seconds
        """
        return self.data["cache"]["default_expire"]

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
            return self.data[section][option]
        except KeyError as exc:
            raise UnknownConfig() from exc

    def get_url(self, option: str) -> str:
        """Gets a url configuration element

        Args:
            option (str): Configuration option

        Returns:
            str: URL configuration parameter
        """

        try:
            return self.data["fio_urls"][self.version][option]
        except KeyError as exc:
            raise UnknownConfig() from exc

    def cache_url_expirations(self) -> Dict[str, any]:
        """Creates the dict for requests_cache url expirations

        Returns:
            Dict[str, any]: URL specific expiration settings
        """
        # check if requests-cache is installed
        if self.cache and importlib.util.find_spec("requests_cache") is not None:
            from requests_cache import DO_NOT_CACHE, NEVER_EXPIRE

            try:
                expiration_list: Dict[str, any] = {}

                # walk through given urls
                for url, expiration in self.data["cache"]["urls"].items():
                    # decide on potential values coming as int or str:
                    #   int = take as seconds
                    if isinstance(expiration, int):
                        expiration_list[url] = expiration
                    #   NEVER_EXPIRE
                    elif expiration == "NEVER_EXPIRE":
                        expiration_list[url] = NEVER_EXPIRE
                    #   DO_NOT_CACHE
                    elif expiration == "DO_NOT_CACHE":
                        expiration_list[url] = DO_NOT_CACHE
                    else:
                        logger.warn(
                            "Unknown expiration configuration: %s | %s", url, expiration
                        )
                return expiration_list
            # no cache urls defined, return empty list
            except KeyError:
                return {}

        else:
            return {}
