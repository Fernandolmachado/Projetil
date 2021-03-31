# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame

from classes.janela import Janela
from classes.config import Config
from classes.cena import Cena


class Jogo(Cena):
    def __init__(self, display: Janela, config: Config):
        """
        Executa do jogo.
        :param display: objeto contendo a tela e o clock
        :param config: objeto contendo as variaveis de controle
        """
        super().__init__(display, config)
        self.id_cena = 4

    def handle_events(self, event):
        # evento de clique com botao esquerdo do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.clicked = True
            self.event_pos = event.pos
        # evento de liberacao do botao esquerdo do mouse
        elif event.type == pygame.MOUSEBUTTONUP:
            self.unclicked = True
            self.clicked = False
            self.event_pos = event.pos

    def update(self):
        pass
