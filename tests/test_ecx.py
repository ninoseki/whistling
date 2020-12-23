import vcr

from whistling.ecx import ECX


@vcr.use_cassette(
    "tests/fixtures/vcr_cassettes/ecx.yaml", filter_headers=["authorization"],
)
def test_report(ecx_token: str):
    client = ECX(ecx_token)
    res = client.report("http://scurdepypl.hekpdekskvauthadmine.com/", brand="PayPal",)
    assert res is not None
