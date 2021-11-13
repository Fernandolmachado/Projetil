# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021
import pygame
from math import atan, degrees

from src.config import Config
from src.objects.Timer import Timer


class Player(object):
    def __init__(self, id: int, artificial_intelligence=None):
        self.id = id
        self.ai = artificial_intelligence

        self.posx = 0
        self.posy = 0
        self.width = 0
        self.height = 0

        self.tank_speed = 0.3
        self.cannon_angle = 45
        self.force = 30
        self.cannon_position = list()

        self.tank_images = None
        self.tank_image_sprite = 0
        self.default_cannon_image = None
        self.cannon_image = None

        self.cannon_centerx = None
        self.cannon_centery = None

        self.life = 100
        self.dead = False
        self.damage = False

        self.start_turn = False

        self.counter = 0

        self.display_width = 800

    def adjust_cannon_position(self):
        self.cannon_centerx = self.posx + self.tank_images[self.tank_image_sprite].get_width() // 2
        self.cannon_centery = self.posy + 10

        self.cannon_position = [
            self.cannon_centerx - self.cannon_image.get_width() // 2,
            self.cannon_centery - self.cannon_image.get_height() // 2
        ]

    def move(self, direction: int, players: list):
        self.posx += direction * self.tank_speed

        # Colisão nas bordas da janela
        if self.posx < 0:
            self.posx = 0
        elif self.display_width is not None and (self.posx + self.width) > self.display_width:
            self.posx = self.display_width - self.width

        # Colisão com players
        for player in players:
            if self.get_rect().colliderect(player.get_rect()):
                if self.posx < player.get_pos()[0]:
                    self.posx = player.get_pos()[0] - self.width
                else:
                    self.posx = player.get_pos()[0] + player.get_rect().width

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
        self.display_width = display.get_width()

        self.rotate_cannon()
        if self.damage:
            self.damage_animation(display)
        else:
            self.draw(display)

    def draw(self, display):
        display.blit(self.cannon_image, self.cannon_position)
        display.blit(self.tank_images[self.tank_image_sprite], self.get_pos())
        self.life_bar_draw(display)

    def damage_animation(self, display):
        # Animação de dano
        if (self.counter // 5) % 2 == 1:
            self.draw(display)

        self.counter += 1

        if self.counter > 100:
            self.counter = 0
            self.damage = False

    def life_bar_draw(self, display):
        # desenha barra de vida
        bar_width = 100
        bar_height = 20
        bar_posx = self.posx + self.tank_images[self.tank_image_sprite].get_width() // 2 - bar_width // 2
        bar_posy = self.posy + self.height + 5
        # Barra branca
        pygame.draw.rect(display, (200, 230, 200, 200), [bar_posx, bar_posy, bar_width, bar_height], border_radius=2)

        if self.life > 50:
            # Borda
            pygame.draw.rect(display, (10, 180, 20, 200), [bar_posx - 2, bar_posy - 2, bar_width + 4, bar_height + 4],
                             2, 2)
            # Barra de vida
            pygame.draw.rect(display, (10, 230, 20, 200), [bar_posx, bar_posy, self.life, bar_height], border_radius=2)
        else:
            # Borda
            pygame.draw.rect(display, (180, 10, 20, 200), [bar_posx - 2, bar_posy - 2, bar_width + 4, bar_height + 4],
                             2, 2)
            # Barra de vida
            pygame.draw.rect(display, (230, 10, 20, 200), [bar_posx, bar_posy, self.life, bar_height], border_radius=2)

    def take_damage(self, damage: int):
        self.life -= damage
        self.damage = True
        if self.life < 0:
            self.life = 0

    def ai_moving(self, players: list, timer: Timer, config: Config):
        return self.ai.run(self, players, timer, config)

    # Getters
    # Setters
    def get_id(self) -> int:
        return self.id

    def is_ai(self):
        return self.ai is not None

    def has_life(self) -> bool:
        return self.life > 0

    def set_dead(self):
        self.dead = True

    def is_dead(self) -> bool:
        return self.dead

    def get_pos(self) -> list:
        return [self.posx, self.posy]

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.posx, self.posy, self.width, self.height)

    def get_cennon_center(self) -> list:
        return [self.cannon_centerx, self.cannon_centery]

    def get_angle(self) -> float:
        return self.cannon_angle

    def set_angle(self, angle: int):
        self.cannon_angle = angle

    def get_force(self) -> int:
        return self.force

    def set_player_images(self, tank_images: list, posx: int, posy: int):
        self.tank_images = tank_images[:2]
        self.default_cannon_image = tank_images[2]
        self.cannon_image = self.default_cannon_image

        self.posx = posx
        self.posy = posy
        self.width = self.tank_images[self.tank_image_sprite].get_width()
        self.height = self.tank_images[self.tank_image_sprite].get_height()

        self.adjust_cannon_position()

    def is_damage_animation(self):
        return self.damage
