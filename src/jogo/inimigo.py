# pylint: disable=import-error
from jogo.entity import Entity

class Enemy(Entity):
    def __init__(self, health, damage, armor):
        self.healf = health
        self.damage = damage
        self.armor = armor

    def attack(self):
        pass

    def take_damage(self):
        pass

    def die(self):
        pass