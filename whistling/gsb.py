"""
Reporter class for Google Safe Browsing
"""
from typing import List, Optional

import httpx

from whistling.abstract_reporter import AbstractReporter


def build_payload(
    url: str,
    screenshot: Optional[str] = None,
    dom: Optional[str] = None,
    flags: Optional[List[str]] = None,
) -> list:
    return [url, None, screenshot, dom, None, flags]


class GSB(AbstractReporter):
    def __init__(
        self,
        base_url: str = "https://safebrowsing.google.com/safebrowsing/clientreport/crx-report",
        _=None,
    ):
        self.base_url = base_url

    def report(self, url: str, **kwargs) -> httpx.Response:
        """Report the URL to Google Safe Browsing

        Args:
            url (str): The URL to report

        Keyword Args:
            screenshot (str): screenshot of the malicious site as a base64 encoded PNG
            dom (str): DOM of the malicious site
            flags (List[str]): a set of flags for why the site was flagged as suspicious

        Returns:
            httpx.Response: A response from Google Safe Browsing
        """
        screenshot: Optional[str] = kwargs.get("screenshot", None)
        dom: Optional[str] = kwargs.get("dom", None)
        flags: Optional[List[str]] = kwargs.get("flags", None)

        payload = build_payload(url, screenshot=screenshot, dom=dom, flags=flags)

        res = httpx.post(self.base_url, json=payload)
        res.raise_for_status()
        return res
