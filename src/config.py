# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021


class   Config(object):
    def __init__(self):
        """
        Armazena variaveis de controle do jogo
        """

        self.running = True  # app em execucao
        self.scene = 0  # cena em execucao

        self.play_type = 3  # tipo de jogo (2: 2 jogadores, 3: 3 jogadores, 4: 4 jogadores)
        self.world = None  # objeto da classe Mundo
        self.world_list = [  # lista de caminhos para as imagens
            "img/background_forest.png",
            "img/background_forest.png",
            "img/background_forest.png",
            "img/background_forest.png"
        ]

        self.players = list()  # lista de objetos de jogadores e/ou IA
        self.gravity = 1
        self.RIGHT = 1
        self.LEFT = -1

        self.menu_music = None

        self.sounds = {
            "menu_music": "sound/menu_music.wav",
            "cursor": "sound/cursor.flac",
            "select": "sound/select.wav",
            "game_music": "sound/game_music.wav",
            "start": "sound/start_game.wav",
            "turn": "sound/turn_alert.wav",
            "tank": "sound/tank_moving.wav",
            "cannon": "sound/cannon_aim.wav",
            "shot": "sound/cannon_shot.wav",
            "collision": "sound/collision.flac",
            "on_the_tank": "sound/bullet_collision.wav",
            "on_the_ground": "sound/on_the_ground.wav",
            "timer": "sound/timer_alert.wav",
            "end": "sound/end_game.wav"
        }
