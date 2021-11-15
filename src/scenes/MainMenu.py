# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame

from src.config import Config
from src.objects.Sound import Sound
from src.objects.Window import Window
from src.scenes.Scene import Scene
from src.objects.PositionalSurface import PositionalSurface
from src.objects.Text import Text


class MainMenu(Scene):
    def __init__(self, display: Window, config: Config):
        """
        Executa menu principal do jogo.
        :param display: objeto contendo a tela
        :param config: objeto contendo as variaveis de controle
        """
        super().__init__(display, config)
        self.id_cena = 1

        # Carrega imagem de fundo
        self.background_image = pygame.image.load("img/menu_background.png").convert_alpha()
        self.background_image = pygame.transform.scale(
            self.background_image,
            (int(self.display.get_display().get_width() * 1.25), int(self.display.get_display().get_height() * 1.25))
        )

        # caixa do menu
        self.menu_box = PositionalSurface(50, 50, pygame.Color(150, 180, 190, 40), (150, 150))

        # botao jogar
        self.play_button = Text(self.menu_box, "Jogar", "Comic Sans MS", 30, pygame.Color(0, 0, 0), (0, 30), True)
        self.play_button.center_x()

        # botao sair
        self.exit_button = Text(self.menu_box, "Sair", "Comic Sans MS", 30, pygame.Color(0, 0, 0), (0, 80), True)
        self.exit_button.center_x()

        # variaveis de controle do mouse
        self.clicked = False
        self.event_pos = None

        self.event = None

        # sons
        config.menu_music = Sound(config.sounds["menu_music"])

        self.play_button.set_hover_sound(Sound(config.sounds["cursor"]))
        self.play_button.set_click_sound(Sound(config.sounds["select"]))
        self.exit_button.set_hover_sound(Sound(config.sounds["cursor"]))
        self.exit_button.set_click_sound(Sound(config.sounds["select"]))

        config.menu_music.play(-1)
        config.menu_music.set_volume(0.7)

    def handle_events(self, event):
        # evento de clique com botao esquerdo do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.clicked = True
            self.event_pos = event.pos

    def update(self):
        self.button_events()

        # buffer da caixa de menu
        self.menu_box.fill_with_border(5)

        self.play_button.blit()
        self.exit_button.blit()

        # renderizar objetos na janela
        self.display.get_display().blit(self.background_image, (0, 0))
        self.display.get_display().blit(self.menu_box, self.menu_box.get_position())

    def on_close(self):
        if self.event == "play":
            self.config.scene = self.id_cena + 1
        elif self.event == "exit":
            self.config.running = False

    def button_events(self):
        """
        Trata a interacao do usuario por meio dos eventos do mouse
        :return: None
        """
        # eventos com o mouse
        # botao Jogar
        if self.play_button.get_rect(self.menu_box.get_position()).collidepoint(pygame.mouse.get_pos()):
            if self.clicked:
                self.play_button.on_click()
                self.event = "play"
                self.close()
            else:
                # efeito de mouse hover
                self.play_button.on_hover()
        else:
            self.play_button.on_normal()

        # botao Sair
        if self.exit_button.get_rect(self.menu_box.get_position()).collidepoint(pygame.mouse.get_pos()):
            if self.clicked:
                self.exit_button.on_click()
                self.event = "exit"
                self.close()
            else:
                self.exit_button.on_hover()
        else:
            self.exit_button.on_normal()

        self.clicked = False
