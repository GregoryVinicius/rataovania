import pygame

from jogo.character import Character


class Player(Character):
    def __init__(self, x, y, width, height):
        super().__init__("../resource/personagem.png", "Player 1", 100, 10, 10, 10, 0.5, 0, False)
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load("../resource/personagem.png")
        self.image = pygame.transform.scale(
            self.image, (width, height))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.velocity

    def update(self):
        self.move()
        self.apply_gravity()

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Desenha a sprite na tela
