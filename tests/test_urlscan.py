import pytest
import vcr

from whistling.urlscan import URLScan


@pytest.fixture
def client(urlscan_token: str) -> URLScan:
    return URLScan(urlscan_token)


@vcr.use_cassette("tests/fixtures/vcr_cassettes/urlscan.yaml", filter_headers=["API-Key"])  # type: ignore
def test_report(client: URLScan):
    res = client.report("http://payplint.com.supports-billings.com/admin")
    assert res is not None
