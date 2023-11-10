"""Request adapter performing actual API calls towards FIO endpoints
"""

from typing import Dict, Tuple, List, Optional
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from fio_wrapper.exceptions import UnknownFIOResponse
from fio_wrapper.urls import URLs


class FIOAdapter:
    """FIO Adapater

    Attributes:
        api_key (str, optional): FIO API-Key.
        version (str, optional): FIO API version.
        base_url (str, optional): FIO base url.
        ssl_verify (bool, optional): Verify https connection.
        timeout (float, optional): Request timeout in seconds.

    """

    def __init__(
        self,
        api_key: str = "",
        version: str = "1.0.0",
        base_url: str = "https://rest.fnar.net",
        ssl_verify: bool = True,
        timeout: float = 10.0,
    ):
        """Initializes the FIO adapter

        Args:
            api_key (str, optional): FIO API-Key. Defaults to "".
            version (str, optional): FIO API version. Defaults to "1.0.0".
            base_url (str, optional): FIO base url. Defaults to "https://rest.fnar.net".
            ssl_verify (bool, optional): Verify https connection. Defaults to True.
            timeout (float, optional): Request timeout in seconds. Defaults to 10.0.
        """
        self.api_key = api_key
        self.version = version
        self.base_url = base_url
        self.ssl_verify = ssl_verify
        self.urls = URLs(base_url=base_url)
        self.timeout = timeout

        if not ssl_verify:
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    def headers(self):
        return {"Authorization": self.api_key}

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
            response = requests.request(
                method=http_method,
                url=endpoint,
                verify=self.ssl_verify,
                headers=self.headers(),
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
