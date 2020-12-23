"""
Reporter class for Netcraft
"""
import httpx

from whistling.abstract_reporter import AbstractReporter


def build_payload(url: str, email: str):
    return {"urls": [url], "email": email}


class Netcraft(AbstractReporter):
    def __init__(
        self, token, base_url: str = "https://report.netcraft.com/api/v2/report/urls",
    ):
        self.base_url = base_url
        self.token = token

    def report(self, url: str, **_) -> httpx.Response:
        assert self.token is not None

        payload = build_payload(url, self.token)

        res = httpx.post(self.base_url, json=payload)
        res.raise_for_status()
        return res
