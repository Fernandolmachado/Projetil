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

        self.level_range = [10, 5, 1]
        self.cannon_speed = 1

    def run(self, player_me: Player, players: list, timer: Timer, config: Config):
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
                    delta_angle = player_me.get_angle() - self.angle
                    if abs(delta_angle) < self.cannon_speed:
                        player_me.set_angle(self.angle)
                    elif delta_angle < 0:
                        player_me.set_angle(player_me.get_angle() + self.cannon_speed)
                    else:
                        player_me.set_angle(player_me.get_angle() - self.cannon_speed)
                else:
                    self.planned = False
                    # Atira
                    return True
        else:
            if not self.planned:
                self.planning_movement(player_me, players)
                self.planning_aim(player_me, players, config.gravity)

        # Não atira
        return False

    def planning_movement(self, player_me: Player, players: list):
        target_position = random.choice(range(int(player_me.get_pos()[0]) - 20, int(player_me.get_pos()[0]) + 20))
        print(target_position)

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
