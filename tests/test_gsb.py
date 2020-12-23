import vcr

from whistling.gsb import GSB


@vcr.use_cassette("tests/fixtures/vcr_cassettes/gsb.yaml")
def test_report():
    client = GSB()
    res = client.report(
        "http://secure2.verification-personal-information.ini-ippat-jatim.or.id"
    )
    assert res is not None
