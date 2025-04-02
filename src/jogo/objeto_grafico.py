# pylint: disable=import-error
import random

from jogo.entity import Entity


class ObjetoGrafico(Entity):
    def __init__(self, pode_dropar=False, itens_possiveis=None):
        """
        Inicializa o objeto gráfico.

        :param imagem_path: Caminho para a imagem do objeto.
        :param posicao: Tupla (x, y) representando a posição inicial.
        :param escala: Tupla (largura, altura) para redimensionar a imagem (opcional).
        :param pode_dropar: Define se o objeto pode dropar itens.
        :param itens_possiveis: Lista de itens possíveis para dropar.
        """
        
        self.pode_dropar = pode_dropar
        self.itens_possiveis = itens_possiveis if itens_possiveis else []

    def desenhar(self, tela):
        """
        Desenha o objeto na tela.

        :param tela: Superfície onde o objeto será desenhado.
        """
        tela.blit(self.imagem, self.rect.topleft)
        # Opcional: Desenhar a hitbox para debug
        # pygame.draw.rect(tela, (255, 0, 0), self.hitbox, 1)

    def dropar_item(self):
        """
        Faz o objeto dropar um item, se possível.

        :return: Um objeto Item ou None.
        """
        if self.pode_dropar and self.itens_possiveis:
            item_escolhido = random.choice(self.itens_possiveis)
            return Item(item_escolhido, self.rect.center)
        return None