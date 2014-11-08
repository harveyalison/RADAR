import pygame
from Shared.Constants import *
from Shared.Colours import *
from Shared.Scene import *
from Shared.Enums import *

class FrontScene(Scene):

     def __init__(self, game):
         Scene.__init__(self, game)

         self.__explosionSprite = pygame.image.load(Constants.EXPLOSION)
         self.__leftGunSprite = pygame.image.load(Constants.LEFT_GUN)
         self.__rightGunSprite = pygame.image.load(Constants.RIGHT_GUN)
         self.__nightVisionFighterSprite = pygame.image.load(Constants.JU88_NIGHT_REAR)
         self.__catsEyesSprite = pygame.image.load(Constants.CATS_EYES)
         self.__starryNightSprite = pygame.image.load(Constants.STARRY_NIGHT)
         self.__cockpitSprite = pygame.image.load(Constants.BEAUFIGHTER_COCKPIT)

         self.__fighterFading = 'IN'
         self.__fighterPosition =  [900.0, 20.0]
         self.__fighterSize = [128.0, 25.0]  
         self.__alpha = 0
         self.__shooting = False
         self.__shootingCounter = 0

     def render(self):
         
         # Draw starry background
         self.getGame().screen.blit(self.__starryNightSprite, (0,0))

         # Draw fighter
         fighterSpriteScaled = pygame.transform.scale(self.__nightVisionFighterSprite, (int(self.__fighterSize[0]), int(self.__fighterSize[1])))           
         fighterPosition = [self.__fighterPosition[0] - fighterSpriteScaled.get_width() / 2, self.__fighterPosition[1] - fighterSpriteScaled.get_height() / 2]                
         self.blit_alpha2(self.getGame().screen, fighterSpriteScaled, fighterPosition, self.__alpha)
            
         # Draw shooting and explosion, if required
         if self.__shooting:
             self.getGame().screen.blit(self.__explosionSprite, (374,50))
             self.getGame().screen.blit(self.__leftGunSprite, (364,100))
             self.getGame().screen.blit(self.__rightGunSprite, (474,100))

         # Draw cockpit 
         self.getGame().screen.blit(self.__cockpitSprite, (0,0))

         # Draw cats eyes
         self.blit_alpha2(self.getGame().screen, self.__catsEyesSprite, (0,0), self.__alpha)
         font = pygame.font.Font(None, 32)
         self.blit_alpha2(self.getGame().screen, font.render('RADAR gives you...', True, Colours.GREEN, Colours.BLACK), (130, 475), self.__alpha)
         self.blit_alpha2(self.getGame().screen, font.render('Cats eyes!', True, Colours.GREEN, Colours.BLACK), (700, 475), self.__alpha)


         # Draw Labels at bottom
         self.clearText()
         self.addText('WWII Night Fighter RADAR Interception', 300, 670, Colours.GREEN, Colours.BLACK, 32)    
         self.addText('Press the green button to find out more!', 300, 720, Colours.GREEN, Colours.BLACK, 32)

         Scene.render(self)
         

     def updateState(self):
         Scene.updateState(self)

         # Set fighter position
         if self.__shooting:
             self.__shootingCounter += 1
             if self.__shootingCounter >= 200:     
                 self.__shooting = False        
                 self.__fighterPosition = [900.0, 20,0] 
         elif self.__fighterPosition[0] <= 500:
             self.__shooting = True
             self.__shootingCounter = 0
         else:
             self.__fighterPosition[0] -= 1
             self.__fighterPosition[1] += 0.2

         # Set fighter size
         sizeScale = (self.__fighterPosition[0] - 500) / 400
         self.__fighterSize[0] = 512 - sizeScale * 400
         self.__fighterSize[1] = 100 - sizeScale * 80

         # Set alpha
         if self.__shooting:
             self.__alpha = 255
         elif self.__fighterFading == 'IN':           
             if self.__alpha < 255:
                 self.__alpha += 10
             else:
                 self.__fighterFading = 'OUT'
         else:
             if self.__alpha > 0:
                 self.__alpha -= 10
             else:
                 self.__fighterFading = 'IN'


     def handleEvents(self, events):
         #Scene.handleEvents(self, events)

         for event in events:
             if event.type == pygame.QUIT:
                 exit()

             if event.type == pygame.KEYUP:
                 if event.key == pygame.K_ESCAPE or \
                     event.key == ord('q'):
                     # Shut down in an orderly fashion
                     pygame.quit()
                     exit()

                 if event.key == ord('c') or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                     
                     self.getGame().changeScene(Enums.Scene.INTRO)

                     
     def blit_alpha2(self, target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)