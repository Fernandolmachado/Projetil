# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     10/03/2021

import pygame

from src.scenes.Scene import Scene
from src.objects.Window import Window
from src.config import Config
from src.utils.Text import Text
from src.utils.Button import Button
from src.objects.Player import Player
from src.objects.ArtificialIntelligence import ArtificialIntelligence


class PlayerMenu(Scene):
    def __init__(self, display: Window, config: Config):
        """
        Executa menu de escolha do mundo.
        :param display: objeto contendo a tela e o clock
        :param config: objeto contendo as variaveis de controle
        """
        super().__init__(display, config)
        self.id_cena = 2

        # Carrega imagem de fundo
        self.background_image = pygame.image.load("img/menu_background.png").convert_alpha()
        self.background_image = pygame.transform.scale(
            self.background_image,
            (int(self.display.get_display().get_width() * 1.25), int(self.display.get_display().get_height() * 1.25))
        )

        # Comunicacao
        self.message = Text(self.display.get_display(), "Escolha os jogadores", "Comic Sans MS", 50,
                            pygame.Color(0, 0, 0), (150, 70))

        # Cria seletores de personagens

        # Lista de cores de cada personagem
        self.characters_color_list = [
            pygame.Color(255, 0, 0),
            pygame.Color(0, 255, 0),
            pygame.Color(0, 0, 255),
            pygame.Color(255, 255, 0)
        ]

        # Lista de botões de escolha de tipo do jogador (jogável ou CPU)
        self.players_buttons = [
            Button(self.display.get_display(), (100, 320), "Jogador", 30, pygame.Color(0, 0, 0)),
            Button(self.display.get_display(), (300, 320), "CPU", 30, pygame.Color(0, 0, 0)),
            Button(self.display.get_display(), (500, 320), "CPU", 30, pygame.Color(0, 0, 0)),
            Button(self.display.get_display(), (700, 320), "CPU", 30, pygame.Color(0, 0, 0))
        ]

        # Lista de botões de nível de dificuldade (1, 2 ou 3)
        self.player_level_buttons = [
            Button(self.display.get_display(), (100, 400), "1", 30, pygame.Color(0, 0, 0)),
            Button(self.display.get_display(), (300, 400), "1", 30, pygame.Color(0, 0, 0)),
            Button(self.display.get_display(), (500, 400), "1", 30, pygame.Color(0, 0, 0)),
            Button(self.display.get_display(), (700, 400), "1", 30, pygame.Color(0, 0, 0))
        ]


        # Botão Voltar
        self.back_button = Text(self.display.get_display(), "Voltar", "Comic Sans MS", 40,
                                pygame.Color(0, 0, 0), (50, 500), True)

        # Botão Jogar
        self.play_button = Text(self.display.get_display(), "Jogar", "Comic Sans MS", 40,
                                pygame.Color(0, 0, 0), (650, 500), True)

        # variaveis de controle do mouse
        self.clicked = False
        self.event_pos = None

        self.event = None

    def handle_events(self, event):
        # evento de clique com botao esquerdo do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.clicked = True
            self.event_pos = event.pos

    def update(self):
        self.button_events()

        # renderizar objetos na janela
        self.display.get_display().blit(self.background_image, (0, 0))

        self.message.blit()

        # Desenha os circulos representando a cor do personagem
        for i in range(len(self.characters_color_list)):
            pygame.draw.circle(
                self.display.get_display(),
                self.characters_color_list[i],
                [200 * i + 100, 250],
                50
            )

            self.players_buttons[i].blit()
            if self.players_buttons[i].get_text() == "CPU":
                self.player_level_buttons[i].blit()

        # Botões
        self.back_button.blit()
        self.play_button.blit()

    def on_close(self):
        if self.event == "play":
            print("aqui")
            for i in range(len(self.players_buttons)):
                if self.players_buttons[i].get_text() == "CPU":
                    self.config.players.append(
                        Player(i, ArtificialIntelligence(int(self.player_level_buttons[i].get_text()))))
                else:
                    self.config.players.append(Player(i))

            self.config.scene = self.id_cena + 1
        elif self.event == "back":
            self.config.scene = self.id_cena - 1

    def button_events(self):
        """
        Trata a interacao do usuario por meio dos eventos do mouse
        :return: None
        """
        # botao voltar
        if self.back_button.get_rect().collidepoint(pygame.mouse.get_pos()):
            if self.clicked:
                self.back_button.on_click()
                self.event = "back"
                self.close()
            else:
                self.back_button.on_hover()
        else:
            self.back_button.on_normal()

        # botao de play
        if self.play_button.get_rect().collidepoint(pygame.mouse.get_pos()):
            if self.clicked:
                self.play_button.on_click()
                self.event = "play"
                self.close()
            else:
                self.play_button.on_hover()
        else:
            self.play_button.on_normal()

        for i in range(len(self.players_buttons)):

            player_button = self.players_buttons[i]
            player_level_button = self.player_level_buttons[i]

            if player_button.get_rect().collidepoint(pygame.mouse.get_pos()):
                if self.clicked:
                    player_button.on_click()
                    player_button.set_text("Jogador" if player_button.get_text() == "CPU" else "CPU")
                else:
                    player_button.on_hover()
            else:
                player_button.on_normal()

            if player_button.get_text() == "CPU" and player_level_button.get_rect().collidepoint(pygame.mouse.get_pos()):
                if self.clicked:
                    player_level_button.on_click()
                    if player_level_button.get_text() == "1":
                        player_level_button.set_text("2")
                    elif player_level_button.get_text() == "2":
                        player_level_button.set_text("3")
                    else:
                        player_level_button.set_text("1")
                else:
                    player_level_button.on_hover()
            else:
                player_level_button.on_normal()

        self.clicked = False
