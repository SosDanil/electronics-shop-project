import pytest

from src.phone import Phone


@pytest.fixture
def test_item1():
    return Phone("Iphone", 100000, 15, 3)


def test_repr(test_item1):
    assert repr(test_item1) == "Phone('Iphone', 100000, 15, 3)"
