# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021
import pygame
from pygame import *

from src.objects.Sound import Sound


class Text(object):
    def __init__(self, surface: Surface, text: str, font: str, size: int, color: Color, pos: tuple, button=False):
        self.surface = surface
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.pos = pos
        self.text_center = None
        self.is_hover = False
        self.hover_sound = None
        self.click_sound = None
        self.button = button
        self.render()

        self.set_center()

    def set_color(self, color: Color):
        self.color = color

    def get_text(self) -> str:
        return self.text

    def set_text(self, text: str):
        self.text = text

    def get_position(self) -> tuple:
        return self.pos

    def render(self, factor=1):
        my_font = font.SysFont(self.font, int(self.size * factor))
        self.text_surface = my_font.render(self.text, False, self.color)

        if self.button:
            self.rect = Rect(
                10,
                self.pos[1] - 2,
                self.surface.get_rect().right - 20,
                self.text_surface.get_height() + 10
            )

    def blit(self):
        if self.button:
            draw.rect(
                self.surface,
                (0, 0, 0),
                self.rect,
                -1
            )

        self.pos = (
            self.text_center[0] - self.text_surface.get_rect().width // 2,
            self.text_center[1] - self.text_surface.get_rect().height // 2
        )

        self.surface.blit(self.text_surface, self.pos)

    def set_center(self):
        self.text_center = (
            self.pos[0] + self.text_surface.get_rect().centerx,
            self.pos[1] + self.text_surface.get_rect().centery
        )

    def center_x(self):
        self.pos = (
            self.surface.get_width() / 2 - self.text_surface.get_width() / 2,
            self.pos[1]
        )
        self.render()
        self.set_center()

    def center_y(self):
        self.pos = (
            self.pos[0],
            self.surface.get_height() / 2 - self.text_surface.get_height() / 2
        )
        self.render()
        self.set_center()

    def set_size(self, size: int):
        self.size = size
        self.render()

    def set_hover_sound(self, sound: Sound):
        self.hover_sound = sound

    def set_click_sound(self, sound: Sound):
        self.click_sound = sound

    def on_hover(self):
        self.render(1.25)
        if not self.is_hover and self.hover_sound is not None:
            self.is_hover = True
            self.hover_sound.play()

    def on_normal(self):
        self.render(1)
        self.is_hover = False

    def on_click(self):
        self.render(0.8)
        self.click_sound.play()

    def get_rect(self, abs=None) -> Rect:
        if abs:
            self.rect.x += abs[0]
            self.rect.y += abs[1]
            return self.rect
        else:
            rect = self.text_surface.get_rect()
            rect.x += self.pos[0]
            rect.y += self.pos[1]
            return rect
