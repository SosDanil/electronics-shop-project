"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from config import PATH_TO_CSV


item1 = Item("Samsung M3", 10000.0, 5)  # тестовый экземпляр


def test_calculate_total_price():
    assert item1.calculate_total_price() == 50000


def test_apply_discount():
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5000


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


def test_repr():
    assert repr(item1) == "Item('Samsung M3', 10000.0, 5)"
    assert str(item1) == "Samsung M3"
