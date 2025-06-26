import pygame
from jogo.entity import Entity


class Platform(Entity):
    def __init__(self, x, y, width, height, sprite_path="../resource/platform1.png"):
        super().__init__(sprite_path)
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    @staticmethod
    def add_platform(x, y, width, height, sprite_path="../resource/platform1.png"):
        return Platform(x, y, width, height, sprite_path)
