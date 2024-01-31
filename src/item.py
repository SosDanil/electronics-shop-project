import csv
import os.path

from src.InstantiateCSVError import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты классов Item и Phone")
        return self.quantity + other.quantity

    @property
    def name(self):
        """Возвращает название товара"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Устанавливает новое название товара с ограничением в 10 символов"""
        if len(new_name) > 10:
            print("Длина наименования товара превышает 10 символов")
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Отсутствует файл {path}")
        cls.all.clear()
        with open(path, newline="", encoding="windows-1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if len(row) < 3:
                    raise InstantiateCSVError(path)
                cls(row["name"], float(row["price"]), int(row["quantity"]))
                print(row)
        # except FileNotFoundError:
        #     print(f"Отсутствует файл {path}")
        # except InstantiateCSVError:
        #     print(f"Файл {path} поврежден")

    @staticmethod
    def string_to_number(string: str) -> int | None:
        if string.isalpha():
            print("Нужно было ввести число")
            return None
        else:
            return int(float(string))
