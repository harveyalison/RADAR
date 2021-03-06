import time
from Shared.Scene import *
from Shared.Colours import *
from Shared.Constants import *

class AI_MK_IV_InfoScene(Scene):

    def __init__(self, game=None):

        if game is not None:
            Scene.__init__(self, game)
            self.__AI_MK_IV_RECEIVER_Sprite = pygame.image.load(Constants.AI_MK4_RECEIVER)
            self.__AI_MK4_INDICATOR_Sprite = pygame.image.load(Constants.AI_MK4_INDICATOR)
            self.__AI_MK4_MIXER_Sprite = pygame.image.load(Constants.AI_MK_IV_MIXER)
            self.__AI_MK4_TRACE_Sprite = pygame.image.load(Constants.AI_MK4_TRACE)
            self.__AI_MK4_EQUIPMENT_VOICE_Sound = pygame.mixer.Sound(Constants.AI_MK4_EQUIPMENT_VOICE)
            self.__AI_MK4_INDICATOR_VOICE_Sound = pygame.mixer.Sound(Constants.AI_MK4_INDICATOR_VOICE)
            self.__AI_MK4_RECEIVER_VOICE_Sound = pygame.mixer.Sound(Constants.AI_MK4_RECEIVER_VOICE)
            self.__greenButtonSprite = pygame.image.load(Constants.ARCADE_GREEN)
            self.__redButtonSprite = pygame.image.load(Constants.ARCADE_RED)
            self.__blueButtonSprite = pygame.image.load(Constants.ARCADE_BLUE)

        self.__page = 1

    def render(self):
       
        self.clear_text()

        # Draw Title
        self.add_text('AI MK IV Airbourne Interception Radar', 350, 20, Colours.YELLOW, Colours.BLACK, 40)

        # Draw page body
        if self.__page == 1:
            self.renderPage1()
        elif self.__page == 2:
            self.renderPage2()
        elif self.__page == 3:
            self.renderPage3()

        # Draw footer
        self.add_text('Green button: find out more |', 240, 720, Colours.YELLOW, Colours.BLACK, 32)
        self.add_text('Blue button: home |', 605, 720, Colours.YELLOW, Colours.BLACK, 32)
        self.add_text('Red button: simulation', 870, 720, Colours.YELLOW, Colours.BLACK, 32)

        self.get_game().screen.blit(self.__greenButtonSprite, (200, 718))
        self.get_game().screen.blit(self.__blueButtonSprite, (565, 718))
        self.get_game().screen.blit(self.__redButtonSprite, (830, 718))

        Scene.render(self)

    def handle_events(self, events):
        Scene.handle_events(self, events)

        for event in events:
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_ESCAPE or event.key == ord('b'):
                    self.get_game().change_scene(Enums.Scene.FRONT)
                    self.__page = 1
                elif event.key == ord('a'):
                    self.get_game().change_scene(Enums.Scene.AI_MK_IV_SIMULATOR)
                    self.__page = 1
                else:
                    pygame.mixer.stop()

                    if event.key == ord('c') or event.key == pygame.K_RETURN:
                        if self.__page == 1:
                            self.__page = 2
                        elif self.__page == 2:
                            self.__page = 3
                        elif self.__page == 3:
                            self.__page = 1
                    if event.key == pygame.K_LEFT:
                        if self.__page == 3:
                            self.__page = 2
                        elif self.__page == 2:
                            self.__page = 1
                        elif self.__page == 1:
                            self.__page = 3
                    if event.key == pygame.K_RIGHT:
                        if self.__page == 3:
                            self.__page = 1
                        elif self.__page == 2:
                            self.__page = 3
                        elif self.__page == 1:
                            self.__page = 2
                    self.start()

    def start(self):

        if self.__page == 1:
            self.__AI_MK4_EQUIPMENT_VOICE_Sound.play()
        elif self.__page == 2:
            self.__AI_MK4_RECEIVER_VOICE_Sound.play()
        elif self.__page == 3:
            self.__AI_MK4_INDICATOR_VOICE_Sound.play()

        Scene.start(self)

    def updateState(self):
         Scene.updateState(self)

    def renderPage1(self):

        self.add_text('THE EQUIPMENT', 148, 80, Colours.YELLOW, Colours.BLACK, 32)

        self.add_text('The AI Mk 4 was the first night fighter radar to enter service', 148, 120, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('in late 1940. It was introduced as a response to the change of', 148, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('tactics that the Germans had taken, in moving away from', 148, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('daylight raids to bombing at night. It was initially installed', 148, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('in Blenheims, but continued on, being installed in the', 148, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Beaufighter and even into the early Mosquitoes until later', 148, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('radars were developed. The radar transmitted 20uS', 148, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('pulses from an aerial fitted on the nose of the aircraft, in a', 148, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('wide forward beam and at a frequency of 195 MHz. Four', 148, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('receiving aerials, each with a relatively narrow beam, were', 148, 390, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('fitted on the wings, two facing outwards, one for port and', 148, 420, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('one for starboard, and the other two for elevation, all being', 148, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('at an angle of about 35 degrees to the centre line of the aircraft. Depending on the position of the target,', 148, 480, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('each aerial would receive a different signal level. The signal levels were displayed on the indicator unit', 148, 510, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('after passing though a receiver. The equipment was installed in the position normally occupied by the', 148, 540, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('rear gunner in the Blenheim. The operator sat facing the rear looking into the indicator, the receiver being', 148, 570, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('fitted vertically at the operator\'s side. Information as to the course that the pilot was to fly to intercept the', 148, 600, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('target was passed to the pilot via the intercom system.', 148, 630, Colours.YELLOW, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__AI_MK_IV_RECEIVER_Sprite, (728, 80))

    def renderPage2(self):

        self.add_text('THE RECEIVER (R3102A)', 148, 80, Colours.YELLOW, Colours.BLACK, 32)

        self.add_text('The receiver was a fairly conventional superhet with two RF', 148, 120, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('stages and a separate oscillator / mixer. Tuning over a limited', 148, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('range of +- 1MHz was by means of a variable inductor.', 148, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Normally four receivers would be required, one for each aerial', 148, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('but space and weight prevented this so that a two pole, 4 way', 148, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('motor driven switch was incorporated in the receiver that', 148, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('synchronously switched each aerial signal into the receiver,', 148, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('whilst at the same time switching the output to the', 148, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('appropriate channel of the indicator unit. Sequences of', 148, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('port / starboard / up / down signals were thus sent to the', 148, 390, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('indicator unit. The receiver also contained the power supply ', 148, 420, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('for the indicator unit.', 148, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 480, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 510, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 540, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 570, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 600, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 148, 630, Colours.YELLOW, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__AI_MK4_INDICATOR_Sprite, (728, 80))
        self.get_game().screen.blit(self.__AI_MK4_MIXER_Sprite, (728, 400))

    def renderPage3(self):
        self.add_text('THE INDICATOR UNIT (Type 48A)', 148, 80, Colours.YELLOW, Colours.BLACK, 32)

        self.add_text('The indicator unit contains two 3-inch cathode ray tubes, each tube', 148, 120, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('having an identical timebase scan. On the right hand tube the trace is', 148, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('vertical and used for displaying port/starboard signals whilst the left', 148, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('hand tube is for up and down aerial signals. The trace or timebase is', 148, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('initiated at the same time that the transmitter pulse occurs and the', 148, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('receiver pulses appear someway along the timebase depending on the', 148, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('range of the target. On the right-hand tube, port signals deflect the', 148, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('trace to the left, whilst the starboard signal deflects the trace to the', 148, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('right. A graticule, calibrated in miles, is fitted to the right hand tube', 148, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('only. Up / Down signals are treated in a similar manner on the left hand', 148, 390, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('tube. When the target is on-axis, the signal levels on either side of the two traces are equal. If the target is', 148, 420, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('off-axis, the signal level on that side will at first increase and then decrease if the target moves further', 148, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('off-axis still.', 148, 480, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Due to the low operating frequency (195 MHz), the aerials have limited directional capabilities, such that', 148, 510, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('strong echoes are received from the ground immediately below the aircraft. These die away with distance', 148, 540, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('but still swamp any target signals. This results in the range of the equipment being limited to the height', 148, 570, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('of the aircraft. The ground echo appears on the trace as a triangular shape, referred to as the "Christmas', 148, 600, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('tree effect" and occurring at a distance equal to the height of the aircraft. Some breakthrough of the', 148, 630, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('transmitter pulse also occurs at the beginning of the trace, limiting the minimum operating range, although', 148, 660, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('the system works down to a few hundred yards allowing visual contact by the pilot to be achieved.', 148, 690, Colours.YELLOW, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__AI_MK4_TRACE_Sprite, (828, 80))








                

