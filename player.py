"""Contains logic for the player in the game"""
# pylint: disable=no-member
import pygame
from circleshape import CircleShape

from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHOT_RADIUS,
)
from shot import Shot


class Player(CircleShape):
    """Contains logic for the player class which inherits from the Circle Shape base class"""

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.containers = None
        self.cooldown_timer = 0

    # in the player class
    def triangle(self):
        """Creates the player's triangle on the screen"""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "WHITE", self.triangle(), 2)

    def rotate(self, dt):
        """Rotates the player

        Args:
            dt (integer): delta value
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """Moves the player

        Args:
            dt (integer): delta value
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.cooldown_timer -= dt

    def shoot(self):
        """Shoots bullets from the player"""
        if self.cooldown_timer > 0:
            return
        else:
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            )
