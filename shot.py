import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white", 
            (int(self.position.x),(int(self.position.y))), 
            self.radius, 
            width = 1
        )

    def update(self, dt):
        self.position += (self.velocity * dt)
        