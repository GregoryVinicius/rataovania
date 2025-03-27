import pygame

class Camera:
    def __init__(self, width, height):
        """
        Inicializa a câmera.
        :param width: Largura do mapa.
        :param height: Altura do mapa.
        """
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        """
        Aplica o deslocamento da câmera a uma entidade.
        :param entity: Entidade a ser ajustada.
        :return: Retorna a posição ajustada da entidade.
        """
        return entity.rect.move(self.camera.topleft)

    def update(self, target, screen_width, screen_height):
        """
        Atualiza a posição da câmera com base na posição do alvo.
        :param target: O alvo (personagem) que a câmera deve seguir.
        :param screen_width: Largura da tela.
        :param screen_height: Altura da tela.
        """
        x = -target.rect.centerx + screen_width // 2
        y = -target.rect.centery + screen_height // 2

        # Limita a câmera aos limites do mapa
        x = min(0, x)  # Não ultrapassa o lado esquerdo
        x = max(-(self.width - screen_width), x)  # Não ultrapassa o lado direito
        y = min(0, y)  # Não ultrapassa o topo
        y = max(-(self.height - screen_height), y)  # Não ultrapassa a parte inferior

        self.camera = pygame.Rect(x, y, self.width, self.height)