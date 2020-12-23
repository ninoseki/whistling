import pytest
from environs import Env

env = Env()
env.read_env()


@pytest.fixture
def ecx_token() -> str:
    return env.str("ECX_API_KEY", "")


@pytest.fixture
def netcraft_token() -> str:
    return env.str("NETCRAFT_EMAIL", "")


@pytest.fixture
def urlscan_token() -> str:
    return env.str("URLSCAN_API_KEY", "")
