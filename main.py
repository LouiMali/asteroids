import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *



def main():
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ...
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_clock = pygame.time.Clock()
    dt = 0
  
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable,)

    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        updateable.update(dt)

        # checking for collision
        for obj in asteroids:
            collision = obj.collision_check(player)
            if collision:
                print("Game over!")
                exit()

        # destroying asteroids with shots
        for obj in asteroids:
            for single in shots:
                if single.collision_check(obj):
                    obj.split()
                    single.kill()

        for obj in drawable:
            obj.draw(screen)
        
        # refreshing the screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = (my_clock.tick(60) / 1000)


if __name__ == "__main__":
    main()