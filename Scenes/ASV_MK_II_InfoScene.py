from Shared.Scene import *
from Shared.Colours import *
from Shared.Constants import *

class ASV_MK_II_InfoScene(Scene):

    def __init__(self, game=None):

        if game is not None:
            Scene.__init__(self, game)
            self.__ASV_MK_II_EQUIPMENT_Sprite = pygame.image.load(Constants.ASV_MK_II_EQUIPMENT)
            self.__ASV_MK_II_TRACE_Sprite = pygame.image.load(Constants.ASV_MK_II_TRACE)
            self.__greenButtonSprite = pygame.image.load(Constants.ARCADE_GREEN)
            self.__redButtonSprite = pygame.image.load(Constants.ARCADE_RED)
            self.__blueButtonSprite = pygame.image.load(Constants.ARCADE_BLUE)

        self.__page = 1

    def render(self):

        self.clear_text()

        # Draw Title
        self.add_text('Air to Surface Vessel Radar ASV Mk II', 385, 20, Colours.YELLOW, Colours.BLACK, 40)

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
            pass  # self.__AI_MK4_VOICE_Sound.play()

        Scene.start(self)

    def updateState(self):
        Scene.updateState(self)

    def renderPage1(self):
        self.add_text('The equipment', 148, 120, Colours.YELLOW,
                      Colours.BLACK, 28)
        self.add_text('', 148, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('This radar works on a similar frequency (176 MHz) to the AI Mk4', 148, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('and on very similar principles. With ASV only two aerials, port', 148, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('and starboard are required as the vertical displacement between', 148, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('the target and aircraft is simply the height of the aircraft.', 148, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The range of the radar exceeds that of the AI Mk4 and this is', 148, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('assumed to be due to the fact that the sea acts like a mirror', 148, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('and only the sea surface beneath the aircraft results in a', 148, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('strong echo and targets beyond this distance are not affected.', 148, 390, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The early ASV systems used separate transmit and receive aerials', 148, 420, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('but a later development used an Aerial Coupling unit containing a motor driven switch. Using a combination of', 148, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('quarter wave lines and spark gaps it was possible to stop the receiver being overloaded  by the transmitting', 148, 480, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('pulse and therefore the same aerial could be used for both functions, giving improved performance.', 148, 510, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 540, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Another variation used a very large aerial array mounted along the top of the fuselage. This was used broadside', 148, 570, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('on for sweeping the shipping lanes. The system could also be used as a beacon receiver at ranges up to 90 miles.', 148, 600, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 630, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 660, Colours.YELLOW, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__ASV_MK_II_EQUIPMENT_Sprite, (775, 120))

    def renderPage2(self):
        self.add_text('The display:', 148, 120, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Again the signal appears on the trace as a blip either to the left', 148, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('or the right depending whether the signal is port or starboard,', 148, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('and the distance from the bottom of the trace is equivalent to the', 148, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('range. Three distance ranges are selectable on the indicator, and', 148, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('the appropriate scales are engraved on the cursor.', 148, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The lower and larger blip is the simulated sea echo pulse at the', 148, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('height of the aircraft. Often the aircraft would fly low and the', 148, 390, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('noise echo would be lower down the trace. The upper pulse is a', 148, 420, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('simulated target, slightly to port of the aircraft flight line, and at', 148, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('a greater distance.', 148, 480, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 510, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 540, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 570, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 600, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 630, Colours.YELLOW, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__ASV_MK_II_TRACE_Sprite, (775, 120))