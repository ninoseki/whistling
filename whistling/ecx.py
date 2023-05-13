"""
Reporter class for APWG's eCX
"""
from datetime import datetime

import httpx

from whistling.abstract_reporter import AbstractReporter


def current_time() -> int:
    now = datetime.now()
    return int(datetime.timestamp(now))


def build_payload(
    url: str,
    brand: str | None = None,
    confidence_level: int | None = None,
    date_discovered: int | None = None,
):
    return {
        "brand": brand or "",
        "url": url,
        "confidence_level": confidence_level or 100,
        "date_discovered": date_discovered or current_time(),
    }


class ECX(AbstractReporter):
    def __init__(
        self,
        token: str,
        *,
        base_url: str = "https://api.ecrimex.net/phish",
    ):
        self.base_url = base_url
        self.token = token

        assert self.token is not None

    def report(self, url: str, **kwargs) -> httpx.Response:
        """Report the URL to eCX

        Args:
            url (str): The URL to report

        Keyword Args:
            brand (str):
            date_discovered (int): 10 digit epoch timestamp
            confidence_level (int): 50, 90, or 100

        Returns:
            httpx.Response: A response from eCX
        """
        brand: str | None = kwargs.get("brand", None)
        date_discovered: int | None = kwargs.get("date_discovered", None)
        confidence_level: int | None = kwargs.get("confidence_level", None)

        payload = build_payload(
            url=url,
            brand=brand,
            confidence_level=confidence_level,
            date_discovered=date_discovered,
        )
        headers = {"authorization": self.token}

        res = httpx.post(self.base_url, json=payload, headers=headers)
        res.raise_for_status()
        return res
