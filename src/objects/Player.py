# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

from pygame import *

from src.objects.ArtificialIntelligence import ArtificialIntelligence


class Player(object):
    def __init__(self, id: int, artificial_intelligence=None):
        self.id = id
        self.ai = artificial_intelligence
