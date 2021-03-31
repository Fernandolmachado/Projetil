# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     10/03/2021

import pygame

from src.scenes.Scene import Scene
from src.objects.Window import Window
from src.config import Config
from src.utils.Text import Text


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
                            pygame.Color(0, 0, 0), (150, 100))

        # Botão Voltar
        self.back_button = Text(self.display.get_display(), "Voltar", "Comic Sans MS", 40,
                                pygame.Color(0, 0, 0), (50, 500), True)

        # Botão Jogar
        self.play_button = Text(self.display.get_display(), "Jogar", "Comic Sans MS", 40,
                                pygame.Color(0, 0, 0), (650, 500), True)

        # Imagens dos jogadores


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
        self.back_button.blit()
        self.play_button.blit()

    def on_close(self):
        if self.event == "play":
            # TODO: populate self.config.players
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

        self.clicked = False
