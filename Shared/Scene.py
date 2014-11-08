import pygame
from Shared.Enums import *

class Scene:

    def __init__(self, game):
        self.__game = game
        self.__texts = []
        self.__TICKS_SINCE_LAST_EVENT = 0

    def render(self):
        for text in self.__texts:
            self.__game.screen.blit(text[0], text[1])

    def getGame(self):
        return self.__game

    def updateState(self):
        pass

    def handleEvents(self, events):
        if self.__TICKS_SINCE_LAST_EVENT == 2000:
            self.getGame().changeScene(Enums.Scene.FRONT)

        self.__TICKS_SINCE_LAST_EVENT += 1

        for event in events:
             if event.type == pygame.KEYUP:
                 if event.key == pygame.K_ESCAPE:
                     self.getGame().changeScene(Enums.Scene.FRONT)

    def clearText(self):
        self.__texts = []

    def addText(self, string, x=0, y=0, color = [255, 255, 255], background = [0, 0, 0], size = 17):
        font = pygame.font.Font(None, size)
        self.__texts.append([font.render(string, True, color, background), (x, y)])