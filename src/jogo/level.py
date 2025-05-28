import pygame
import os


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, sprite_path=None):
        super().__init__()
        if sprite_path:
            self.image = pygame.image.load(sprite_path)
            self.image = pygame.transform.scale(
                self.image, (width, height))  
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill((255, 0, 0)) 
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Level:
    def __init__(self, background):
        self.background = background
        self.enemies = []
        self.platforms = pygame.sprite.Group()
        self.load()

    def add_platform(self, x, y, width, height, sprite_path=None):
        platform = Platform(x, y, width, height, sprite_path)
        self.platforms.add(platform)

    def load(self):
        self.add_platform(100, 300, 200, 50, "../resource/platform1.png")
        self.add_platform(400, 200, 200, 50, "../resource/platform1.png")

    def update(self, screen, player):
        self.draw(screen)
        self.check_collision_with_platforms(player)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.platforms.draw(screen)

    def check_collision_with_platforms(self, player):
        player.on_ground = False
        collided_platforms = pygame.sprite.spritecollide(
            player, self.platforms, False)
        for platform in collided_platforms:
            if player.y_velocity > 0 and player.rect.bottom <= platform.rect.top + 10:
                player.rect.bottom = platform.rect.top
                player.y_velocity = 0
                player.on_ground = True
