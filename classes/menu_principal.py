# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame

from classes.cena import Cena
from classes.janela import Janela
from classes.config import Config
from classes.texto import Texto
from classes.minha_surface import MinhaSurface


class MenuPrincipal(Cena):
    def __init__(self, display: Janela, config: Config):
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
        self.menu_box = MinhaSurface(50, 50, pygame.Color(150, 180, 190, 40), (150, 150))

        # botao jogar
        self.play_button = Texto(self.menu_box, "Jogar", "Comic Sans MS", 30, pygame.Color(0, 0, 0), (0, 30), True)
        self.play_button.center_x()

        # botao sair
        self.exit_button = Texto(self.menu_box, "Sair", "Comic Sans MS", 30, pygame.Color(0, 0, 0), (0, 80), True)
        self.exit_button.center_x()

        # variaveis de controle do mouse
        self.clicked = False
        self.unclicked = False
        self.event_pos = None

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
        self.logic_events()

        # buffer da caixa de menu
        self.menu_box.fill_with_border(5)

        self.play_button.blit()
        self.exit_button.blit()

        # renderizar objetos na janela
        self.display.get_display().blit(self.background_image, (0, 0))
        self.display.get_display().blit(self.menu_box, self.menu_box.get_position())

    def logic_events(self):
        """
        Trata a interacao do usuario por meio dos eventos do mouse
        :return: None
        """
        # eventos com o mouse
        # botao Jogar
        if self.play_button.get_rect(self.menu_box.get_position()).collidepoint(pygame.mouse.get_pos()):
            if self.unclicked:
                self.play_button.on_normal()
                self.clicked = False
                self.unclicked = False

                self.config.cena = self.id_cena + 1
                self.close()
            elif self.clicked:
                # efeito de clicar
                self.play_button.on_click()
            else:
                # efeito de mouse hover
                self.play_button.on_hover()
        else:
            self.play_button.on_normal()

        # botao Sair
        if self.exit_button.get_rect(self.menu_box.get_position()).collidepoint(pygame.mouse.get_pos()):
            if self.unclicked:
                self.play_button.on_normal()
                self.clicked = False
                self.unclicked = False

                self.config.running = False
                self.close()
            elif self.clicked:
                self.exit_button.on_click()
            else:
                self.exit_button.on_hover()
        else:
            self.exit_button.on_normal()

        self.unclicked = False
