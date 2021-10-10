# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame
import random

from src.config import Config
from src.objects.Window import Window
from src.scenes.Scene import Scene
from src.objects.Sprite import Sprite
from src.objects.Player import Player
from src.objects.Bullet import Bullet

RIGHT = 1
LEFT = -1


class Game(Scene):
    def __init__(self, display: Window, config: Config):
        """
        Executa do jogo.
        :param display: objeto contendo a tela e o clock
        :param config: objeto contendo as variaveis de controle
        """
        super().__init__(display, config)
        self.id_cena = 4

        # CARREGA ASSETS
        # Carrega imagem de fundo
        self.background_image = pygame.image.load("img/world.png").convert_alpha()
        self.background_image = pygame.transform.scale(
            self.background_image,
            (int(self.display.get_display().get_width()), int(self.display.get_display().get_height()))
        )
        self.ground = pygame.Rect(0, 510, 800, 90)

        # Trata jogadores
        self.sprites = Sprite("img/player.png")
        self.players = self.config.players
        self.handle_players()

        # TODO: Gerar turno aleatório
        self.player_turn = self.players[0]

        # Bala de canhão
        self.bullet = None

        # variaveis de controle do mouse
        self.clicked = False
        self.click_released = False
        self.event_pos = None
        self.event = None

        # Altera cursor
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_NO)

    def update(self):
        self.button_events()

        if self.bullet is not None:
            self.bullet.move()
            for player in self.players:
                if player.get_id() != self.player_turn.get_id() and self.bullet.check_impact(player.get_rect()):
                    player.take_damage(10)  # TODO: validar dano
                    self.bullet = None
            if self.bullet.check_impact(self.ground):
                self.bullet = None
            elif self.bullet.get_center()[0] < 0 or self.bullet.get_center()[0] > self.display.get_display().get_width():
                self.bullet = None

        # renderizar objetos na janela
        self.display.get_display().blit(self.background_image, (0, 0))

        if self.bullet is not None:
            self.bullet.blit(self.display.get_display())

        self.player_turn.blit(self.display.get_display())


    def handle_events(self, event):
        # evento de clique com botao esquerdo do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.clicked = True
            self.event_pos = event.pos
        # evento de liberacao do botao esquerdo do mouse
        elif event.type == pygame.MOUSEBUTTONUP:
            self.click_released = True
            self.clicked = False
            self.event_pos = event.pos
        else:
            self.click_released = False

    def button_events(self):

        if self.clicked:
            self.bullet = Bullet(self.player_turn.get_cennon_center(), 3, self.player_turn.get_angle())

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.player_turn.move(RIGHT)
        elif keys[pygame.K_LEFT]:
            self.player_turn.move(LEFT)

        self.player_turn.aim_cannon(pygame.mouse.get_pos())

    def handle_players(self):
        sprites = [self.sprites.get_sprites([j, 0, 80, 60]) for j in range(5, 160, 90)]
        sprites.append(self.sprites.get_sprites([185, 4, 50, 13], cannon=True))
        self.players[0].set_player_images(sprites, 50, 450)

        # TODO: Atribuir para os outros players
        # for i in range(len(self.players)):
        #     #Indica sprite do player [ vermelho, verde, azul, amarelo
        #     self.players[i].set_pos(20 + i*50, 0)
        #     sheet = self.sprites.get_sheet()
        #     sprites = [self.sprites.get_sprites([j, i*200, 100, 200]) for j in range(0, 200, 100)]
        #     sprites.append(self.sprites.get_sprites([200, i*50, 100, 50]))
        #     self.players[i].set_player_images(sprites)
