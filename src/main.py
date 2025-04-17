# pylint: disable=syntax-error
import pygame
from pygame.locals import QUIT
from jogo.config import SCREEN_WIDTH, SCREEN_HEIGHT
from jogo.level import Level


def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ratãovania")

    # Carregar a imagem de fundo
    background = pygame.image.load("../resource/imagem-teste.jpg").convert()
    clock = pygame.time.Clock()
    # level = Level()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
