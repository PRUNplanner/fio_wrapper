"""Request adapter performing actual API calls towards FIO endpoints
"""
import logging
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
import importlib.util

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from fio_wrapper.config import Config

from fio_wrapper.exceptions import UnknownFIOResponse

logger = logging.getLogger(__name__)


class FIOAdapter:
    """FIO Adapater"""

    def __init__(self, config: Config, header: Dict[str, str]):
        """Initializes the FIO adapter

        Args:
            config (Config): Wrapper configuration.
            header (Dict[str, str]): FIO Header.
        """

        self.config = config
        self.header = header
        self.ssl_verify = self.config.ssl_verify
        self.timeout = self.config.timeout

        if not self.ssl_verify:
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        # register a session based on requests.session or, if installed
        # requests-cache session handler

        if self.config.cache and importlib.util.find_spec("requests_cache") is not None:
            logger.debug("Using requests-cache Session")
            from requests_cache import CachedSession

            self._session = CachedSession(
                cache_name="fio_wrapper",
                backend="memory",
                expire_after=self.config.cache_default_expire,
                urls_expire_after=self.config.cache_url_expirations(),
                cache_control=False,
            )
        else:
            logger.debug("Using request Session")
            self._session = requests.session()

    def _do(
        self,
        http_method: str,
        endpoint: str,
        params: Dict = None,
        data: Dict = None,
        err_codes: Optional[List[int]] = None,
        timeout: Optional[float] = None,
    ) -> Tuple[int, any]:
        try:
            logger.debug(
                "Calling (%s) %s with params: %s | data: %s",
                http_method,
                endpoint,
                params,
                data,
            )

            response = self._session.request(
                method=http_method,
                url=endpoint,
                verify=self.ssl_verify,
                headers=self.header,
                params=params,
                json=data,
                timeout=timeout if timeout is not None else self.timeout,
            )

            # successful FIO response
            if response.status_code == 200:
                return 200, response.json()
            # FIO response in provided codes to catch in endpoint
            elif isinstance(err_codes, List) and response.status_code in err_codes:
                return response.status_code, None
            # other FIO response, not accounted for
            else:
                raise UnknownFIOResponse()

        except requests.exceptions.Timeout as errt:
            raise requests.exceptions.Timeout() from errt
        except requests.exceptions.TooManyRedirects as errr:
            raise requests.exceptions.TooManyRedirects from errr
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def get(
        self,
        endpoint: str,
        params: Dict = None,
        err_codes: Optional[List[int]] = None,
        timeout: Optional[float] = None,
    ) -> Tuple[int, any]:
        """Performs a GET request towards endpoint

        Args:
            endpoint (str): URL
            params (Dict, optional): GET parameters. Defaults to None.
            err_codes (List[int], optional): List of error codes to handle in calling function. Defaults to None.
            timeout (float, optional): Request timeout in seconds. Defaults to None.

        Returns:
            Tuple[int, any]: Request status code and request data
        """
        return self._do(
            http_method="GET",
            endpoint=endpoint,
            params=params,
            err_codes=err_codes,
            timeout=timeout,
        )

    def post(
        self,
        endpoint: str,
        params: Dict = None,
        data: Dict = None,
        err_codes: Optional[List[int]] = None,
        timeout: Optional[float] = None,
    ) -> Tuple[int, any]:
        """Performs a POST request towards endpoint

        Args:
            endpoint (str): URL
            params (Dict, optional): POST parameters. Defaults to None.
            data (Dict, optional): POST data. Defaults to None.
            err_codes (List[int], optional): List of error codes to handle in calling function. Defaults to None.
            timeout (float): Request timeout in seconds. Defaults to None.

        Returns:
            Tuple[int, any]: Request status code and request data
        """
        return self._do(
            http_method="POST",
            endpoint=endpoint,
            params=params,
            data=data,
            err_codes=err_codes,
            timeout=timeout,
        )
