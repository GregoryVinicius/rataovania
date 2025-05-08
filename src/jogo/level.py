import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(255, 0, 0)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Level:
    def __init__(self, background):
        self.background = background
        self.enemies = []
        self.platforms = pygame.sprite.Group()
        
    def add_platform(self, x, y, width, height, color=(255, 0, 0)):
        platform = Platform(x, y, width, height, color)
        self.platforms.add(platform)

    def load(self):
        # Exemplo de plataformas adicionadas ao carregar o nível
        self.add_platform(100, 300, 200, 20)
        self.add_platform(400, 200, 150, 20)

    def update(self, screen, player):
        self.draw(screen)
        self.load()
        self.check_collision_with_platforms(player)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        self.platforms.draw(screen)

    def check_collision_with_platforms(self, player):
        collided_platforms = pygame.sprite.spritecollide(player, self.platforms, False)
        for platform in collided_platforms:
            if player.y_velocity > 0 and player.rect.bottom <= platform.rect.top + 10:
                player.rect.bottom = platform.rect.top
                player.y_velocity = 0
                player.on_ground = True