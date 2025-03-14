"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.InstantiateCSVError import InstantiateCSVError
from src.item import Item
from config import PATH_TO_CSV
from src.phone import Phone


@pytest.fixture
def test_item1():
    return Item("Samsung M3", 10000.0, 5)


@pytest.fixture
def test_item2():
    return Phone("Xiaomi", 7000.0, 150, 2)


@pytest.fixture
def test_item3():
    return Phone("Iphone", 100000.0, 15, 3)


def test_calculate_total_price(test_item1):
    assert test_item1.calculate_total_price() == 50000


def test_apply_discount(test_item1):
    test_item1.pay_rate = 0.5
    test_item1.apply_discount()
    assert test_item1.price == 5000


def test_string_to_number():
    assert Item.string_to_number("3") == 3
    assert Item.string_to_number("3.3") == 3
    assert Item.string_to_number("3.8") == 3
    assert Item.string_to_number("cat") is None


def test_instantiate_from_csv():
    Item.instantiate_from_csv(PATH_TO_CSV)
    assert len(Item.all) == 5
    item2 = Item.all[1]
    assert item2.name == "Ноутбук"
    assert item2.price == 1000
    assert item2.quantity == 3


def test_repr_and_str(test_item1):
    assert repr(test_item1) == "Item('Samsung M3', 10000.0, 5)"
    assert str(test_item1) == "Samsung M3"


def test_add(test_item1, test_item2, test_item3):
    total_quantity1 = test_item1 + test_item2  # объекты классов Item и Phone
    total_quantity2 = test_item2 + test_item3  # два объекта класса Phone
    assert total_quantity1 == 155
    assert total_quantity2 == 165


def test_instantiate_from_csv_raises():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('itemino.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../src/items_test.csv')

