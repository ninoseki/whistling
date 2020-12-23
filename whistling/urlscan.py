"""
Reporter class for urlscan.io
"""
from typing import Optional

import httpx

from whistling.abstract_reporter import AbstractReporter


def build_payload(
    url: str,
    customagent: Optional[str] = None,
    referer: Optional[str] = None,
    visibility: Optional[str] = None,
) -> dict:
    d = {
        "url": url,
        "customagent": customagent,
        "referer": referer,
        "visibility": visibility,
    }
    return {k: v for k, v in d.items() if v is not None}


class URLScan(AbstractReporter):
    def __init__(
        self, token: str, base_url: str = "https://urlscan.io/api/v1/scan/",
    ):
        self.base_url = base_url
        self.token = token

    def report(self, url: str, **kwargs) -> httpx.Response:
        """[summary]

        Args:
            url (str): The URL to report

        Keyword Args:
            customagent (str): Override User-Agent for this scan
            referer (str): Override HTTP referer for this scan
            visibility (str): One of public, unlisted, private

        Returns:
            httpx.Response: [description]
        """
        assert self.token is not None

        customagent: Optional[str] = kwargs.get("customagent", None)
        referer: Optional[str] = kwargs.get("referer", None)
        visibility: Optional[str] = kwargs.get("visibility", None)

        payload = build_payload(
            url=url, customagent=customagent, referer=referer, visibility=visibility
        )
        headers = {"API-Key": self.token}

        res = httpx.post(self.base_url, json=payload, headers=headers)
        res.raise_for_status()
        return res
