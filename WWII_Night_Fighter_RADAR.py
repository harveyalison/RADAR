import pygame

from Shared.Colours import *

#from Highscore import *
#from Ball import *
#from Pad import *
#from Level import *
from Scenes import *
from Shared.Constants import *

class WWII_Night_Fighter_Radar:

    def __init__(self):
        #self.__lives = 1
        #self.__score = 0

        #self.__level = Level(self)
        #self.__level.load(0)

        #self.__pad = Pad((GameConstants.SCREEN_SIZE[0]/2,
        #                 GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1]),
        #                 pygame.image.load(GameConstants.SPRITE_PAD)
        #                 )
        #self.__balls = [
        #    Ball((400, 400), pygame.image.load(GameConstants.SPRITE_BALL), self)
        #]

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("WWII Night Fighter RADAR")

        self.__clock = pygame.time.Clock()

        #size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        #self.screen = pygame.display.set_mode(size, pygame.DOUBLEBUF|pygame.FULLSCREEN, 32)

        self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        pygame.mouse.set_visible(0)

        self.__scenes = (
            FrontScene(self),
            IntroScene(self),
            WhatIsRadarScene(self),
            AirborneInterceptScene(self),
            ASV_MK_II_InfoScene(self),
            ASV_MK_II_SimulatorScene(self),
            ASV_MK_II_GameScene(self),
            AI_MK_IV_InfoScene(self),
            AI_MK_IV_SimulatorScene(self),
            AI_MK_IV_GameScene(self),
            AI_MK_VIII_InfoScene(self),
            AI_MK_VIII_SimulatorScene(self),
            AI_MK_VIII_GameScene(self),            
            AI_MK_X_InfoScene(self),
            AI_MK_X_SimulatorScene(self),
            AI_MK_X_GameScene(self)       
        )

        self.__currentScene = 0

        #self.__sounds = (
        #    pygame.mixer.Sound(GameConstants.SOUND_FILE_GAMEOVER),
        #    pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK),
        #    pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_LIFE),
        #    pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_SPEED),
        #    pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_WALL),
        #    pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_PAD)
        #)

    def start(self):
        while 1:
            self.__clock.tick(20)

            self.screen.fill(Colours.BLACK)

            currentScene = self.__scenes[self.__currentScene]

            currentScene.updateState()

            currentScene.handleEvents(pygame.event.get())

            currentScene.render()

            pygame.display.update()


    def changeScene(self, scene):
        self.__currentScene = scene

    #def getLevel(self):
    #    return self.__level

    #def getScore(self):
    #    return self.__score

    #def increaseScore(self, score):
    #    self.__score += score

    #def getLives(self):
    #    return self.__lives

    #def getBalls(self):
    #    return self.__balls

    #def getPad(self):
    #    return self.__pad

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()

    #def reduceLives(self):
    #    self.__lives -= 1

    #def increaseLives(self):
    #    self.__lives += 1

    #def reset(self):
    #    self.__lives = 5
    #    self.__score = 0
    #    self.__level.load(0)

if __name__ == "__main__":
	WWII_Night_Fighter_Radar().start()