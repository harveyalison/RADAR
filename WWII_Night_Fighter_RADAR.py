from Scenes import *
from Shared.Constants import *

class WWIINightFighterRadar:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("WWII Night Fighter RADAR")

        self.__clock = pygame.time.Clock()

        # Un-comment these lines, and comment out the one below, to run full screen
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

        self.__sounds = (
            #    pygame.mixer.Sound(GameConstants.SOUND_FILE_GAMEOVER),
            #    pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK),
            #    pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_LIFE),
            #    pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_SPEED),
            #    pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_WALL),
            #    pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_PAD)
        )

    def start(self):
        while 1:
            self.__clock.tick(20)

            self.screen.fill(Colours.BLACK)

            currentscene = self.__scenes[self.__currentScene]

            currentscene.updateState()

            currentscene.handle_events(pygame.event.get())

            currentscene.render()

            pygame.display.update()


    def change_scene(self, scene):
        pygame.mixer.stop()
        self.__currentScene = scene
        self.__scenes[self.__currentScene].start()


    def play_sound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()


if __name__ == "__main__":
    WWIINightFighterRadar().start()