# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame
import time

from src.objects.Text import Text


class Information(object):
    def __init__(self, display: pygame.Surface, posx: int, posy: int):
        self.posx = posx
        self.posy = posy
        self.message = ""
        self.msg_time = 3
        self.msg_over_time = 0
        self.reset_over_time()
        self.color = pygame.Color(50, 80, 60)

        self.has_message = False

        self.text = Text(display, self.message, "Comic Sans MS", 40, self.color, (posx, posy))

    def blit(self):
        if self.has_message:
            seconds = int(self.msg_over_time - time.time())
            if seconds <= 0:
                self.text.set_text("")
                self.has_message = False

            self.text.render()
            self.text.center_x()
            self.text.center_y()
            self.text.blit()

    def set_message(self, msg: str):
        self.text.set_text(msg)
        self.has_message = True
        self.reset_over_time()

    def reset_over_time(self):
        self.msg_over_time = time.time() + self.msg_time
