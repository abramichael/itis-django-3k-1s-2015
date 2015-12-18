from utils import fact
import pytest


def test_fact():
    assert fact(3) == 6

def test_fact2():
    assert fact(4) == 24

def test_fact3():
    with pytest.raises(ValueError):
        n = fact(-1)
