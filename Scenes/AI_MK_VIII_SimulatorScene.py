from Shared.Scene import *
from Shared.Colours import *

class AI_MK_VIII_SimulatorScene(object):

    def __init__(self, surface):
        self.surface = surface

    def Show(self):
        self.Draw()
        return self.HandleEvents()

    def Draw(self):
        # First, fill the whole screen with black
        self.surface.fill(BLACK)

        # Draw Title
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('AI MK VIII Airbourne Interception Radar', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (275, 20)
        self.surface.blit(textSurfaceObj, textRectObj)

        # First paragraph
        fontObj = pygame.font.Font('freesansbold.ttf', 16)
        
        textSurfaceObj = fontObj.render('The AI Mk7/8 was the first centimetric Airborne Interception Radar, appearing in about 1942/43 and installed in', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER + 20, 70)
        self.surface.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render('Beaufighters and Mosquitoes. The earlier AI MK4 only worked at a frequency of 200 MHz. Gone are the multiple aerials', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER + 20, 90)
        self.surface.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render('all to be replaced by a single transmit/receive aerial mounted at the centre of the radar dish. The dish is mounted', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER + 20, 110)
        self.surface.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render('in the nose of the aircraft behind a transparent cover. At 10cms(3000MHz) the radar beam is much narrower, almost', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER + 20, 130)
        self.surface.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render('operating like a torch beam, and thus the radar beam can be made to sweep around the sky looking for a target.', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER + 20, 150)
        self.surface.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render('The dish is used to focus the beam and point it in the required direction. The dish is spun on its axis and ', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER + 20, 170)
        self.surface.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render('initially the beam is directed forwards. The dish is then progressively turned "off axis" thus sweeping a ', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER + 20, 190)
        self.surface.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render('spiral in the sky in front of the aircraft. When it reaches a maximum spiral outwards it returns to the', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER + 20, 210)
        self.surface.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render('centre on an inwards spiral. The whole process is repeated continuously.', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER + 20, 230)
        self.surface.blit(textSurfaceObj, textRectObj)

        # First image
        RXMK8_Img = pygame.image.load('Images/RXMK8.jpg')
        self.surface.blit(RXMK8_Img, (DISPLAYBORDER + 20, 270))

        # Second image
        RXMK8_Img = pygame.image.load('Images/INDMK8.jpg')
        self.surface.blit(RXMK8_Img, (DISPLAYBORDER + 300, 270))

        # Remaining text from the website commented out unless and until needed
        
        #textSurfaceObj = fontObj.render('The AI MK8 Receiver contains the Klystron, the unit that protrudes from the front of the receiver and can be', True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (DISPLAYBORDER + 20, 430)
        #self.surface.blit(textSurfaceObj, textRectObj)
        #textSurfaceObj = fontObj.render('removed as an assembly. The Klystron is used as a local oscillator in conjunction with the Magnetron, the main radar pulse generator.', True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (DISPLAYBORDER + 20, 450)
        #self.surface.blit(textSurfaceObj, textRectObj)

        # Third paragraph        
        #textSurfaceObj = fontObj.render('AI MK8 Indicator Unit has the central single CRT the operation of which can be seen on the animation simulation as follows', True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (DISPLAYBORDER + 20, 470)
        #self.surface.blit(textSurfaceObj, textRectObj)

        # Third image
        #RXMK8_Img = pygame.image.load('Images/MK8Animation.gif')
        #self.surface.blit(RXMK8_Img, (DISPLAYBORDER + 20, 490))
 
        #<U>Demonstration animation of a Night Fighter AI MK8 (Airborne Interception) radar.</U>
        #<P> The radar screen is the green circle on the left and the target aircraft simulation appears on the right.
        #The target aircraft at night is invisible to the pilot until the target is within a few hundred yards of the night fighter and the pilot is directed onto the target by information given to him by the radar operator from the information on his radar screen
        #The target echo appears on the radar screen as a yellow arc of a circle. In practice the screen is just one colour (green) but in this animation it has been changed to yellow to make the echo easier to identify. The distance of the arc from the centre of the screen is proportional to the distance that the target is in front of the night fighter. The direction of the echo indicates the direction of the target (up, down, left or right) and the length of the arc tells the operator how far the target is 'off axis', When the target is 'dead on axis' the target echo becomes a complete circle. The band of noise at the bottom of the radar screen is an echo due to reflection from the ground, below and forward of the aircraft. when the beam sweeps downwards.


        textSurfaceObj = fontObj.render('Press any button to return to start screen.', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER + 20, 450)
        self.surface.blit(textSurfaceObj, textRectObj)
        
        pygame.display.update()
        
    def HandleEvents(self):
        global SELECTED_OPTION
        
        # Wait forever until the user enters something we can use
        while True:
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT or \
                    (event.type == KEYUP and event.key == K_ESCAPE) or \
                    (event.type == KEYUP and event.key == ord('a')) or \
                    (event.type == KEYUP and event.key == ord('b')) or \
                    (event.type == KEYUP and event.key == ord('c')) :
                    return InfoScreenResult.QUIT                 
                










                

