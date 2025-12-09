import pytest

SYSTEM_VERSION = "v1.2.0"

@pytest.mark.skipif(SYSTEM_VERSION == "v1.2.0", reason="version is incorrect")
def test_system_version_valid():
    pass

@pytest.mark.skipif(SYSTEM_VERSION == "v1.2.0", reason="version is incorrect")
def test_system_version_invalid():
    pass



