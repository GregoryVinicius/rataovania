# pylint: disable=too-many-arguments
# pylint: disable=import-error
from jogo.entity import Entity

class Item(Entity):
    def __init__(self, name, item_type, consumable, cure, drop_chance):
        self.name = name
        self.item_type = item_type
        self.consumable = consumable 
        self.cure = cure
        self.drop_chance = drop_chance
        
    def Equip(self):
        pass

    def Use(self):
        pass

    def Drop(self):
        pass

    def Discard(self):
        pass
