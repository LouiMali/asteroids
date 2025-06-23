import pygame
from constants import *
from player import *
from circleshape import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_clock = pygame.time.Clock()
    dt = 0
    
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        player.update(dt)

        # refreshing the screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = (my_clock.tick(60) / 1000)


if __name__ == "__main__":
    main()