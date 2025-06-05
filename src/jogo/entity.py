import pygame

class Entity():
    #criar vetor para posição e tamanho
    def __init__(self, sprite = None, positon = (None, None), scale = None, hitbox_size = (None, None)):
        self.sprite = sprite
        self.position = pygame.math.Vector2(position)
        self.scale = scale
        self.hitbox_size = pygame.math.Vector2(hitbox_size)
       
    def draw_hitbox(self):
        self.hitbox_size = pygame.Rect(self.position_x, self.position_y, self.hitbox_size_x, self.hitbox_size_y)

    def collided_with(self, outra_entidade):
        pass