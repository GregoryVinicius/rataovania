import pygame
from jogo.entity import Entity

class Platform(Entity):
    def __init__(self):
        super().__init__("../resource/platform1.png", )

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def add_platform(self, x, y, width, height, sprite_path=None):
        pygame.platform = Platform()