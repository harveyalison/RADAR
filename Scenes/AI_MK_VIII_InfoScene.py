from Shared.Scene import *
from Shared.Colours import *
from Shared.Constants import *

class AI_MK_VIII_InfoScene(Scene):

    def __init__(self, game=None):
        if game is not None:
            Scene.__init__(self, game)
            self.__AI_MK_VIII_Sprite = pygame.image.load(Constants.AI_MK_VIII)
            self.__AI_MK_VIII_RX_Sprite = pygame.image.load(Constants.AI_MK_VIII_RX)
            self.__greenButtonSprite = pygame.image.load(Constants.ARCADE_GREEN)
            self.__redButtonSprite = pygame.image.load(Constants.ARCADE_RED)
            self.__blueButtonSprite = pygame.image.load(Constants.ARCADE_BLUE)

        self.__page = 1

    def render(self):

        self.clear_text()

        # Draw Title
        self.add_text('AI MK VIII Airbourne Interception RADAR', 390, 20, Colours.YELLOW, Colours.BLACK, 40)

        # Draw page body
        if self.__page == 1:
            self.renderPage1()

        # Draw footer
        self.add_text('Blue button: home', 410, 720, Colours.YELLOW, Colours.BLACK, 32)
        #self.add_text('Red button: simulation', 720, 720, Colours.YELLOW, Colours.BLACK, 32)

        self.get_game().screen.blit(self.__blueButtonSprite, (360, 718))
        #self.get_game().screen.blit(self.__redButtonSprite, (680, 718))

        Scene.render(self)

    def handle_events(self, events):
        Scene.handle_events(self, events)

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE or event.key == ord('b'):
                    self.get_game().change_scene(Enums.Scene.FRONT)
                #elif event.key == ord('a'):
                #    self.get_game().change_scene(Enums.Scene.AI_MK_IV_SIMULATOR)

    def updateState(self):
         Scene.updateState(self)

    def renderPage1(self):

        self.add_text('THE EQUIPMENT', 148, 80, Colours.YELLOW, Colours.BLACK, 32)

        self.add_text('The AI MK 7/8 was the first centimetric Airborne Interception radar, appearing in about 1942/43 and', 148, 120, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('installed in Beaufighters and Mosquitoes. The earlier AI MK 4 only worked at a frequency of 200 MHz.', 148, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Gone are the multiple aerials all to be replaced by a single transmit/receive aerial mounted at the centre', 148, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('of the radar dish. The dish is mounted in the nose of the aircraft behind a transparent cover.', 148, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('At 10cms(3000MHz) the radar beam is much narrower, almost operating like a torch beam, and thus the', 148, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('RADAR beam can be made to sweep around the sky looking for a target. The dish is used to focus the', 148, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('beam and point it in the required direction. The dish is spun on its axis and initially the beam is directed', 148, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('forwards. The dish is then progressively turned "off axis" thus sweeping a spiral in the sky in ', 148, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('front of the aircraft. When it reaches a maximum spiral outwards it returns to the centre on an inwards', 148, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('spiral. The whole process is repeated continuously.', 148, 390, Colours.YELLOW, Colours.BLACK, 28)

        self.add_text('Indicator', 363, 470, Colours.YELLOW, Colours.BLACK, 28)
        self.get_game().screen.blit(self.__AI_MK_VIII_Sprite, (363, 510))
        self.add_text('Receiver', 778, 470, Colours.YELLOW, Colours.BLACK, 28)
        self.get_game().screen.blit(self.__AI_MK_VIII_RX_Sprite, (778, 510))










                

