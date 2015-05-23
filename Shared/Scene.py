import pygame
from Shared.Enums import *
from Shared.Colours import *

class Scene:
    def __init__(self, game):
        self.__game = game
        self.__texts = []
        self.__TICKS_SINCE_LAST_EVENT = 0

    def render(self):
        for text in self.__texts:
            self.__game.screen.blit(text[0], text[1])

    def get_game(self):
        return self.__game

    def updateState(self):
        pass

    def start(self):
        self.__TICKS_SINCE_LAST_EVENT = 0

    def handle_events(self, events):
        if self.__TICKS_SINCE_LAST_EVENT == 2500:
            self.get_game().change_scene(Enums.Scene.FRONT)

        self.__TICKS_SINCE_LAST_EVENT += 1

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_b:
                    self.get_game().change_scene(Enums.Scene.FRONT)
                    self.__page = 1

    def clear_text(self):
        self.__texts = []

    def add_text(self, string, x=0, y=0, color=Colours.GREEN, background=Colours.BLACK, size=17):
        font = pygame.font.Font(None, size)
        self.__texts.append([font.render(string, True, color, background), (x, y)])