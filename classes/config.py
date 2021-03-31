# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

from classes.jogador import Jogador


class Config(object):
    def __init__(self):
        """
        Armazena variaveis de controle do jogo
        """

        self.running = True             # app em execucao
        self.cena = 0                   # cena em execucao

        self.play_type = 3              # tipo de jogo (2: 2 jogadores, 3: 3 jogadores, 4: 4 jogadores)
        self.world = None               # objeto da classe Mundo
        self.world_list = [             # lista de caminhos para as imagens
            "img/background_forest.png",
            "img/background_forest.png",
            "img/background_forest.png",
            "img/background_forest.png"
        ]

        self.players = list()           # lista de objetos de jogadores e/ou IA