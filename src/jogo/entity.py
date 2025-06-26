import pygame

class Entity():
    def __init__(self, sprite, positon, scale, hitbox_size):
        self.sprite = sprite
        self.position = pygame.Vector2(positon)
        self.scale = scale
        self.hitbox_size = pygame.Vector2(hitbox_size)
       
    def draw_hitbox(self):
        self.hitbox_size = pygame.Rect(self.position_x, self.position_y, self.hitbox_size_x, self.hitbox_size_y)

    def collided_with(self, ):
        