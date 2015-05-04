import time
from Shared.Scene import *
from Shared.Colours import *
from Shared.Constants import *

class AI_MK_X_InfoScene(Scene):
    def __init__(self, game=None):

        if game is not None:
            Scene.__init__(self, game)
            self.__AI_MK_X_1_Sprite = pygame.image.load(Constants.AI_MK_X_1)
            self.__AI_MK_X_2_Sprite = pygame.image.load(Constants.AI_MK_X_2)
            self.__AI_MK_X_3_Sprite = pygame.image.load(Constants.AI_MK_X_3)
            self.__AI_MK_X_Sprite = pygame.image.load(Constants.AI_MK_X)
            self.__greenButtonSprite = pygame.image.load(Constants.ARCADE_GREEN)
            self.__redButtonSprite = pygame.image.load(Constants.ARCADE_RED)
            self.__blueButtonSprite = pygame.image.load(Constants.ARCADE_BLUE)

        self.__page = 1

    def render(self):

        self.clear_text()

        # Draw Title
        self.add_text('AI MK X Airbourne Interception RADAR', 350, 20, Colours.YELLOW, Colours.BLACK, 40)

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
            pass #self.__AI_MK4_VOICE_Sound.play()

        Scene.start(self)

    def updateState(self):
         Scene.updateState(self)

    def renderPage1(self):

        self.add_text('THE EQUIPMENT', 60, 80, Colours.YELLOW, Colours.BLACK, 32)

        self.add_text('The AI MK X is a modified version of the American SCR 720 Radar. It required a two man crew,', 60, 120, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('the operator giving instructions to the pilot over the intercom. It was used in aircraft like the', 60, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Mosquito for nightfighter operations. The system radiates 0.75 microsecond pulses in the ', 60, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('centimetric band at 9.1 cms. The peak power being approximately 70 KW. The aerial system,', 60, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('housed in a Perspex dome on the nose of the aircraft, consists of a small vertical dipole at the', 60, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('centre of a parabolic dish, the dipole being used for both transmission and reception.', 60, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The first British designed centimetric AI radar was the AI MK VII / MK VIII. This had a similar performance to the MK X, although', 60, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('the scanning and display methods differ considerably. A British MK IX system was also developed that was more sophisticated, as', 60, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('it had \'lock and follow\' capabilities, but problems in meeting production quantities and timescales required prevented it from', 60, 390, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('being adopted, and the American MK X was used instead.', 60, 420, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The MK VIII scanning system was what is termed a \'spiral scan\'. In this system the dish is rotated about its axis and gradually', 60, 480, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('deflected sideways, tracing out a spiral in the sky, out to an angle of about 45 degrees, The deflection then returns slowly to the ', 60, 510, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('zero position when the process is repeated.', 60, 540, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 570, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 600, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 630, Colours.YELLOW, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__AI_MK_X_Sprite, (950, 110))

    def renderPage2(self):

        self.add_text('THE EQUIPMENT (continued)', 60, 80, Colours.YELLOW, Colours.BLACK, 32)

        self.add_text('In the MK X, the parabolic dish is rotated continually about its vertical axis. It is also slowly', 60, 120, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('tilted up and down, which effectively traces out a helix in the sky, much like looking out from the', 60, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('centre of a coil spring. The rear half of the scan, some 210 degrees, is blanked off, as its field', 60, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('of view is interrupted by the structure of the aircraft. The presentation of the information', 60, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('to the operator is also different. In the MK VIII, a single tube with a circular display was used.', 60, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The target range is measured from the centre of the tube with the target appearing as a segment of a circle, its angular position ', 60, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('defining the azimuth and elevation and the length of the segment showing how much the target is off axis. As the target', 60, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('approached the axis of the aircraft, the segment gradually extended to a full circle.', 60, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The MK X has two tubes, the left one or the \'C\' scope displaying the target as a spot on an azimuth / elevation grid. The right one', 60, 390, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('or the \'B\' tube has again an azimuth calibration on the horizontal axis but the vertical axis shows the range of the target. A range', 60, 420, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('marker line, adjustable by the operator, can be moved up and down the trace to select a particular target. Only when this marker', 60, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('line overlays the target does the target appear on the left hand \'C\' tube. The amount of vertical scanning or tilt can be selected', 60, 480, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('by the operator and has 5 switched ranges. The maximum scan is +40 degrees to -20 degrees down to -5 degrees to +10 degrees.', 60, 510, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('A fixed -5 degrees is used when homing onto a beacon. The range can also be selected from 2 miles, 5 miles, 10 miles up to 100', 60, 540, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('miles for use with a homing beacon.', 60, 570, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 600, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The beam width is some 10 degrees, with a vertical rotation speed of 360 RPM (100 rpm for the beacon range). There are 12 ', 60, 630, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('scan lines up and 12 down for the +40/-20 degree range, giving a full scan time of 4 seconds.', 60, 660, Colours.YELLOW, Colours.BLACK, 28)

        self.get_game().screen.blit(self.__AI_MK_X_Sprite, (950, 110))

    def renderPage3(self):
        self.add_text('THE INDICATOR UNIT', 60, 80, Colours.YELLOW, Colours.BLACK, 32)

        self.add_text('This first picture shows the front panel of the Indicator unit with the two', 60, 120, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('tubes. The controls are for the display only and consist of brightness, focus,', 60, 150, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('X & Y shifts for each tube, plus a graticule brightness control. The brightness', 60, 180, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('on this display has been increased to show the scan lines. The brightness', 60, 210, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('would normally be turned low such that only the target spot would be seen.', 60, 240, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The resolution, due to the limited number of scan lines is low and the target', 60, 270, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('spot can appear on two elevation scan lines at the same time.', 60, 300, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 330, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The second picture shows details of the LH Azimuth / Elevation display.', 60, 360, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 390, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The third picture is the RH Range/Azimuth tube showing the Range Marker', 60, 420, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Bar and two simulated targets. The Range Marker Bar is just intercepting', 60, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('the second target, the spot of which can just be seen on the LH tube.', 60, 480, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('Electronic noise has been added to this trace to give it a realistic effect. ', 60, 510, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('The two targets can be moved independently in all three axis i.e. range,', 60, 540, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('azimuth and elevation controls from the simulator control box.', 60, 570, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 600, Colours.YELLOW, Colours.BLACK, 28)
        self.add_text('', 60, 630, Colours.YELLOW, Colours.BLACK, 28)

        self.add_text('1', 778, 80, Colours.YELLOW, Colours.BLACK, 28)
        self.get_game().screen.blit(self.__AI_MK_X_1_Sprite, (778, 110))
        self.add_text('2', 778, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.get_game().screen.blit(self.__AI_MK_X_2_Sprite, (778, 480))
        self.add_text('3', 1028, 450, Colours.YELLOW, Colours.BLACK, 28)
        self.get_game().screen.blit(self.__AI_MK_X_3_Sprite, (1028, 480))










                

