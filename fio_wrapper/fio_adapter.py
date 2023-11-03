"""Request adapter performing actual API calls towards FIO endpoints
"""

from typing import Dict, Tuple
import requests
from urllib3.exceptions import InsecureRequestWarning
from fio_wrapper.urls import URLs


class FIOAdapter:
    def __init__(
        self,
        api_key: str = "",
        version: str = "1.0.0",
        base_url: str = "https://rest.fnar.net",
        ssl_verify: bool = True,
    ):
        self.api_key = api_key
        self.version = version
        self.base_url = base_url
        self._ssl_verify = ssl_verify
        self.urls = URLs(base_url=base_url)

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
        err_codes=[],
    ) -> Tuple[int, any]:
        try:
            response = requests.request(
                method=http_method,
                url=endpoint,
                verify=self._ssl_verify,
                headers=self.headers(),
                params=params,
                json=data,
            )

            if response.status_code == 200:
                return 200, response.json()
            elif response.status_code in err_codes:
                return response.status_code, None
            else:
                return response.status_code, None

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
        err_codes=[],
    ) -> Tuple[int, any]:
        """Performs a GET request towards endpoint

        Args:
            endpoint (str): URL
            params (Dict, optional): GET parameters. Defaults to None.
            err_codes (list, optional): List of error codes to handle in calling function. Defaults to [].

        Returns:
            Tuple[int, any]: Request status code and request data
        """
        return self._do(
            http_method="GET",
            endpoint=endpoint,
            params=params,
            err_codes=err_codes,
        )

    def post(
        self, endpoint: str, params: Dict = None, data: Dict = None, err_codes=[]
    ) -> Tuple[int, any]:
        """Performs a POST request towards endpoint

        Args:
            endpoint (str): URL
            params (Dict, optional): POST parameters. Defaults to None.
            data (Dict, optional): POST data. Defaults to None.
            err_codes (list, optional): List of error codes to handle in calling function. Defaults to [].

        Returns:
            Tuple[int, any]: Request status code and request data
        """
        return self._do(
            http_method="POST",
            endpoint=endpoint,
            params=params,
            data=data,
            err_codes=err_codes,
        )
