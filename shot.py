"""Contains the logic for the shot/bullet"""

import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    """Defines the class for the shot"""

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.containers = None

    def draw(self, screen):
        pygame.draw.circle(screen, "GREEN", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
