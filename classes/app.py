# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame

from classes.janela import Janela
from classes.config import Config
from classes.apresentacao import Apresentacao
from classes.menu_principal import MenuPrincipal
from classes.menu_mundo import MenuMundo
from classes.menu_jogador import MenuJogador
from classes.jogo import Jogo


class App(object):

    test = True

    @staticmethod
    def executar():
        """
        Executa o jogo Projetil

        :return: None
        """

        # inicializa modulos do pygame
        pygame.init()

        # instancia de dependencias
        display = Janela()
        config = Config()

        # teste
        config.cena = 0

        # execucao do jogo
        while config.running:
            if config.cena == 0:
                Apresentacao(display, config).run()
            elif config.cena == 1:
                MenuPrincipal(display, config).run()
            elif config.cena == 2:
                MenuMundo(display, config).run()
            elif config.cena == 3:
                MenuJogador(display, config).run()
            elif config.cena == 4:
                Jogo(display, config).run()
            else:
                raise ValueError()
