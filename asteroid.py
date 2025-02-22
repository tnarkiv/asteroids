"""Contains the logic for asteroids"""

import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    """The Asteroid Class"""

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.containers = None

    def draw(self, screen):
        pygame.draw.circle(screen, "RED", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        """Splits the asteroid"""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_velocity_1 = self.velocity.rotate(angle) * 1.2
            new_velocity_2 = self.velocity.rotate(-angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_velocity_1
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = new_velocity_2
