import pygame
from jogo.Platform import Platform

class Level:
    def __init__(self, background):
        self.background = background
        self.enemies = []
        self.load()

    def load(self):
        Platform.add_platform(100, 300, 200, 50, "../resource/platform1.png")
        Platform.add_platform(400, 200, 200, 50, "../resource/platform1.png")

    def update(self, screen, player):
        self.draw(screen)
        self.check_collision_with_platforms(player)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        Platform.draw(screen)
        
#Arrumar bug de atravessar a plataforma
    def check_collision_with_platforms(self, player):
        player.on_ground = False
        collided_platforms = pygame.sprite.spritecollide(
            player, self.platforms, False)
        for platform in collided_platforms:
            if player.y_velocity > 0 and player.rect.bottom <= platform.rect.top + 10:
                player.rect.bottom = platform.rect.top
                player.y_velocity = 0
                player.on_ground = True
