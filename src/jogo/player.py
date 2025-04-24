# pylint: disable=import-error
import pygame

from jogo.character import Character


class Player(Character):
    def __init__(self, x, y, width, height, color=(0, 0, 255)):
        super().__init__("Player 1", 100, 10, 10, 10, 0.5, 0, False)
        # Define a posição e o tamanho do jogador
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color  # Cor do jogador

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.velocity
            
    def update(self):
        self.apply_gravity()  # Aplica a gravidade ao jogador
        self.move()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
