# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     12/03/2021

from pygame import *


class Imagem(object):
    def __init__(self, filename: str, posx: int, posy: int, size: tuple):
        self.filename = filename
        self.posx = posx
        self.posy = posy
        self.width = size[0]
        self.height = size[1]

        self.image = image.load(self.filename).convert_alpha()
        self.scale(self.width, self.height)

    def get_position(self) -> tuple:
        return self.posx, self.posy

    def get_image(self) -> Surface:
        return self.image
    
    def on_hover(self):
        self.scale(self.width * 1.1, self.height * 1.1)

    def on_click(self):
        self.scale(self.width * 0.9, self.height * 0.9)

    def on_normal(self):
        self.scale(self.width, self.height)

    def scale(self, width, height):
        self.image = transform.scale(self.image, (int(width), int(height)))

    def get_rect(self) -> Rect:
        return Rect(self.posx, self.posy, self.image.get_width(), self.image.get_height())
