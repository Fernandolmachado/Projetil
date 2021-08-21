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

        # inicializa modulos do pygame
        pygame.init()

        # instancia de dependencias
        display = Window()
        config = Config()

        # teste
        config.scene = 2

        # execucao do jogo
        while config.running:
            if config.scene == 0:
                Presentation(display, config).run()
            elif config.scene == 1:
                MainMenu(display, config).run()
            elif config.scene == 2:
                PlayerMenu(display, config).run()
            elif config.scene == 3:
                WorldMenu(display, config).run()
            elif config.scene == 4:
                Game(display, config).run()
            else:
                raise ValueError()
