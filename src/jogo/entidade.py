import pygame
from jogo.elementoGrafico import ElementoGrafico

class Entidade(ElementoGrafico):
    def __init__(self, imagem_path, posicao, escala=None, hitbox_offset=(0, 0), hitbox_tamanho=None):
        """
        Inicializa uma entidade com hitbox.

        :param imagem_path: Caminho para a imagem do sprite.
        :param posicao: Tupla (x, y) representando a posição inicial.
        :param escala: Tupla (largura, altura) para redimensionar a imagem (opcional).
        :param hitbox_offset: Deslocamento da hitbox em relação ao sprite (x, y).
        :param hitbox_tamanho: Tamanho da hitbox (largura, altura). Se None, usa o tamanho do sprite.
        """
        super().__init__(imagem_path, posicao, escala)
        self.hitbox_offset = hitbox_offset
        self.hitbox = self.rect.inflate(0, 0)  # Cria a hitbox com base no rect inicial
        if hitbox_tamanho:
            self.hitbox.size = hitbox_tamanho
        self.atualizar_hitbox()

    def atualizar_hitbox(self):
        """
        Atualiza a posição da hitbox com base na posição do sprite e no deslocamento.
        """
        self.hitbox.topleft = (
            self.rect.topleft[0] + self.hitbox_offset[0],
            self.rect.topleft[1] + self.hitbox_offset[1],
        )

    def desenhar_hitbox(self, tela, cor=(255, 0, 0)):
        """
        Desenha a hitbox na tela (útil para depuração).

        :param tela: Superfície do Pygame onde a hitbox será desenhada.
        :param cor: Cor da hitbox (padrão: vermelho).
        """
        pygame.draw.rect(tela, cor, self.hitbox, 1)

    def mover(self, dx, dy):
        """
        Move a entidade e atualiza a hitbox.

        :param dx: Deslocamento no eixo X.
        :param dy: Deslocamento no eixo Y.
        """
        super().mover(dx, dy)
        self.atualizar_hitbox()

    def colidiu_com(self, outra_entidade):
        """
        Verifica se a hitbox desta entidade colidiu com a hitbox de outra entidade.

        :param outra_entidade: Outro objeto da classe Entidade.
        :return: True se houver colisão, False caso contrário.
        """
        return self.hitbox.colliderect(outra_entidade.hitbox)