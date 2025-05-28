import pygame

class Entity():
    def __init__(self, imagem_path = None, position = None, scale = None, hitbox_size = None):
        self.position = position
        self.sprite = imagem_path
        self.scale = scale
        self.hitbox_size = hitbox_size
        

    def atualizar_hitbox(self):

    def desenhar_hitbox(self, tela, cor=(255, 0, 0)):
        pygame.draw.rect(tela, cor, self.hitbox_size, 1)

    def colidiu_com(self, outra_entidade):
        pass