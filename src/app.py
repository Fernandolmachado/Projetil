# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame

from src.config import Config
from src.objects.Window import Window
from src.scenes.Presentation import Presentation
from src.scenes.MainMenu import MainMenu
from src.scenes.PlayerMenu import PlayerMenu
from src.scenes.WorldMenu import WorldMenu
from src.scenes.Game import Game


class App(object):
    test = True

    @staticmethod
    def run():
        """
        Executa o jogo Projetil

        :return: None
        """
        # Used to prevent high latency of buffer
        # (frequency, size, channel, buffer)
        # channel argument: 1 mono, 2 stereo
        # buffer: must be a power of 2
        pygame.mixer.pre_init(22100, -16, 2, 64)

        # inicializa modulos do pygame
        pygame.init()

        # instancia de dependencias
        display = Window()
        config = Config()

        # teste
        config.scene = 0

        # execucao do jogo
        while config.running:
            if config.scene == 0:
                scene = Presentation(display, config)
            elif config.scene == 1:
                scene = MainMenu(display, config)
            elif config.scene == 2:
                scene = PlayerMenu(display, config)
            elif config.scene == 3:
                scene = WorldMenu(display, config)
            elif config.scene == 4:
                scene = Game(display, config)
            else:
                raise ValueError()

            scene.run()
