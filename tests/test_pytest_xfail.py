import pytest


@pytest.mark.xfail(reason="Bug: fail known issue")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Bug: fail known issue")
def test_without_bug():
    assert 2 == 2

@pytest.mark.xfail(reason="Service is tempoary not available")
def test_external_serv_down():
    assert 3 == 5

