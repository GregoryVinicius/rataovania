# pylint: disable=syntax-error
#type: ignore
import pygame
from pygame.locals import QUIT
from jogo.configuracao import SCREEN_WIDTH, SCREEN_HEIGHT
from jogo.level import Level

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ratãovania")
    
    clock = pygame.time.Clock()
    # level = Level()
    
    running = True
    while running:
            if event.type == QUIT:
                running = False
        
        # level.update()
        # level.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()