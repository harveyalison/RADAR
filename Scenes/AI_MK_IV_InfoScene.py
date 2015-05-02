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
            self.__AI_MK4_VOICE_Sound = pygame.mixer.Sound(Constants.AI_MK4_VOICE)

        self.__page = 1

    def render(self):
       
        self.clear_text()

        # Draw Title
        self.add_text('AI MK IV Airbourne Interception RADAR', 270, 20, Colours.GREEN, Colours.BLACK, 40)

        # Draw page body
        if self.__page == 1:
            self.renderPage1()
        elif self.__page == 2:
            self.renderPage2()
        elif self.__page == 3:
            self.renderPage3()

        # Draw footer
        self.add_text('Green button: find out more | Blue button: home | Red button: simulation', 130, 720, Colours.GREEN, Colours.BLACK, 32)

        Scene.render(self)

    def handle_events(self, events):
        Scene.handle_events(self, events)

        for event in events:
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_ESCAPE or event.key == ord('b'):
                    self.get_game().change_scene(Enums.Scene.FRONT)
                elif event.key == ord('a'):
                    self.get_game().change_scene(Enums.Scene.AI_MK_IV_SIMULATOR)
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
            self.__AI_MK4_VOICE_Sound.play()

        Scene.start(self)

    def updateState(self):
         Scene.updateState(self)

    def renderPage1(self):

        self.add_text('THE EQUIPMENT', 20, 80, Colours.GREEN, Colours.BLACK, 32)

        self.add_text('The AI Mk 4 was the first night fighter Radar to enter service', 20, 120, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('in late 1940. It was introduced as a response to the change of', 20, 150, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('tactics that the Germans had taken, in moving away from', 20, 180, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('daylight raids to bombing at night. It was initially installed', 20, 210, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('in Blenheims, but continued on, being installed in the', 20, 240, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('Beaufighter and even into the early Mosquitoes until later', 20, 270, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('Radars were developed. The Radar transmitted 20uS', 20, 300, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('pulses from an aerial fitted on the nose of the aircraft, in a', 20, 330, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('wide forward beam and at a frequency of 195 MHz. Four', 20, 360, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('receiving aerials, each with a relatively narrow beam, were', 20, 390, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('fitted on the wings, two facing outwards, one for port and', 20, 420, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('one for starboard, and the other two for elevation, all being', 20, 450, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('at an angle of about 35 degrees to the centre line of the aircraft. Depending on the position of the target,', 20, 480, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('each aerial would receive a different signal level. The signal levels were displayed on the indicator unit', 20, 510, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('after passing though a receiver. The equipment was installed in the position normally occupied by the', 20, 540, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('rear gunner in the Blenheim. The operator sat facing the rear looking into the indicator, the receiver being', 20, 570, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('fitted vertically at the operator\'s side. Information as to the course that the pilot was to fly to intercept the', 20, 600, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('target was passed to the pilot via the intercom system.', 20, 630, Colours.GREEN, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__AI_MK_IV_RECEIVER_Sprite, (600, 80))

    def renderPage2(self):

        self.add_text('THE RECEIVER (R3102A)', 20, 80, Colours.GREEN, Colours.BLACK, 32)

        self.add_text('The receiver was a fairly conventional superhet with two RF', 20, 120, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('stages and a separate oscillator / mixer. Tuning over a limited', 20, 150, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('range of +- 1MHz was by means of a variable inductor.', 20, 180, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('Normally four receivers would be required, one for each aerial', 20, 210, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('but space and weight prevented this so that a two pole, 4 way', 20, 240, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('motor driven switch was incorporated in the receiver that', 20, 270, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('synchronously switched each aerial signal into the receiver,', 20, 300, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('whilst at the same time switching the output to the', 20, 330, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('appropriate channel of the indicator unit. Sequences of', 20, 360, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('port / starboard / up / down signals were thus sent to the', 20, 390, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('indicator unit. The receiver also contained the power supply ', 20, 420, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('for the indicator unit.', 20, 450, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('', 20, 480, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('', 20, 510, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('', 20, 540, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('', 20, 570, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('', 20, 600, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('', 20, 630, Colours.GREEN, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__AI_MK4_INDICATOR_Sprite, (600, 80))
        self.get_game().screen.blit(self.__AI_MK4_MIXER_Sprite, (600, 400))

    def renderPage3(self):
        self.add_text('THE INDICATOR UNIT (Type 48A)', 20, 80, Colours.GREEN, Colours.BLACK, 32)

        self.add_text('The indicator unit contains two 3-inch cathode ray tubes, each tube', 20, 120, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('having an identical timebase scan. On the right hand tube the trace is', 20, 150, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('vertical and used for displaying port/starboard signals whilst the left', 20, 180, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('hand tube is for up and down aerial signals. The trace or timebase is', 20, 210, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('initiated at the same time that the transmitter pulse occurs and the', 20, 240, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('receiver pulses appear someway along the timebase depending on the', 20, 270, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('range of the target. On the right-hand tube, port signals deflect the', 20, 300, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('trace to the left, whilst the starboard signal deflects the trace to the', 20, 330, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('right. A graticule, calibrated in miles, is fitted to the right hand tube', 20, 360, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('only. Up / Down signals are treated in a similar manner on the left hand', 20, 390, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('tube. When the target is on-axis, the signal levels on either side of the two traces are equal. If the target is', 20, 420, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('off-axis, the signal level on that side will at first increase and then decrease if the target moves further', 20, 450, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('off-axis still.', 20, 480, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('Due to the low operating frequency (195 MHz), the aerials have limited directional capabilities, such that', 20, 510, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('strong echoes are received from the ground immediately below the aircraft. These die away with distance', 20, 540, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('but still swamp any target signals. This results in the range of the equipment being limited to the height', 20, 570, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('of the aircraft. The ground echo appears on the trace as a triangular shape, referred to as the "Christmas', 20, 600, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('tree effect" and occurring at a distance equal to the height of the aircraft. Some breakthrough of the', 20, 630, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('transmitter pulse also occurs at the beginning of the trace, limiting the minimum operating range, although', 20, 660, Colours.GREEN, Colours.BLACK, 28)
        self.add_text('the system works down to a few hundred yards allowing visual contact by the pilot to be achieved.', 20, 690, Colours.GREEN, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__AI_MK4_TRACE_Sprite, (700, 80))








                

