# pylint: disable=too-many-arguments
from jogo.entity import Entity


class Character(Entity):
    def __init__(self, name, health, damage, defense, velocity, gravity=0.5, y_velocity=0, on_ground=False):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.velocity = velocity
        self.gravity = gravity  # Intensidade da gravidade
        self.y_velocity = y_velocity  # Velocidade vertical inicial
        self.on_ground = on_ground  # Verifica se o personagem está no chão

    def attack(self, target):
        damage = self.damage - target.defense
        if damage > 0:
            target.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

    def apply_gravity(self):
        """Aplica a gravidade ao personagem."""
        if not self.on_ground:
            self.y_velocity += self.gravity  # Aumenta a velocidade vertical devido à gravidade
            self.rect.y += self.y_velocity  # Move o personagem para baixo
        else:
            self.y_velocity = 0  # Reseta a velocidade vertical ao tocar o chão
