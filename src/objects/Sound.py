import pygame


class Sound(pygame.mixer.Sound):
    def __init__(self, sound_file: str):
        self.file = sound_file
        super().__init__(sound_file)

