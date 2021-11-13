import pygame
from math import cos, sin, radians


class Bullet(object):
    def __init__(self, center: list, radius: int, angle: float, force: int, gravity: int):
        self.centerx = center[0]
        self.centery = center[1]
        self.radius = radius
        self.force = force
        self.gravity = gravity

        self.angle = int(angle)
        self.bullet_speed = [cos(radians(self.angle)) * force, sin(radians(self.angle)) * -force]
        self.bullet_color = (0, 0, 0)

    def move(self):
        self.centerx += int(self.bullet_speed[0])
        self.centery += int(self.bullet_speed[1])

        # Gravidade
        self.bullet_speed[1] += self.gravity

    def check_impact(self, obj):
        return self.get_rect().colliderect(obj)

    def blit(self, display: pygame.Surface):
        pygame.draw.circle(display, self.bullet_color, self.get_center(), self.radius)

    # Getters
    # Setters
    def get_center(self) -> list:
        return [self.centerx, self.centery]

    def get_rect(self) -> list:
        return pygame.Rect(self.centerx - self.radius, self.centery - self.radius, self.radius * 2, self.radius * 2)
