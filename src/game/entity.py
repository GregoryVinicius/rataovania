import pygame

class Entity():
    def __init__(self, sprite, positon, hitbox_size):
        self.sprite = sprite
        self.position = pygame.Vector2(positon)
        # self.scale = scale
        self.hitbox_size = pygame.Vector2(hitbox_size)
       
    def draw_hitbox(self):
        self.hitbox_size = pygame.Rect(self.position_x, self.position_y, self.hitbox_size_x, self.hitbox_size_y)

    def collided_with(self, other):
        return self.hitbox.colliderect(other.hitbox)