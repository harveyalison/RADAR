from Shared.Scene import *
from Shared.Colours import *
from Shared.Constants import *

class AirborneInterceptScene(Scene):

    def __init__(self, game=None):
        if game is not None:
            Scene.__init__(self, game)
            self.__MK_VIII_IN_BEAUFIGHTER_Sprite = pygame.image.load(Constants.MK_VIII_IN_BEAUFIGHTER)
            self.__blueButtonSprite = pygame.image.load(Constants.ARCADE_BLUE)
            self.__AIRBORNE_INTERCEPTION_RADAR_VOICE_Sound = pygame.mixer.Sound(Constants.AIRBORNE_INTERCEPTION_RADAR_VOICE)

        self.__page = 1

    def render(self):

        self.clear_text()

        # Draw Title
        self.add_text('Airborne Interception Radar', 420, 20, Colours.YELLOW, Colours.BLACK, 40)

        # Draw page body
        if self.__page == 1:
            self.renderPage1()

        # Draw footer
        self.add_text('Blue button: home', 410, 720, Colours.YELLOW, Colours.BLACK, 32)
        self.get_game().screen.blit(self.__blueButtonSprite, (360, 718))

        Scene.render(self)

    def handle_events(self, events):
        Scene.handle_events(self, events)

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE or event.key == ord('b'):
                    self.get_game().change_scene(Enums.Scene.FRONT)

    def start(self):

        if self.__page == 1:
            self.__AIRBORNE_INTERCEPTION_RADAR_VOICE_Sound.play()

        Scene.start(self)

    def updateState(self):
         Scene.updateState(self)

    def renderPage1(self):

        self.add_text('Airborne Interception radar, or AI, was the Royal Air Force (RAF) term for radar systems used to equip', 148, 80, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('aircraft in the air-to-air role. These radars are used primarily by RAF and Fleet Air Arm night fighters', 148, 110, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('and interceptors for locating and tracking other aircraft, although most AI radars could also be used in a', 148, 140, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('number of secondary roles as well. The term was sometimes used generically for similar radars used in', 148, 170, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('other countries.', 148, 200, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 230, Colours.YELLOW, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__MK_VIII_IN_BEAUFIGHTER_Sprite, (383, 260))
        self.add_text('The AI. Mk. VIII, seen here on a', 630, 260, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Beaufighter, set the pattern for', 630, 290, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('AI radars well into the 1970s.', 630, 320, Colours.YELLOW, Colours.BLACK, 28)

        self.add_text('The term was first used circa 1936, when a group at the Bawdsey Manor research center began considering', 148, 470, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('how to fit a radar system into an aircraft. This work led to the Airborne Intercept radar Mk. IV, the first', 148, 500, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('production air-to-air radar system. Mk. IV entered service in July 1940 and reached widespread availability', 148, 530, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('on the Bristol Beaufighter by early 1941. The Mk. IV helped end The Blitz, the Luftwaffe\'s night bombing', 148, 560, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('campaign of late 1940 and early 1941.', 148, 590, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 620, Colours.YELLOW, Colours.BLACK, 28)