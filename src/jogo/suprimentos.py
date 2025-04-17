# pylint: disable=import-error
import random

from jogo.entity import Entity
from jogo.item import Item


class Surpimentos(Entity):
    def __init__(self, itens_possiveis=None):       

    def dropar_item(self):
        """
        Faz o objeto dropar um item, se possível.

        :return: Um objeto Item ou None.
        """
        if (self.pode_dropar and self.itens_possiveis):
            item_escolhido = random.choice(self.itens_possiveis)
            return Item.Drop(item_escolhido)
        return None