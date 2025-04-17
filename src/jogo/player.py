# pylint: disable=import-error
import pygame

from src.jogo.character import Character

class Player(Character):
    def __init__(self):
        super().__init__("Player 1", 100, 10, 10, 10)

    keys = pygame.key.get_pressed()

    def jump(self):
        pass
    
    def double_jump(self):
        pass
    
    def dash(self):
        pass
    
    def super_dash(self):
        pass