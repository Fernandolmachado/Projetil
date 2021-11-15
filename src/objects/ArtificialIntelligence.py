# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     07/04/2021
import random
from math import asin, degrees

from src.config import Config
from src.objects.Timer import Timer
from src.objects.Player import Player


class ArtificialIntelligence(object):
    def __init__(self, level: int):
        self.level = level
        self.planned = False
        self.angle = None
        self.position = None
        self.aiming = False

        self.level_range = [10, 5, 1]
        self.cannon_speed = 1

        self.over_prepare = False
        self.prepare_time = 0

    def run(self, player_me: Player, players: list, timer: Timer, config: Config):
        fire = False

        if timer.get_seconds() < 11:

            if int(player_me.get_pos()[0]) != self.position:
                delta_position = player_me.get_pos()[0] - self.position
                if delta_position < 0:
                    player_me.move(config.RIGHT, players)
                else:
                    player_me.move(config.LEFT, players)
            else:
                # Ajusta mira
                if player_me.get_angle() != self.angle:
                    self.aiming = True
                    delta_angle = player_me.get_angle() - self.angle
                    if abs(delta_angle) < self.cannon_speed:
                        player_me.set_angle(self.angle)
                    elif delta_angle < 0:
                        player_me.set_angle(player_me.get_angle() + self.cannon_speed)
                    else:
                        player_me.set_angle(player_me.get_angle() - self.cannon_speed)

                    delta_angle = player_me.get_angle() - self.angle
                    if delta_angle == 0:
                        self.over_prepare = True
                else:
                    if self.over_prepare:
                        self.prepare_time = timer.get_seconds()
                        self.over_prepare = False

                    if self.prepare_time - timer.get_seconds() > 1:
                        self.planned = False
                        # Atira
                        fire = True
        else:
            if not self.planned:
                self.planning_movement(player_me, players)
                self.planning_aim(player_me, players, config.gravity)

        # Não atira
        return fire

    def planning_movement(self, player_me: Player, players: list):
        target_position = random.choice(range(int(player_me.get_pos()[0]) - 20, int(player_me.get_pos()[0]) + 20))

        if target_position < 0:
            target_position == 0
        elif target_position + player_me.get_rect().width > 800:
            # TODO: Insirir as dimensões da janela na classe de configuração
            target_position = 800 - player_me.get_rect().width

        self.position = target_position

    def planning_aim(self, player_me: Player, players: list, gravity: int):
        # Escolhe alvo
        target_player = random.choice(players)

        # Distancia entre o jogador e o oponente
        distance = target_player.get_pos()[0] - self.position

        # Encontra o ângulo de disparo
        target_angle = 90 - (int(degrees(asin(abs(distance) * gravity / player_me.get_force() ** 2) / 2)))

        if target_angle < 45:
            target_angle = 45

        if distance < 0:
            target_angle = 180 - target_angle

        # Define intervalo de angulos e escolhe um
        range_interval = self.level_range[self.level - 1]
        self.angle = random.choice(range(target_angle - range_interval, target_angle + range_interval))

        self.planned = True

    def is_aiming(self) -> bool:
        return self.aiming

    def set_aiming(self, aiming: bool):
        self.aiming = aiming
