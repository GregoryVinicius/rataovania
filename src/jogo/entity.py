import pygame

class Entity():
    def __init__(self, imagem_path = None, position = None, scale = None, hitbox_size = None):
        """
        Inicializa uma entidade com hitbox.

        :param sprite: Caminho para a imagem do sprite.
        :param position: Tupla (x, y) representando a posição inicial.
        :param scale: Tupla (largura, altura) para redimensionar a imagem (opcional).
        :param hitbox_size: Tamanho da hitbox (largura, altura). Se None, usa o tamanho do sprite.
        """ 
        self.position = position
        self.sprite = imagem_path
        self.scale = scale
        self.hitbox_size = hitbox_size
        

    def atualizar_hitbox(self):
        """
        Atualiza a posição da hitbox com base na posição do sprite e no deslocamento.
        """
        # self.hitbox.topleft = (
        #     self.rect.topleft[0] + self.hitbox_offset[0],
        #     self.rect.topleft[1] + self.hitbox_offset[1],
        # )

    def desenhar_hitbox(self, tela, cor=(255, 0, 0)):
        """
        Desenha a hitbox na tela (útil para depuração).

        :param tela: Superfície do Pygame onde a hitbox será desenhada.
        :param cor: Cor da hitbox (padrão: vermelho).
        """
        pygame.draw.rect(tela, cor, self.hitbox_size, 1)

    def colidiu_com(self, outra_entidade):
        """
        Verifica se a hitbox desta entidade colidiu com a hitbox de outra entidade.

        :param outra_entidade: Outro objeto da classe Entidade.
        :return: True se houver colisão, False caso contrário.
        """
        # return self.hitbox.colliderect(outra_entidade.hitbox)