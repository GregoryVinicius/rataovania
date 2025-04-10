# pylint: disable=import-error
from jogo.entity import Entity

class Enemy(Entity):
    def __init__(self, name, health, damage, armor, speed):
        self.name = name
        self.healf = health
        self.damage = damage
        self.armor = armor
        self.speed = speed

    def attack(self):
        pass

    def take_damage(self):
        pass

    def die(self):
        pass