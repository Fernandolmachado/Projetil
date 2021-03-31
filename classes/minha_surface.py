# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

from pygame import *


class MinhaSurface(Surface):
    def __init__(self, posx: int, posy: int, color: Color, *args, **kwargs):
        """
        Superficie para criar objetos do jogo
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)

        self.posx = posx
        self.posy = posy
        self.color = color

    def get_position(self) -> tuple:
        return self.posx, self.posy

    def get_posx(self) -> int:
        return self.posx

    def get_posy(self) -> int:
        return self.posy

    def set_pos(self, position: list):
        self.posx, self.posy = position

    def get_color(self) -> Color:
        return self.color

    def set_color(self, color: Color):
        self.color = color

    def fill_with_border(self, border: int):
        """
        Preenche surface com a cor atribuida e desenha borda
        :return: None
        """
        self.fill(self.color)
        draw.rect(self, (0, 0, 0), Rect(5, 5, self.get_width() - 10, self.get_height() - 10), border)
