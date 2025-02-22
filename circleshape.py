"""Contains logic for the Circle shape base class"""

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """Class definition for Circle shape"""

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Draws the object

        Args:
            screen (pygame.display): Screen on which the object will be drawn
        """
        # sub-classes must override

    def update(self, dt):
        """Updates the object after each game loop

        Args:
            dt (integer): delta value
        """
        # sub-classes must override

    def is_colliding(self, circle_shape):
        """Checks for collisions between shapes

        Args:
            circle_shape (CircleShape): other circle shape object which is being checked for
            collision

        Returns:
            boolean: denotes whether objects are colliding
        """
        distance = self.position.distance_to(circle_shape.position)
        if distance <= (self.radius + circle_shape.radius):
            return True
        else:
            return False
