import pygame
from jogo.Platform import Platform

class Level:
    def __init__(self, background):
        self.background = background
        self.enemies = []
        self.load()

    def load(self):
        Platform.add_platform(100, 300, 200, 50, "../resource/platform1.png")
        Platform.add_platform(400, 200, 200, 50, "../resource/platform1.png")

    def update(self, screen, player):
        self.draw(screen)
        
        
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        Platform.draw(screen)