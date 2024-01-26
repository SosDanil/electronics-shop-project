import pytest

from src.keyboard import Keyboard


@pytest.fixture
def test_keyboard1():
    return Keyboard('Dragon Fly 2000', 15000, 42)


def test_str(test_keyboard1):
    assert str(test_keyboard1) == 'Dragon Fly 2000'


def test_change_lang(test_keyboard1):
    assert test_keyboard1.language == "EN"
    test_keyboard1.change_lang()
    assert test_keyboard1.language == "RU"
