import pygame
from game.entity import Entity


class Platform(Entity):
    def __init__(self, x, y, width, height, sprite_path="../resource/platform1.png"):
        super().__init__(sprite=sprite_path, positon= [x, y],scale= hitbox_size=[height, width])
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = pygame.Rect(self.positon[0], self.position[1], self.hitbox_size[0], self.hitbox_size[1])

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    @staticmethod
    def add_platform(x, y, width, height, sprite_path="../resource/platform1.png"):
        return Platform(x, y, width, height, sprite_path)
