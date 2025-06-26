import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_clock = pygame.time.Clock()
    dt = 0
  
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    
    AsteroidField.containers = (updateable,)
    asteroid_field = AsteroidField()
    

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        updateable.update(dt)

        for obj in asteroids:
            collision = obj.collision_check(player)
            if collision:
                print("Game over!")
                exit()

        for obj in drawable:
            obj.draw(screen)
        
        # refreshing the screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = (my_clock.tick(60) / 1000)


if __name__ == "__main__":
    main()