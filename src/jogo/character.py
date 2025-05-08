# pylint: disable=too-many-arguments
from jogo.entity import Entity


class Character(Entity):
    def __init__(self, name, health, damage, defense, velocity, resultant_force=None, y_velocity=0, on_ground=False):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.velocity = velocity
        self.resultant_force = resultant_force  # Intensidade da gravidade
        self.y_velocity = y_velocity  # Velocidade vertical inicial
        self.on_ground = on_ground  # Verifica se o personagem está no chão

    def attack(self, target):
        damage = self.damage - target.defense
        if damage > 0:
            target.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

    def apply_gravity(self, gravity=None):
        if gravity is None:
            gravity = self.resultant_force
        if not self.on_ground:
            self.y_velocity += gravity
            self.rect.y += self.y_velocity