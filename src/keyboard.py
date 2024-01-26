from src.item import Item
from src.mixin_language import MixinLanguage


class Keyboard(Item, MixinLanguage):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
