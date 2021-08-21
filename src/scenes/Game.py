# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame
import random

from src.config import Config
from src.objects.Window import Window
from src.scenes.Scene import Scene


class Game(Scene):
    def __init__(self, display: Window, config: Config):
        """
        Executa do jogo.
        :param display: objeto contendo a tela e o clock
        :param config: objeto contendo as variaveis de controle
        """
        super().__init__(display, config)
        self.id_cena = 4

        # CARREGA ASSETS
        # Carrega imagem de fundo
        self.background_image = pygame.image.load("img/world.png").convert_alpha()
        self.background_image = pygame.transform.scale(
            self.background_image,
            (int(self.display.get_display().get_width()), int(self.display.get_display().get_height()))
        )

        # Trata jogadores
        self.players = self.config.players
        self.turn_order = list()
        self.handle_players()


        # variaveis de controle do mouse
        self.clicked = False
        self.click_released = False
        self.event_pos = None

        self.event = None

    def handle_events(self, event):
        # evento de clique com botao esquerdo do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.clicked = True
            self.event_pos = event.pos
        # evento de liberacao do botao esquerdo do mouse
        elif event.type == pygame.MOUSEBUTTONUP:
            self.click_released = True
            self.clicked = False
            self.event_pos = event.pos

    def update(self):
        self.button_events()

        # renderizar objetos na janela
        self.display.get_display().blit(self.background_image, (0, 0))

    def handle_players(self):
        # Determina aleatoriamente a ordem de jogadas
        temp_players_list = self.players.copy()
        for i in range(len(self.players)):
            player = random.choice(temp_players_list)
            self.turn_order.append(player)
            temp_players_list.remove(player)

        self.random_positioning_players()

    def random_positioning_players(self):
        temp_players_list = self.players.copy()
        for i in range(len(self.players)):
            player = random.choice(temp_players_list)
            self.players[self.players.index(player)].set
            temp_players_list.remove(player)

    def button_events(self):
        pass
