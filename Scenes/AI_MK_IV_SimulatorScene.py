import math
import random

from Shared.Scene import *
from Shared.Colours import *
from Shared.Enums import *
from Shared.Constants import *


class AI_MK_IV_SimulatorScene(Scene):

    def __init__(self, game=None):

        if game is not None:
            Scene.__init__(self, game)
            self.__crossHairsSprite = pygame.image.load(Constants.CROSS_HAIRS)
            self.__AI_MK_IV_Sprite = pygame.image.load(Constants.AI_MK_IV_TRANSPARENT_512)
            self.__nightVisionFighterSprite = pygame.image.load(Constants.JU88_NIGHT_REAR)
            self.__explosionSprite = pygame.image.load(Constants.EXPLOSION)

        self.__maximumRange = 3.500
        self.__crossHairsCentre = (736, 275)
        self.__crossHairsRadius = 200
        self.__shooting = False

        self.reset()

    def render(self):
       
        self.clear_text()

        # Draw Title
        self.add_text('AI MK IV Simulator!', 30, 30, Colours.GREEN, Colours.BLACK, 32)

        # Draw simulation information
        self.add_text('The pilot can see nothing of the target until he is within', 30, 80, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('a few hundred yards, and must identify the target', 30, 110, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('aircraft visually as \'an enemy\' before opening fire.', 30, 140, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('The left hand screen tells the RADAR operator if the', 30, 170, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('target is above or below him. This is known as the', 30, 200, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('\'elevation\'. In practice the RADAR screen is all', 30, 230, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('green and the echo is not easily seen, but for', 30, 260, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('demonstration purposes the target echo is shown', 30, 290, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('yellow. The \'Christmas tree\' noise is due to', 30, 320, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('reflections from the ground immediately below and', 30, 350, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('forward of the aircraft. Targets are lost in this noise', 30, 380, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('and the range is therefore limited to the height of the', 30, 410, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('aircraft. The RADAR operator gives verbal instructions', 30, 440, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('to the pilot to bring the aircraft on the correct course', 30, 470, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('for interception, when the echoes on both screens are', 30, 500, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('equi-distant either side of the axis. The right hand', 30, 530, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('screen is similar to the elevation display, but shows', 30, 560, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('the operator whether the target is to the left or right.', 30, 590, Colours.GREEN, Colours.BLACK, 24)
        self.add_text('This is known as the \'azimuth\'.', 30, 620, Colours.GREEN, Colours.BLACK, 24)
        # Draw Options
        self.add_text('Green button: new game | Blue button: home', 30, 680, Colours.GREEN, Colours.BLACK, 24)

        # Draw AI MK IV image
        self.get_game().screen.blit(self.__AI_MK_IV_Sprite, (480, 550))

        self.add_text('Target range (miles): ' + str(self.__targetRange), 460, 10, Colours.GREEN, Colours.BLACK, 16)
        self.add_text('Target azimuth (deg): ' + str(int(self.__targetAzEl[0])), 460, 25, Colours.GREEN, Colours.BLACK, 16)
        self.add_text('Target elevation (deg): ' + str(int(self.__targetAzEl[1])), 460, 40, Colours.GREEN, Colours.BLACK, 16)

        fighterSpriteScaled = pygame.transform.scale(self.__nightVisionFighterSprite, (int(self.__targetSize[0]), int(self.__targetSize[1]))) 
        self.get_game().screen.blit(fighterSpriteScaled, (int(self.__targetPos[0] - fighterSpriteScaled.get_width()/2), int(self.__targetPos[1] - fighterSpriteScaled.get_height()/2)))




        # Draw shooting and explosion, if required
        if self.__shooting:
            self.get_game().screen.blit(self.__explosionSprite, (self.__crossHairsCentre[0] - self.__explosionSprite.get_width()/2,self.__crossHairsCentre[1] - self.__explosionSprite.get_height()/2))

        self.get_game().screen.blit(self.__crossHairsSprite, (480, 20))
        
        self.drawBackgroundNoise()

        # Draw el tube line

        rangeratio = self.__targetRange / self.__maximumRange
        rangex = 595 + (rangeratio * 87)

        rangeytop = 0.0
        rangeybot = 0.0

        if self.__targetAzEl[1] < 0:
            rangeytop = 639.0
            rangeybot = 659.0 - self.__targetAzEl[1]/2
        else:
            rangeytop = 639.0 - self.__targetAzEl[1]/2
            rangeybot = 659.0

        pygame.draw.aaline(self.get_game().screen, Colours.YELLOW, (rangex, rangeytop), (rangex, rangeybot))

        # Draw az tube line

        rangey = 720 - (rangeratio * 118)

        rangexleft = 0.0
        rangexright = 0.0

        if self.__targetAzEl[0] < 0:
            rangexleft = 810 + self.__targetAzEl[0]/2.5
            rangexright = 830
        else:
            rangexleft = 810
            rangexright = 830 + self.__targetAzEl[0]/2.5

        pygame.draw.aaline(self.get_game().screen, Colours.YELLOW, (rangexleft, rangey), (rangexright, rangey))

        Scene.render(self)
       
    def drawBackgroundNoise(self):
        # Elevation tube
        for x in xrange(605, 692):
            linelength = random.randint(1,5)
            pygame.draw.aaline(self.get_game().screen, Colours.GREEN, (x, 649), (x, 649-linelength))
            pygame.draw.aaline(self.get_game().screen, Colours.GREEN, (x, 649), (x, 649+linelength))

        # Azimuth tube
        for y in xrange(592, 710):
            linelength = random.randint(1,5)
            pygame.draw.aaline(self.get_game().screen, Colours.GREEN, (820-linelength, y), (820, y))
            pygame.draw.aaline(self.get_game().screen, Colours.GREEN, (820+linelength, y), (820, y))

    def updateTargetRange(self):
        if self.__targetRange >= 0.5:
            self.__targetRange -= 0.005
        else:
            self.__targetRange = self.__maximumRange

    def reset(self):
        self.__targetRange = self.__maximumRange
        self.__targetRadius = self.__crossHairsRadius
        self.__targetSize = [128.0, 25.0]
        self.__targetRange = self.__maximumRange
        self.__targetAzEl = [45.0, 45.0]
        self.__targetAngle = 45.0
        targetX = self.__targetRadius * math.cos(math.radians(self.__targetAngle))
        targetY = self.__targetRadius * math.sin(math.radians(self.__targetAngle))
        self.__targetPos = [self.__crossHairsCentre[0] + targetX, self.__crossHairsCentre[1] - targetY]

    def updateState(self):
         Scene.updateState(self)

         if self.__shooting:
             self.__shootingCounter += 1
             if self.__shootingCounter >= 200:
                 self.__shooting = False
                 self.reset()
             return

         elif self.__targetRadius <= 30:
             self.__shooting = True
             self.__shootingCounter = 0


         self.updateTargetRange()

         ratio = self.__targetRange / self.__maximumRange

         self.__targetSize[0] = (1 - ratio) * 386 + 125
         self.__targetSize[1] = (1 - ratio) * 75 + 25

         self.__targetRadius = ratio * self.__crossHairsRadius

         if self.__targetAngle >= 360:
             self.__targetAngle = 0
         else:
             self.__targetAngle += 0.5


         if self.__targetAngle >=0 and self.__targetAngle < 90: #TR quadrant
             azpx = self.__targetRadius * math.cos(math.radians(90 - self.__targetAngle))
             elpx = self.__targetRadius * math.sin(math.radians(90 - self.__targetAngle))
             self.__targetAzEl[0] = azpx / self.__crossHairsRadius * 90
             self.__targetAzEl[1] = elpx / self.__crossHairsRadius * 90
             self.__targetPos = [self.__crossHairsCentre[0] + azpx, self.__crossHairsCentre[1] - elpx]
         elif self.__targetAngle >=90 and self.__targetAngle < 180: #BR quadrant
             azpx = self.__targetRadius * math.cos(math.radians(self.__targetAngle - 90))
             elpx = -1 * self.__targetRadius * math.sin(math.radians(self.__targetAngle - 90))
             self.__targetAzEl[0] = azpx / self.__crossHairsRadius * 90
             self.__targetAzEl[1] = elpx / self.__crossHairsRadius * 90
             self.__targetPos = [self.__crossHairsCentre[0] + azpx, self.__crossHairsCentre[1] - elpx]
         elif self.__targetAngle >=180 and self.__targetAngle < 270: #BL quadrant
             azpx = self.__targetRadius * math.cos(math.radians(self.__targetAngle - 90))
             elpx = -1 * self.__targetRadius * math.sin(math.radians(self.__targetAngle - 90))
             self.__targetAzEl[0] = azpx / self.__crossHairsRadius * 90
             self.__targetAzEl[1] = elpx / self.__crossHairsRadius * 90
             self.__targetPos = [self.__crossHairsCentre[0] + azpx, self.__crossHairsCentre[1] - elpx]
         else: #TL quadrant
             azpx = -1 * self.__targetRadius * math.cos(math.radians(self.__targetAngle - 270))
             elpx = self.__targetRadius * math.sin(math.radians(self.__targetAngle - 270))
             self.__targetAzEl[0] = azpx / self.__crossHairsRadius * 90
             self.__targetAzEl[1] = elpx / self.__crossHairsRadius * 90
             self.__targetPos = [self.__crossHairsCentre[0] + azpx, self.__crossHairsCentre[1] - elpx]

    def handle_events(self, events):
        Scene.handle_events(self, events)

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE or event.key == ord('b'):
                    self.get_game().change_scene(Enums.Scene.FRONT)
                if event.key == ord('c'):
                    self.get_game().change_scene(Enums.Scene.AI_MK_IV_GAME)

