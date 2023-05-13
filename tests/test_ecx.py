import pytest
import vcr

from whistling.ecx import ECX


@pytest.fixture
def client(ecx_token: str) -> ECX:
    return ECX(ecx_token)


@vcr.use_cassette(
    "tests/fixtures/vcr_cassettes/ecx.yaml",
    filter_headers=["authorization"],
)  # type: ignore
def test_report(client: ECX):
    res = client.report("http://scurdepypl.hekpdekskvauthadmine.com/", brand="PayPal")
    assert res is not None
