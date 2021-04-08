# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     07/04/2021

from pygame import *


class Button(object):
    def __init__(self, surface: Surface, center: tuple, text: str, font_size: int, color: Color):
        self.surface = surface
        self.center = center
        self.text = text
        self.font = "Comic Sans MS"
        self.font_size = font_size
        self.color = color

        self.text_surface = None
        self.rect = None
        self.render()

    def render(self, factor=1):
        my_font = font.SysFont(self.font, int(self.font_size * factor))
        self.text_surface = my_font.render(self.text, False, self.color)

        self.rect = self.text_surface.get_rect()

    def blit(self):

        pos = (
            self.center[0] - self.text_surface.get_rect().width // 2,
            self.center[1] - self.text_surface.get_rect().height // 2
        )

        self.rect.left = pos[0]
        self.rect.top = pos[1]

        self.surface.blit(self.text_surface, pos)

    def on_normal(self):
        self.render(1)

    def on_click(self):
        self.render(0.75)

    def on_hover(self):
        self.render(1.25)

    def get_surface(self) -> Surface:
        return self.surface
    # Getters e Setters

    def set_surface(self, surface: Surface):
        self.surface = surface

    def get_center(self) -> tuple:
        return self.center

    def set_center(self, centerx: int, centery: int):
        self.center = (centerx, centery)

    def get_text(self) -> str:
        return self.text

    def set_text(self, text: str):
        self.text = text

    def get_font_size(self) -> str:
        return self.font_size

    def set_font_size(self, font_size: str):
        self.font_size = font_size

    def get_color(self) -> Color:
        return self.color

    def set_color(self, color: Color):
        self.color = color

    def get_rect(self) -> Rect:
        return self.rect
