import pygame
from constant import GROUND_LEVEL
from jogo.entity import Entity

class Character(Entity, pygame.sprite.Sprite):
    def __init__(self, imagem_path, name, health, damage, defense, velocity, resultant_force=None, y_velocity=0, on_ground=False, x=0, y=0, width=50, height=50):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.sprite = imagem_path
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.velocity = velocity
        self.resultant_force = resultant_force
        self.y_velocity = y_velocity
        self.on_ground = on_ground
        self.ground_level = GROUND_LEVEL
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))

    def attack(self, target):
        damage = self.damage - target.defense
        if damage > 0:
            target.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

    def apply_gravity(self, gravity=None, time=1):
        if gravity is None:
            gravity = self.resultant_force or 0
    
        max_fall_speed = 13
    
        if not self.on_ground:
            self.y_velocity += gravity * time
            if self.y_velocity > max_fall_speed:
                self.y_velocity = max_fall_speed
            self.rect.y += self.y_velocity
    
            if self.rect.y >= self.ground_level:
                self.rect.y = self.ground_level
                self.y_velocity = 0
                self.on_ground = True
        else:
            self.y_velocity = 0
            
        