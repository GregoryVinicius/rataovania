# pylint: disable=import-error
from src.jogo.character import Character

class Enemy(Character):
    def __init__(self):
        self.name = "Inimigo"
        self.base_health = 100.0
        self.speed = 10.0
        self.damage = 10.0
        self.armor = 0.0

    def attack(self):
        pass

    def take_damage(self):
        pass

    def die(self):
        pass