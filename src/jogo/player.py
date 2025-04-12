# pylint: disable=import-error
import pygame

from src.jogo.character import Character

class Player(Character):
    def __init__(self):
        self.name = "RatãoVania"
        self.base_health = 100.0
        self.speed = 10.0
        self.damage = 10.0
        self.armor = 0.0

    keys = pygame.key.get_pressed()

    def jump(self):
        pass
    
    def double_jump(self):
        pass
    
    def dash(self):
        pass
    
    def super_dash(self):
        pass