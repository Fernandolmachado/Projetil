# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame

from src.scenes.Scene import Scene
from src.objects.Window import Window
from src.config import Config


class Presentation(Scene):
    def __init__(self, display: Window, config: Config):
        """
        Executa video de apresentacao do jogo.
        :param display: objeto contendo a tela
        :param config: objeto contendo as variaveis de controle
        """
        super().__init__(display, config)
        self.id_cena = 0

        # define cor de fundo para branco
        self.background_color.r = 255
        self.background_color.g = 255
        self.background_color.b = 255

        # carrega imagem de fundo
        self.background_image = pygame.image.load("img/apresentacao_1.png").convert_alpha()
        self.background_image = pygame.transform.scale(
            self.background_image,
            (int(self.display.get_display().get_width() * 1.25), int(self.display.get_display().get_height() * 1.25))
        )

        # variaveis de controle para transparencia e fim
        self.times = 0
        self.alpha = 255

    def update(self):
        # renderiza imagem de fundo
        self.display.get_display().blit(self.background_image, (0, 0))

        self.times += 1
        if self.times > 145:                            # Controla transparencia da imagem
            self.alpha -= 2
            self.background_image.set_alpha(self.alpha)
        if self.times > 300:                            # Finaliza apresentacao
            self.close()

    def on_close(self):
        if self.config.running:
            self.config.scene = self.id_cena + 1
