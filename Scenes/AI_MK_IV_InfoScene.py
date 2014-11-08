from Shared.Scene import *
from Shared.Colours import *
from Shared.Constants import *

class AI_MK_IV_InfoScene(Scene):

    def __init__(self, game):
        Scene.__init__(self, game)
        self.__page = 1
        self.__AI_MK_IV_RECEIVER_Sprite = pygame.image.load(Constants.AI_MK4_RECEIVER)
        self.__AI_MK4_INDICATOR_Sprite = pygame.image.load(Constants.AI_MK4_INDICATOR)
        self.__AI_MK4_TRACE_Sprite = pygame.image.load(Constants.AI_MK4_TRACE)


    def render(self):
       
        self.clearText()

        # Draw Title
        self.addText('AI MK IV Airbourne Interception RADAR', 270, 20, Colours.GREEN, Colours.BLACK, 40)

        # Draw page body
        if self.__page == 1:
            self.renderPage1()
        elif self.__page == 2:
            self.renderPage2()
        elif self.__page == 3:
            self.renderPage3()

        # Draw footer
        self.addText('Green button: find out more | Blue button: home | Red button: simulation', 130, 720, Colours.GREEN, Colours.BLACK, 32)

        Scene.render(self)

        
    def handleEvents(self, events):
        Scene.handleEvents(self, events)

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.getGame().changeScene(Enums.Scene.FRONT)
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
                if event.key == ord('a'):
                    self.getGame().changeScene(Enums.Scene.AI_MK_IV_SIMULATOR)

    def updateState(self):
         Scene.updateState(self)

    def renderPage1(self):

        self.addText('THE EQUIPMENT', 20, 80, Colours.GREEN, Colours.BLACK, 32)

        self.addText('This was the first night fighter RADAR to enter service in', 20, 120, Colours.GREEN, Colours.BLACK, 28)
        self.addText('late 1940. It was introduced as a response to the change of', 20, 150, Colours.GREEN, Colours.BLACK, 28)
        self.addText('tactics that the Germans had taken, in moving away from', 20, 180, Colours.GREEN, Colours.BLACK, 28)
        self.addText('daylight raids to bombing at night. It was initially installed', 20, 210, Colours.GREEN, Colours.BLACK, 28)
        self.addText('in Blenheims but continued on, being installed in the', 20, 240, Colours.GREEN, Colours.BLACK, 28)
        self.addText('Beaufighter and even into the early Mosquitoes until later', 20, 270, Colours.GREEN, Colours.BLACK, 28)
        self.addText('RADARs were developed. The RADAR transmitted 20uS', 20, 300, Colours.GREEN, Colours.BLACK, 28)
        self.addText('pulses from an aerial fitted on the nose of the aircraft, in a', 20, 330, Colours.GREEN, Colours.BLACK, 28)
        self.addText('wide forward beam and at a frequency of 195 MHz. Four', 20, 360, Colours.GREEN, Colours.BLACK, 28)
        self.addText('receiving aerials, each with a relatively narrow beam were', 20, 390, Colours.GREEN, Colours.BLACK, 28)
        self.addText('fitted on the wings, two facing outwards one for port and', 20, 420, Colours.GREEN, Colours.BLACK, 28)
        self.addText('one for starboard and the other two for up and down', 20, 450, Colours.GREEN, Colours.BLACK, 28)
        self.addText('directions, all being at an angle of about 35 degrees to the centre line of the aircraft. Depending on the', 20, 480, Colours.GREEN, Colours.BLACK, 28)
        self.addText('position of the target, each aerial would receive a different signal level. The signal levels were displayed', 20, 510, Colours.GREEN, Colours.BLACK, 28)
        self.addText('on the indicator unit after passing though a receiver. The equipment was installed in the position normally', 20, 540, Colours.GREEN, Colours.BLACK, 28)
        self.addText('occupied by the rear gunner in the Blenheim. The operator sat facing the rear looking into the indicator,', 20, 570, Colours.GREEN, Colours.BLACK, 28)
        self.addText('the receiver being fitted vertically at the operator\'s side. Information as to the course that the pilot was to', 20, 600, Colours.GREEN, Colours.BLACK, 28)
        self.addText('fly to intercept the target was passed to the pilot via the intercom system.', 20, 630, Colours.GREEN, Colours.BLACK, 28)

        self.getGame().screen.blit(self.__AI_MK_IV_RECEIVER_Sprite, (600, 80))


    def renderPage2(self):

        self.addText('THE RECEIVER (R3102A)', 20, 80, Colours.GREEN, Colours.BLACK, 32)

        self.addText('The receiver was a fairly conventional superhet with two RF', 20, 120, Colours.GREEN, Colours.BLACK, 28)
        self.addText('stages and a separate oscillator / mixer. Tuning over a limited', 20, 150, Colours.GREEN, Colours.BLACK, 28)
        self.addText('range of +- 1MHz was by means of a variable inductor.', 20, 180, Colours.GREEN, Colours.BLACK, 28)
        self.addText('Normally four receivers would be required, one for each aerial', 20, 210, Colours.GREEN, Colours.BLACK, 28)
        self.addText('but space and weight prevented this so that a two pole, 4 way', 20, 240, Colours.GREEN, Colours.BLACK, 28)
        self.addText('motor driven switch was incorporated in the receiver that', 20, 270, Colours.GREEN, Colours.BLACK, 28)
        self.addText('synchronously switched each aerial signal into the receiver', 20, 300, Colours.GREEN, Colours.BLACK, 28)
        self.addText('whilst at the same time switching the output to the', 20, 330, Colours.GREEN, Colours.BLACK, 28)
        self.addText('appropriate channel of the indicator unit. Sequences of', 20, 360, Colours.GREEN, Colours.BLACK, 28)
        self.addText('port / starboard / up / down signals were thus sent to the', 20, 390, Colours.GREEN, Colours.BLACK, 28)
        self.addText('indicator unit. The receiver also contained the power supplies for the indicator unit.', 20, 420, Colours.GREEN, Colours.BLACK, 28)
        self.addText('', 20, 450, Colours.GREEN, Colours.BLACK, 28)
        self.addText('', 20, 480, Colours.GREEN, Colours.BLACK, 28)
        self.addText('', 20, 510, Colours.GREEN, Colours.BLACK, 28)
        self.addText('', 20, 540, Colours.GREEN, Colours.BLACK, 28)
        self.addText('', 20, 570, Colours.GREEN, Colours.BLACK, 28)
        self.addText('', 20, 600, Colours.GREEN, Colours.BLACK, 28)
        self.addText('', 20, 630, Colours.GREEN, Colours.BLACK, 28)

        self.getGame().screen.blit(self.__AI_MK4_INDICATOR_Sprite, (600, 80))



    def renderPage3(self):
        self.addText('THE INDICATOR UNIT (Type 48A)', 20, 80, Colours.GREEN, Colours.BLACK, 32)

        self.addText('The indicator unit contains two 3-inch cathode ray tubes, each tube', 20, 120, Colours.GREEN, Colours.BLACK, 28)
        self.addText('having an identical timebase scan. On the right hand tube the trace is', 20, 150, Colours.GREEN, Colours.BLACK, 28)
        self.addText('vertical and used for displaying port/starboard signals whilst the left', 20, 180, Colours.GREEN, Colours.BLACK, 28)
        self.addText('hand tube is for up and down aerial signals. The trace or timebase is', 20, 210, Colours.GREEN, Colours.BLACK, 28)
        self.addText('initiated at the same time that the transmitter pulse occurs and the', 20, 240, Colours.GREEN, Colours.BLACK, 28)
        self.addText('receiver pulses appear someway along the timebase depending on the', 20, 270, Colours.GREEN, Colours.BLACK, 28)
        self.addText('range of the target. On the right-hand tube, port signals deflect the', 20, 300, Colours.GREEN, Colours.BLACK, 28)
        self.addText('trace to the left whilst the starboard signal deflects the trace to the', 20, 330, Colours.GREEN, Colours.BLACK, 28)
        self.addText('right. A graticule, calibrated in miles, is fitted to the right hand tube', 20, 360, Colours.GREEN, Colours.BLACK, 28)
        self.addText('only. Up / Down signals are treated in a similar manner on the left hand', 20, 390, Colours.GREEN, Colours.BLACK, 28)
        self.addText('tube. When the target is on axis the signal levels on either side of the two traces are equal. If the target is', 20, 420, Colours.GREEN, Colours.BLACK, 28)
        self.addText('off axis the signal level on that side will at first increase and then decrease if the target moves further', 20, 450, Colours.GREEN, Colours.BLACK, 28)
        self.addText('off axis still.', 20, 480, Colours.GREEN, Colours.BLACK, 28)
        self.addText('Due to the low operating frequency (195 MHz) the aerials have limited directional capabilities such that', 20, 510, Colours.GREEN, Colours.BLACK, 28)
        self.addText('strong echoes are received from the ground immediately below the aircraft. These die away with distance', 20, 540, Colours.GREEN, Colours.BLACK, 28)
        self.addText('but still swamp any target signals. This results in the range of the equipment being limited to the height', 20, 570, Colours.GREEN, Colours.BLACK, 28)
        self.addText('of the aircraft. The ground echo appears on the trace as a triangular shape, referred to as the "Christmas', 20, 600, Colours.GREEN, Colours.BLACK, 28)
        self.addText('tree effect" and occurring at a distance equal to the height of the aircraft. Some breakthrough of the', 20, 630, Colours.GREEN, Colours.BLACK, 28)
        self.addText('transmitter pulse also occurs at the beginning of the trace, limiting the minimum operating range, although', 20, 660, Colours.GREEN, Colours.BLACK, 28)
        self.addText('the system works down to a few hundred yards allowing visual contact by the pilot to be achieved.', 20, 690, Colours.GREEN, Colours.BLACK, 28)

        self.getGame().screen.blit(self.__AI_MK4_TRACE_Sprite, (700, 80))








                

