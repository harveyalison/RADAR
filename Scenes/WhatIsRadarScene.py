from Shared.Scene import *
from Shared.Colours import *
from Shared.Constants import *

class WhatIsRadarScene(Scene):
    def __init__(self, game=None):

        if game is not None:
            Scene.__init__(self, game)
            self.__HOW_RADAR_WORKS_Sprite = pygame.image.load(Constants.HOW_RADAR_WORKS)
            self.__MOBILE_RADAR_Sprite = pygame.image.load(Constants.MOBILE_RADAR)
            self.__greenButtonSprite = pygame.image.load(Constants.ARCADE_GREEN)
            self.__redButtonSprite = pygame.image.load(Constants.ARCADE_RED)
            self.__blueButtonSprite = pygame.image.load(Constants.ARCADE_BLUE)
            self.__WHAT_IS_RADAR_VOICE_Sound = pygame.mixer.Sound(Constants.WHAT_IS_RADAR_VOICE)
            self.__HOW_RADAR_WORKS_VOICE_Sound = pygame.mixer.Sound(Constants.HOW_RADAR_WORKS_VOICE)

        self.__page = 1

    def render(self):

        self.clear_text()

        # Draw Title
        self.add_text('ALL ABOUT RADAR', 485, 20, Colours.YELLOW, Colours.BLACK, 40)

        # Draw page body
        if self.__page == 1:
            self.renderPage1()
        elif self.__page == 2:
            self.renderPage2()

        # Draw footer
        self.add_text('Green button: find out more', 385, 720, Colours.YELLOW, Colours.BLACK, 32)
        self.add_text('Blue button: home', 740, 720, Colours.YELLOW, Colours.BLACK, 32)

        self.get_game().screen.blit(self.__greenButtonSprite, (340, 718))
        self.get_game().screen.blit(self.__blueButtonSprite, (700, 718))

        Scene.render(self)

    def handle_events(self, events):
        Scene.handle_events(self, events)

        for event in events:
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_ESCAPE or event.key == ord('b'):
                    self.get_game().change_scene(Enums.Scene.FRONT)
                    self.__page = 1
                else:
                    pygame.mixer.stop()

                    if event.key == ord('c') or event.key == pygame.K_RETURN:
                        if self.__page == 1:
                            self.__page = 2
                        elif self.__page == 2:
                            self.__page = 1
                    if event.key == pygame.K_LEFT:
                        if self.__page == 2:
                            self.__page = 1
                        elif self.__page == 1:
                            self.__page = 2
                    if event.key == pygame.K_RIGHT:
                        if self.__page == 2:
                            self.__page = 1
                        elif self.__page == 1:
                            self.__page = 2
                    self.start()

    def start(self):

        if self.__page == 1:
            self.__WHAT_IS_RADAR_VOICE_Sound.play()
        elif self.__page == 2:
            self.__HOW_RADAR_WORKS_VOICE_Sound.play()

        Scene.start(self)

    def updateState(self):
        Scene.updateState(self)

    def renderPage1(self):
        self.add_text('What is Radar?', 148, 120, Colours.YELLOW,
                      Colours.BLACK, 28)
        self.add_text('', 148, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('We can see objects in the world around us because light', 148, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('(usually from the Sun) reflects off them into our eyes.', 148, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('If you want to walk at night, you can shine a torch in front', 148, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('to see where you\'re going. The light beam travels out from', 148, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('the torch, reflects off objects in front of you, and bounces', 148, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('back into your eyes. Your brain instantly computes what this', 148, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('means: it tells you how far away objects are and makes your', 148, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Mobile radar detector truck', 815, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('body move so you don\'t trip over things.', 148, 390, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 420, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Radar works in much the same way. The word \'radar\' stands for RAdio Detection And Ranging, which gives a pretty', 148, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('big clue as to what it does and how it works. Imagine an airplane flying at night through thick fog. The pilots can\'t', 148, 480, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('see where they\'re going, so they use the radar to help them.', 148, 510, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('An airplane\'s radar is a bit like a torch that uses radio waves instead of light. The plane transmits an intermittent', 148, 540, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('radar beam (so it sends a signal only part of the time) and, for the rest of the time, "listens" out for any reflections of', 148, 570, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('that beam from nearby objects. If reflections are detected, the plane knows something is nearby - and it can use the', 148, 600, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('time taken for the reflections to arrive to figure out how far away it is. In other words, radar is a bit like the', 148, 630, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('echolocation system that "blind" bats use to see and fly in the dark.', 148, 660, Colours.YELLOW, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__MOBILE_RADAR_Sprite, (795, 120))

    def renderPage2(self):
        self.add_text('Here is a summary of how radar works:', 148, 120, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('1: Magnetron generates high-frequency radio waves.', 148, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('2: Switch sends signal through to antenna.', 148, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('3: Antenna acts as transmitter, sending narrow beam of', 148, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('    radio waves through the air.', 148, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('4: Radio waves hit enemy airplane and reflect back.', 148, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('5: Antenna picks up reflected waves during a break between', 148, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('    transmissions. Note that the same antenna acts as both', 148, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('    transmitter and receiver, alternately sending out', 148, 390, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('    radio waves and receiving them.', 148, 420, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('6: Switch passes signal through to receiver unit.', 148, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('7: Computer in receiver unit processes reflected waves.', 148, 480, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('8: Enemy plane shows up on radar display, with any', 148, 510, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('    other nearby targets.', 148, 540, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 570, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 600, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 630, Colours.YELLOW, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__HOW_RADAR_WORKS_Sprite, (795, 120))















                

