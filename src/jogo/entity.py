import pygame

class Entity():
    def __init__(self, imagem_path = None, position = None, scale = None, hitbox_size = None):
        pass
        

    def atualizar_hitbox(self):
        pass

    def desenhar_hitbox(self, tela, cor=(255, 0, 0)):
        pygame.draw.rect(tela, cor, self.hitbox_size, 1)

    def colidiu_com(self, outra_entidade):
        pass