import pygame
import math, random
from Shared.Scene import *
from Shared.Colours import *
from Shared.Enums import *
from Shared.Constants import *

class AI_MK_IV_SimulatorScene(Scene):

    def __init__(self, game):
        Scene.__init__(self, game)
        self.__crossHairsSprite = pygame.image.load(Constants.CROSS_HAIRS)
        self.__AI_MK_IV_Sprite = pygame.image.load(Constants.AI_MK_IV_TRANSPARENT_512)
        self.__nightVisionFighterSprite = pygame.image.load(Constants.JU88_NIGHT_REAR)

        self.__maximumRange = 3.500
        self.__crossHairsCentre = (736, 275)
        self.__crossHairsRadius = 200
        self.__targetRange = self.__maximumRange
        self.__targetRadius = self.__crossHairsRadius
        self.__targetSize = [128.0, 25.0]
        self.__targetAngle = 45.0
        self.__targetAzEl = [45.0, 45.0]

        
        targetX = self.__targetRadius * math.cos(self.__targetAngle)
        targetY = self.__targetRadius * math.sin(self.__targetAngle)
        self.__targetPos = [self.__crossHairsCentre[0] + targetX, self.__crossHairsCentre[0] + targetY]



    def render(self):
       
        self.clearText()

        # Draw Title
        self.addText('AI MK IV Simulator!', 100, 50, Colours.GREEN, Colours.BLACK, 32)
        # Draw game description
        self.addText('Steer the aircraft using RADAR', 50, 150, Colours.GREEN, Colours.BLACK, 24) 
        self.addText('to intercept and destroy all threats!', 50, 175, Colours.GREEN, Colours.BLACK, 24) 
        # Draw Controls
        self.addText('Controls:', 50, 225, Colours.GREEN, Colours.BLACK, 24) 
        self.addText('UP = Increase elevation', 50, 250, Colours.GREEN, Colours.BLACK, 24) 
        self.addText('DOWN = Reduce elevation', 50, 275, Colours.GREEN, Colours.BLACK, 24) 
        self.addText('LEFT = Search left', 50, 300, Colours.GREEN, Colours.BLACK, 24) 
        self.addText('RIGHT = Search right', 50, 325, Colours.GREEN, Colours.BLACK, 24) 
        self.addText('Green button = Interrogate Friend or Foe', 50, 350, Colours.GREEN, Colours.BLACK, 24) 
        self.addText('Red Button = Fire', 50, 375, Colours.GREEN, Colours.BLACK, 24) 
        # Draw Options
        self.addText('Options:', 50, 425, Colours.GREEN, Colours.BLACK, 24) 
        self.addText('Green button = new game', 50, 450, Colours.GREEN, Colours.BLACK, 24) 
        self.addText('Red button = quit', 50, 475, Colours.GREEN, Colours.BLACK, 24) 


        # Draw AI MK IV image
        
        self.getGame().screen.blit(self.__AI_MK_IV_Sprite, (480, 550))

        self.addText('Target range (miles): ' + str(self.__targetRange), 460, 10, Colours.GREEN, Colours.BLACK, 16) 
        self.addText('Target azimuth (deg): ' + str(self.__targetAzEl[0]), 460, 25, Colours.GREEN, Colours.BLACK, 16) 
        self.addText('Target elevation (deg): ' + str(self.__targetAzEl[1]), 460, 40, Colours.GREEN, Colours.BLACK, 16) 

        fighterSpriteScaled = pygame.transform.scale(self.__nightVisionFighterSprite, (int(self.__targetSize[0]), int(self.__targetSize[1]))) 
        self.getGame().screen.blit(fighterSpriteScaled, (int(self.__targetPos[0] - fighterSpriteScaled.get_width()/2), int(self.__targetPos[1] - fighterSpriteScaled.get_height()/2)))

        self.getGame().screen.blit(self.__crossHairsSprite, (480, 20))
        
        self.DrawBackgroundNoise()

        Scene.render(self)
       
    def DrawBackgroundNoise(self):
        # Elevation tube
        for x in xrange(605, 692):
            linelength = random.randint(1,5)
            pygame.draw.aaline(self.getGame().screen, Colours.GREEN, (x, 649), (x, 649-linelength))
            pygame.draw.aaline(self.getGame().screen, Colours.GREEN, (x, 649), (x, 649+linelength))

        # Azimuth tube
        for y in xrange(592, 710):
            linelength = random.randint(1,5)
            pygame.draw.aaline(self.getGame().screen, Colours.GREEN, (820-linelength, y), (820, y))
            pygame.draw.aaline(self.getGame().screen, Colours.GREEN, (820+linelength, y), (820, y))

    def updateState(self):
         Scene.updateState(self)

         if self.__targetRange >= 0.5:
             self.__targetRange -= 0.001
         else:
             self.__targetRange = self.__maximumRange

         ratio = self.__targetRange / self.__maximumRange
         self.__targetRadius = ratio * self.__crossHairsRadius
         self.__targetSize[0] = (1 - ratio) * 386 + 125
         self.__targetSize[1] = (1 - ratio) * 75 + 25

         if self.__targetAngle >= 360:
             self.__targetAngle = 0
         else:
             self.__targetAngle += 0.01

         if self.__targetAngle >=0 and self.__targetAngle < 90: #TR quadrant
             self.__targetAzEl[0] = self.__targetAngle
             self.__targetAzEl[1] = 90 - self.__targetAngle
             targetX = self.__targetRadius * math.cos(self.__targetAzEl[0])
             targetY = self.__targetRadius * math.sin(self.__targetAzEl[0])
             self.__targetPos = [self.__crossHairsCentre[0] + targetX, self.__crossHairsCentre[1] + targetY]             
         elif self.__targetAngle >=90 and self.__targetAngle < 180: #BR quadrant
             self.__targetAzEl[0] = 180 - self.__targetAngle
             self.__targetAzEl[1] = 90 - self.__targetAngle
             targetX = self.__targetRadius * math.cos(self.__targetAzEl[0])
             targetY = self.__targetRadius * math.sin(self.__targetAzEl[0])
             self.__targetPos = [self.__crossHairsCentre[0] + targetX, self.__crossHairsCentre[1] + targetY]
         elif self.__targetAngle >=180 and self.__targetAngle < 270: #BL quadrant
             self.__targetAzEl[0] = 180 - self.__targetAngle
             self.__targetAzEl[1] = self.__targetAngle - 270
             targetX = self.__targetRadius * math.cos(self.__targetAzEl[0])
             targetY = self.__targetRadius * math.sin(self.__targetAzEl[0])
             self.__targetPos = [self.__crossHairsCentre[0] + targetX, self.__crossHairsCentre[1] + targetY]
         else: #TL quadrant
             self.__targetAzEl[0] = self.__targetAngle - 360
             self.__targetAzEl[1] = self.__targetAngle - 270
             targetX = self.__targetRadius * math.cos(self.__targetAzEl[0])
             targetY = self.__targetRadius * math.sin(self.__targetAzEl[0])
             self.__targetPos = [self.__crossHairsCentre[0] + targetX, self.__crossHairsCentre[1] + targetY]

         

    def handleEvents(self, events):
        Scene.handleEvents(self, events)

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.getGame().changeScene(Enums.Scene.FRONT)              
                if event.key == ord('c'):
                    self.getGame().changeScene(Enums.Scene.AI_MK_IV_GAME) 

