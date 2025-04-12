# pylint: disable=too-many-arguments
from src.jogo.entity import Entity


class Character(Entity):
    def __init__(self, name, health, damage, defense, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.speed = speed

    def attack(self, target):
        damage = self.damage - target.defense
        if damage > 0:
            target.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0