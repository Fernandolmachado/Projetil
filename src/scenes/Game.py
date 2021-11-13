# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame
import random

from src.config import Config
from src.objects.Window import Window
from src.scenes.Scene import Scene
from src.objects.Sprite import Sprite
from src.objects.Bullet import Bullet
from src.objects.Timer import Timer
from src.objects.Information import Information
from src.utils.Row import Row


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
        self.players = self.config.players.copy()
        self.handle_players()

        self.players_row = Row()
        self.player_turn = None
        self.shooting = False
        self.end_turn_counter = 0
        self.define_turn()

        # Bala de canhão
        self.bullet = None
        self.damage = 20

        # variaveis de controle do mouse
        self.clicked = False
        self.click_released = False
        self.event_pos = None
        self.event = None

        # Timer de rodadas
        self.timer = Timer(self.display.get_display(), 15, 390, 20)

        # Informação
        self.message = Information(self.display.get_display(), 400, 200)
        player_color = self.get_player_color()
        self.message.set_message("Vez do " + player_color)

        # Fim de jogo
        self.end_game = False
        self.end_game_counter = 0

        # Altera cursor
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_NO)

    def update(self):
        self.movement_events()

        # Trata bala atirada
        if self.bullet is not None:
            self.shooting = True
            bullet_gone = False
            self.bullet.move()
            for player in self.players:
                if player.has_life() and self.bullet.check_impact(player.get_rect()):
                    player.take_damage(self.damage)
                    bullet_gone = True
                    break
            if self.bullet.check_impact(self.ground):
                bullet_gone = True
            elif self.bullet.get_center()[0] < 0 or self.bullet.get_center()[0] > self.display.get_display().get_width():
                bullet_gone = True
            if bullet_gone:
                self.bullet = None

        # Espera alguns instantes para mudar de turno
        if self.shooting:
            self.end_turn_counter += 1
            if self.end_turn_counter > 150:
                # elimina jogador derrotado
                for player in self.players:
                    if not player.has_life():
                        player.set_dead()
                self.shooting = False
                self.end_turn_counter = 0
                self.prepare_next_turn()

        # Verifica se tempo do turno acabou e prepara próxima jogada
        if not self.shooting and self.timer.is_over():
            self.prepare_next_turn()

        # Verifica fim de jogo
        if not self.shooting and self.players_row.length() == 0:
            player_color = self.get_player_color()
            self.message.set_message(player_color + " Venceu!")
            end_game = True
            self.end_game_counter += 1

            if self.end_game_counter > 100:
                self.close()

        # limpa jogadores mortos da fila de turnos
        self.players_row.clean()

        # Renderizar objetos na janela
        self.display.get_display().blit(self.background_image, (0, 0))

        self.message.blit()

        self.timer.blit()

        if self.bullet is not None:
            self.bullet.blit(self.display.get_display())

        for player in self.players:
            if not player.is_dead():
                player.blit(self.display.get_display())

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

    def movement_events(self):
        if not self.shooting:
            if not self.player_turn.is_ai():
                # Caso seja jogador
                if self.clicked:
                    self.bullet = Bullet(
                        self.player_turn.get_cennon_center(),
                        3,
                        self.player_turn.get_angle(),
                        self.player_turn.get_force(),
                        self.config.gravity
                    )
                else:
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_RIGHT]:
                        self.player_turn.move(self.config.RIGHT, self.players_row.get_players())
                    elif keys[pygame.K_LEFT]:
                        self.player_turn.move(self.config.LEFT, self.players_row.get_players())

                    self.player_turn.aim_cannon(pygame.mouse.get_pos())
            elif self.players_row.length() > 0:
                # Caso seja máquina
                fire = self.player_turn.ai_moving(self.players_row.get_players(), self.timer, self.config)

                if fire:
                    self.bullet = Bullet(
                        self.player_turn.get_cennon_center(),
                        3,
                        self.player_turn.get_angle(),
                        self.player_turn.get_force(),
                        self.config.gravity
                    )

    def handle_players(self):
        for i in range(len(self.players)):
            # Obtem imagens do tank
            sprites = [self.sprites.get_sprites([j, (i * 65) + 5, 80, 60]) for j in range(5, 160, 90)]
            # Obtem imagem do canhão
            sprites.append(self.sprites.get_sprites([185, (i * 65) + 4, 50, 13], cannon=True))
            # Atribui imagens e posição
            self.players[i].set_player_images(sprites, (i * 200) + 50, 450)

    def define_turn(self):
        temp_players_list = self.players.copy()
        for i in range(4):
            choosed_player = random.choice(temp_players_list)
            self.players.index(choosed_player)
            self.players_row.set_player(self.players[self.players.index(choosed_player)])
            temp_players_list.remove(choosed_player)

        self.player_turn = self.players_row.get_player()

    def get_player_color(self, player=None) -> str:

        if player is not None:
            working_player = player
        else:
            working_player = self.player_turn
        color = ""
        if working_player.get_id() == 1:
            color = "Vermelho"
        if working_player.get_id() == 2:
            color = "Verde"
        if working_player.get_id() == 3:
            color = "Azul"
        if working_player.get_id() == 4:
            color = "Amarelo"

        return color

    def prepare_next_turn(self):
        self.players_row.set_player(self.player_turn)
        self.player_turn = self.players_row.get_player()
        player_color = self.get_player_color()
        self.message.set_message("Vez do " + player_color)
        self.timer.reset_over_time()

    def on_close(self):
        self.config.scene = self.id_cena - 2
