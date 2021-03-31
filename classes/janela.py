# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame


class Janela(object):
    def __init__(self):
        """
        Cria janela do jogo e define o fps.
        """

        self.width = 800
        self.height = 600

        pygame.display.set_caption("Projétil")
        self.display = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        self.elapsed_time = 60

    def get_display(self) -> pygame.Surface:
        """
        Retorna janela do jogo
        :return: Janela do jogo
        """

        return self.display
