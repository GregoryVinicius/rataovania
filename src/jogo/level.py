# pylint: disable=import-error
import pygame


class Platform:
    def __init__(self, x, y, width, height, color=(255, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Level:
    def __init__(self, background):
        self.background = background
        self.enemies = []
        self.platforms = []  # Lista para armazenar as plataformas

    def add_platform(self, x, y, width, height, color=(255, 0, 0)):
        platform = Platform(x, y, width, height, color)
        self.platforms.append(platform)

    def load(self):
        # Exemplo de plataformas adicionadas ao carregar o nível
        self.add_platform(100, 300, 200, 20)  # Plataforma 1
        self.add_platform(400, 200, 150, 20)  # Plataforma 2

    def update(self, screen,  player):
        self.draw(screen)
        self.load()
        self.check_collision_with_platforms(player)

    def draw(self, screen):
        # Desenha o fundo
        screen.blit(self.background, (0, 0))  # Corrigido para usar blit com a imagem de fundo

        # Desenha as plataformas
        for platform in self.platforms:
            platform.draw(screen)
            
    def check_collision_with_platforms(self, player):
        player.on_ground = False  # Assume que o jogador não está no chão
        for platform in self.platforms:
            if player.rect.colliderect(platform.rect):
                # Ajusta o jogador para ficar em cima da plataforma
                if player.y_velocity > 0:  # Apenas se estiver caindo
                    player.rect.bottom = platform.rect.top
                    player.on_ground = True
