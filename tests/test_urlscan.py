import vcr

from whistling.urlscan import URLScan


@vcr.use_cassette(
    "tests/fixtures/vcr_cassettes/urlscan.yaml", filter_headers=["API-Key"],
)
def test_report(urlscan_token: str):
    client = URLScan(urlscan_token)
    res = client.report("http://payplint.com.supports-billings.com/admin")
    assert res is not None
