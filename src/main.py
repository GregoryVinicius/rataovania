# pylint: disable=import-error
import pygame

from pygame.locals import QUIT
from jogo.config import SCREEN_WIDTH, SCREEN_HEIGHT
from jogo.level import Level
from jogo.player import Player

#fazer uma game maneger
#fazer uma game world
def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Ratãovania")

    background = pygame.image.load("../resource/background.png").convert()
    clock = pygame.time.Clock()
    
    level = Level(background)
    level.load()

    player = Player(100, 50, 50, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
 
        level.update(screen, player)
        player.update()

        level.draw(screen)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
