# pylint: disable=import-error
import pygame

from jogo.entity import Entity

class Player(Entity):
    def __init__(self):
        self.base_health = 100.0
        self.speed = 10.0
        self.damage = 10.0
        self.armor = 0.0

    keys = pygame.key.get_pressed()
    def move(self, direction):
        pass
        # if(keys[K_d] or keys[K_RI]):
        #     self.Player.position += 1
        # elif if(keys[K_a] or keys[K_LEFT]):
            # self.Player.
    def jump(self):
        pass
    
    def double_jump(self):
        pass

    def attack(self):
        pass
    
    def dash(self):
        pass