# pylint: disable=import-error
import pygame

from pygame.locals import QUIT
from jogo.config import SCREEN_WIDTH, SCREEN_HEIGHT
from jogo.level import Level
from jogo.player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ratãovania")

    # Carregar a imagem de fundo
    background = pygame.image.load("../resource/background.png").convert()
    clock = pygame.time.Clock()

    # Instanciar o nível e carregar as plataformas
    level = Level(background)
    level.load()

    # Instanciar o jogador
    player = Player(100, 50, 50, 50)  # Posição inicial e tamanho do jogador

    running = True
    while running:
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
 
        # Atualizar o nível e o jogador
        level.update(screen, player)
        player.update()

        # Desenhar o nível e o jogador
        level.draw(screen)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
