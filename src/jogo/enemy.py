# pylint: disable=import-error
from jogo.character import Character

class Enemy(Character):
    def __init__(self):
        super().__init__("Inimigo 1", 100, 10, 10, 10)

    def attack(self):
        pass

    def take_damage(self):
        pass

    def die(self):
        pass