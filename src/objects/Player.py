# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021
import pygame
from math import atan, degrees


class Player(object):
    def __init__(self, id: int, artificial_intelligence=None):
        self.id = id
        self.ai = artificial_intelligence
        self.life = 100

        self.posx = 0
        self.posy = 0
        self.width = 0
        self.height = 0

        self.tank_speed = 0.3
        self.cannon_angle = 45
        self.cannon_position = list()

        self.tank_images = None
        self.tank_image_sprite = 0
        self.default_cannon_image = None
        self.cannon_image = None

        self.cannon_centerx = None
        self.cannon_centery = None

    def adjust_cannon_position(self):
        self.cannon_centerx = self.posx + self.tank_images[self.tank_image_sprite].get_width() // 2
        self.cannon_centery = self.posy + 10

        self.cannon_position = [
            self.cannon_centerx - self.cannon_image.get_width() // 2,
            self.cannon_centery - self.cannon_image.get_height() // 2
        ]

    def move(self, direction: int):
        self.posx += direction * self.tank_speed
        if self.tank_image_sprite == 0:
            self.tank_image_sprite = 1
        else:
            self.tank_image_sprite = 0

        self.adjust_cannon_position()

    def aim_cannon(self, mouse_position: tuple):
        # Cannon centerx rotation
        centerx = self.cannon_position[0] + self.cannon_image.get_width() // 2
        # Cannon centery rotation
        centery = self.cannon_position[1] + self.cannon_image.get_height() // 2

        adjacent_leg = abs(mouse_position[0] - centerx)
        opposite_leg = abs(mouse_position[1] - centery)

        if adjacent_leg != 0:
            self.cannon_angle = degrees(atan(opposite_leg / adjacent_leg))
            if mouse_position[0] < centerx:
                # Complento do ângulo + 90
                self.cannon_angle = (90 - self.cannon_angle) + 90

            # Não permite mirar diretamente para o adversário
            if self.cannon_angle < 45:
                self.cannon_angle = 45
            elif self.cannon_angle > 135:
                self.cannon_angle = 135

    def rotate_cannon(self):
        self.cannon_image = pygame.transform.rotate(self.default_cannon_image, self.cannon_angle)
        self.adjust_cannon_position()

    def blit(self, display: pygame.Surface):
        self.rotate_cannon()
        display.blit(self.cannon_image, self.cannon_position)
        display.blit(self.tank_images[self.tank_image_sprite], self.get_pos())

    def teke_damage(self, damage: int):
        self.life -= damage
        if self.life < 0:
            self.life = 0

    # Getters
    # Setters
    def get_id(self) -> int:
        return self.id

    def get_life(self) -> int:
        return self.life

    def get_pos(self) -> list:
        return [self.posx, self.posy]

    def get_rect(self) -> pygame.Rect:
        print("posx", self.posx)
        print("posy", self.posy)
        print("largura", self.width)
        print("altura", self.height)
        return pygame.Rect(self.posx, self.posy, self.width, self.height)

    def get_cennon_center(self) -> list:
        return [self.cannon_centerx, self.cannon_centery]

    def get_angle(self) -> float:
        return self.cannon_angle

    def set_player_images(self, tank_images: list, posx: int, posy: int):
        self.tank_images = tank_images[:2]
        self.default_cannon_image = tank_images[2]
        self.cannon_image = self.default_cannon_image

        self.posx = posx
        self.posy = posy
        self.width = self.tank_images[self.tank_image_sprite].get_width()
        self.height = self.tank_images[self.tank_image_sprite].get_height()
        print(self.height)

        self.adjust_cannon_position()
