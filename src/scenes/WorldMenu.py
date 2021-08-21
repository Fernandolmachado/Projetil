# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     10/03/2021

import pygame

from src.config import Config
from src.objects.Window import Window
from src.scenes.Scene import Scene
from src.objects.Image import Image
from src.objects.Text import Text


class WorldMenu(Scene):
    def __init__(self, display: Window, config: Config):
        """
        Executa menu de escolha do mundo.
        :param display: objeto contendo a tela e o clock
        :param config: objeto contendo as variaveis de controle
        """
        super().__init__(display, config)
        self.id_cena = 3

        # Carrega imagem de fundo
        self.background_image = pygame.image.load("img/menu_background.png").convert_alpha()
        self.background_image = pygame.transform.scale(
            self.background_image,
            (int(self.display.get_display().get_width() * 1.25), int(self.display.get_display().get_height() * 1.25))
        )

        # Comunicacao
        self.message = Text(self.display.get_display(), "Escolha um mundo", "Comic Sans MS", 50,
                            pygame.Color(0, 0, 0), (200, 100))

        # Opcoes de mundo
        self.worlds_available = 4
        self.worlds_box = list()

        for i in range(self.worlds_available):
            self.worlds_box.append(Image(config.world_list[i], i * 200 + 25, 225, (150, 150)))

        # Botão Voltar
        self.back_button = Text(self.display.get_display(), "Voltar", "Comic Sans MS", 40,
                                pygame.Color(0, 0, 0), (50, 500), True)

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

        # renderizar objetos na janela
        self.display.get_display().blit(self.background_image, (0, 0))

        self.message.blit()
        self.back_button.blit()

        for i in range(self.worlds_available):
            self.display.get_display().blit(self.worlds_box[i].get_image(), self.worlds_box[i].get_position())

    def logic_events(self):
        """
        Trata a interacao do usuario por meio dos eventos do mouse
        :return: None
        """
        # imagens de mundos
        for world in self.worlds_box:
            if world.get_rect().collidepoint(pygame.mouse.get_pos()):
                if self.unclicked:
                    world.on_normal()
                    self.clicked = False
                    self.unclicked = False

                    self.config.scene = self.id_cena + 1
                    self.config.world = world
                    self.close()
                elif self.clicked:
                    # efeito de clicar
                    world.on_click()
                else:
                    # efeito de mouse hover
                    world.on_hover()
            else:
                world.on_normal()

        if self.back_button.get_rect().collidepoint(pygame.mouse.get_pos()):
            if self.unclicked:
                self.back_button.on_normal()
                self.clicked = False
                self.unclicked = False

                self.config.scene = self.id_cena - 1
                self.close()
            elif self.clicked:
                # efeito de clicar
                self.back_button.on_click()
            else:
                # efeito de mouse hover
                self.back_button.on_hover()
        else:
            self.back_button.on_normal()

        self.unclicked = False
