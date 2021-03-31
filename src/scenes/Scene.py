# Projeto:  Projétil
# Autor:    Fernando Machado
# Data:     09/03/2021

import pygame

from src.objects.Window import Window
from src.config import Config


class Scene(object):
    def __init__(self, display: Window, config: Config):
        """
        Executa video de apresentacao do jogo.
        :param display: objeto contendo a tela
        :param config: objeto contendo as variaveis de controle
        """

        self.display = display
        self.config = config
        self.id_cena = 0

        self.background_color = pygame.Color(0, 0, 0)
        self.running = False

        self.clock = pygame.time.Clock()
        self.elapsed_time = 60

    def run(self):
        """
        Executa cena do jogo.
        :return: None
        """

        self.running = True

        while self.running:
            self.clock_tick()
            self.handle_exit()

            self.display.get_display().fill(self.background_color)
            self.update()
            pygame.display.update()

        self.on_close()

    def clock_tick(self):
        """
        Estabiliza e controla tempo de execucao de uma iteracao
        :return: None
        """

        self.clock.tick(self.elapsed_time)

    def handle_exit(self):
        """
        Trata quando o usuário clica para fechar a janela
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
                self.config.running = False
            self.handle_events(event)

    def close(self):
        """
        Finaliza o loop principal.
        :return: None
        """

        self.running = False

    def handle_events(self, event):
        """
        Deve ser implementado na sub-classe.
        Tratamento de eventos de entrada.
        :return: None.
        """
        pass

    def update(self):
        """
        Deve ser implementado na sub-classe.
        Executa no loop principal.
        :return: None.
        """
        pass

    def on_close(self):
        """
        Deve ser implementado na sub-classe.
        Executa apos o loop principal.
        :return: None.
        """
        pass
