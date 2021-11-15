# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame
import time

from src.objects.Sound import Sound
from src.objects.Text import Text


class Timer(object):
    def __init__(self, display: pygame.Surface, turn_time: int, centerx: int, centery: int):
        self.centerx = centerx
        self.centery = centery
        self.turn_time = turn_time
        self.over_time = 0
        self.timer_sound = None
        self.temp_timer = 0
        self.reset_over_time()

        self.text = Text(display, str(turn_time), "Comic Sans MS", 40, pygame.Color(0, 0, 0), (centerx, centery))

    def blit(self):

        if self.get_seconds() < 5:
            if self.temp_timer == 0:
                self.timer_sound.play()
                self.temp_timer = self.get_seconds()

            if self.temp_timer != self.get_seconds():
                self.timer_sound.play()
                self.temp_timer = self.get_seconds()
        else:
           self.temp_timer = 0

        self.text.set_text(str(self.get_seconds()))
        self.text.render()
        self.text.blit()

    def is_over(self) -> bool:
        if int(self.over_time - time.time()) <= 0:
            return True
        else:
            return False

    def get_seconds(self) -> int:
        seconds = int(self.over_time - time.time())
        if seconds < 0:
            seconds = 0
        return seconds

    def reset_over_time(self):
        self.over_time = time.time() + self.turn_time

    def set_sound(self, sound: Sound):
        self.timer_sound = sound
