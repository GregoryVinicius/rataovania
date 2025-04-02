import pygame

class ElementoGrafico:
    def __init__(self, imagem_path, posicao, escala=None):
        """
        Inicializa um elemento gráfico.

        :param imagem_path: Caminho para a imagem do elemento.
        :param posicao: Tupla (x, y) representando a posição inicial.
        :param escala: Tupla (largura, altura) para redimensionar a imagem (opcional).
        """
        self.imagem = pygame.image.load(imagem_path).convert_alpha()
        if escala:
            self.imagem = pygame.transform.scale(self.imagem, escala)
        self.rect = self.imagem.get_rect(topleft=posicao)

    def desenhar(self, tela):
        """
        Desenha o elemento gráfico na tela.

        :param tela: Superfície do Pygame onde o elemento será desenhado.
        """
        tela.blit(self.imagem, self.rect.topleft)

    def mover(self, dx, dy):
        """
        Move o elemento gráfico.

        :param dx: Deslocamento no eixo X.
        :param dy: Deslocamento no eixo Y.
        """
        self.rect.x += dx
        self.rect.y += dy

    def colidiu_com(self, outro_elemento):
        """
        Verifica se este elemento colidiu com outro elemento gráfico.

        :param outro_elemento: Outro objeto da classe ElementoGrafico.
        :return: True se houver colisão, False caso contrário.
        """
        return self.rect.colliderect(outro_elemento.rect)