# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021
import pygame
from math import atan, degrees


class Player(object):
    def __init__(self, id: int, artificial_intelligence=None):
        self.id = id
        self.ai = artificial_intelligence

        self.posx = 0
        self.posy = 0
        self.width = 0
        self.height = 0

        self.tank_speed = 1
        self.cannon_angle = 45
        self.cannon_position = list()

        self.tank_image = None
        self.cannon_image = None

    def get_id(self) -> int:
        return self.id

    def get_posx(self) -> int:
        return self.posx

    def set_posx(self, value: int):
        self.posx = value

    def get_posy(self) -> int:
        return self.posy

    def set_posy(self, value: int):
        self.posy = value

    def get_posy(self) -> int:
        return self.posy

    def set_posy(self, value: int):
        self.posy = value

    def get_rect(self) -> list:
        return pygame.Rect(self.posx, self.posy, self.width, self.height)

    def set_player_image(self, tank_image: pygame.Surface, cannon_image: pygame.Surface):
        self.tank_image = tank_image
        self.cannon_image = cannon_image

        # TODO: Atribuir tamanho e posição do canhão
        self.width = 0
        self.height = 0
        self.cannon_position = list()

    def move_tank(self, direction: int):
        self.posx += direction * self.tank_speed
        self.cannon_position[0] += direction * self.tank_speed

    def aim_cannon(self, mouse_position: tuple):
        adjacent_leg = mouse_position[0] - self.cannon_position[0]
        opposite_leg = abs(self.cannon_position[1] - mouse_position[1])

        self.cannon_angle = degrees(atan(opposite_leg / adjacent_leg))

        if 0 <= self.cannon_angle < 45:
            self.cannon_angle = 45
        elif -45 < self.cannon_angle < 0:
            self.cannon_angle = -45

    def blit(self):
