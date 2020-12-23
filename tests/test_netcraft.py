import vcr

from whistling.netcraft import Netcraft


@vcr.use_cassette("tests/fixtures/vcr_cassettes/netcraft.yaml")
def test_report(netcraft_token: str):
    client = Netcraft(netcraft_token)
    res = client.report(
        "http://secure2.verification-personal-information.ini-ippat-jatim.or.id"
    )
    assert res is not None
