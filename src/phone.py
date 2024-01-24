from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, sim_card_count):
        super().__init__(name, price, quantity)
        self.__sim_card_count = sim_card_count

    @property
    def sim_card_count(self):
        """Возвращает количество сим-карт"""
        return self.__sim_card_count

    @sim_card_count.setter
    def sim_card_count(self, count):
        if count <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            self.__sim_card_count = count

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim_card_count})"




