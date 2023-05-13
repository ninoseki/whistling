import pytest
import vcr

from whistling.netcraft import Netcraft


@pytest.fixture
def client(netcraft_token: str) -> Netcraft:
    return Netcraft(netcraft_token)


@vcr.use_cassette("tests/fixtures/vcr_cassettes/netcraft.yaml")  # type: ignore
def test_report(client: Netcraft):
    res = client.report(
        "http://secure2.verification-personal-information.ini-ippat-jatim.or.id"
    )
    assert res is not None
