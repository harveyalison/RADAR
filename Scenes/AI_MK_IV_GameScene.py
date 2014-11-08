from Shared.Scene import *
import random, pygame, sys, time
from pygame.locals import *
from random import randint
import math
import pygame.gfxdraw
#from Receivers import *
#from Emitters import *
#from globals import *
from WWII_Night_Fighter_RADAR import *
from AI_MK_IV_InfoScene import *

# The one and only receiver
#RECEIVER = None

# The collection of emitters
#EMITTERS = []

#LEVEL = None
#SCORE = None

class AI_MK_IV_GameScene(Scene):
    
    def __init__(self, surface):
        global FPSCLOCK #, WINDOWSURF
        #pygame.init()
        FPSCLOCK = pygame.time.Clock()
        self.surface = surface
        #WINDOWSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('AI MK IV Simulation')
        
        # Keep going until the user says quit
        #while True:
         #   introScreen = IntroScreen(WINDOWSURF)
          #  introScreenResult = introScreen.Show()
           # if introScreenResult == IntroScreenResult.QUIT:
            #    break
            #if introScreenResult == Result.NEWGAME:
             #   GameLoop()   

        # Shut down in an orderly fashion
        #pygame.quit()
        #sys.exit()

    def Show(self):
        gameInfoScreen = AI_MK_IV_Game_Info(self.surface)
        gameInfoScreenResult = gameInfoScreen.Show()
        if gameInfoScreenResult == GameResult.QUIT:
            return GameResult.QUIT
        if gameInfoScreenResult == GameResult.NEWGAME:
            return self.GameLoop()
        

    def GameLoop(self):
        global LEVEL, SCORE #, RECEIVER
        SCORE = 0
        LEVEL = 1
        #RECEIVER = SimpleReceiver(WINDOWSURF)

        while True: # Main game loop
            self.SetupLevel()
            levelResult = self.LevelLoop()
            if levelResult == GameResult.LEVELUP:
                LEVEL += 1
            elif levelResult == GameResult.QUIT:
                return GameResult.QUIT
            elif levelResult == GameResult.GAMEOVER:
                return GameResult.GAMEOVER

    def SetupLevel(self):
        global LEVEL #, EMITTERS
            
        if LEVEL != 1:
            # Pause a bit to let any sounds finish
            # from previous level
            time.sleep(2)
            # Play level up sound
            soundObj = pygame.mixer.Sound('LevelUp.wav')
            soundObj.play()
            time.sleep(2)
        
        # Each level has a number of emitters equal to the level
        #emitterCount = LEVEL   
        #EMITTERS = []       
        #while emitterCount > 0:
        #    EMITTERS.append(SimpleEmitter(WINDOWSURF))
        #    emitterCount -= 1        
                
    def LevelLoop(self): 
        
        while True: # Main level loop
            eventResult = self.HandleEvents()

            if eventResult == GameResult.QUIT:
                return GameResult.QUIT
            
            gameStateChanged = GameResult.NOWT;
            if eventResult == GameResult.SUMMAT:
                gameStateChanged = self.UpdateState()
            
            if gameStateChanged == GameResult.LEVELUP:
                return GameResult.LEVELUP
            elif gameStateChanged == GameResult.GAMEOVER:
                # Show game over screen
                gameOverScreen = GameOverScreen(self.surface)
                gameOverScreen.Show()
                return GameResult.GAMEOVER
            elif gameStateChanged == GameResult.LIFELOST:
                # Show life lost screen
                lifeLostScreen = LifeLostScreen(self.surface)
                lifeLostScreen.Show()
                # Resume
                gameStateChanged = GameResult.SUMMAT
            elif gameStateChanged == GameResult.SUMMAT:
                self.UpdateWindow()

            # Wait a clock tick
            FPSCLOCK.tick(FPS)

    def HandleEvents(self):
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                return GameResult.QUIT

            #RECEIVER.Handle(event)

        # For now, always say summat happened
        return GameResult.SUMMAT

    def UpdateState(self):
        global EMITTERS, RECEIVER, SCORE, LEVEL

        # Default result to always update for now
        result = GameResult.SUMMAT

        # Update the receiver
        #RECEIVER.UpdateState(EMITTERS)

        # Update all the emitters
        #for emitter in EMITTERS:
        #    emitter.UpdateState(RECEIVER, LEVEL)

        #liveEmitters = []
        #noEmitterReachedTarget = True
        #for emitter in EMITTERS:
        #    if emitter.lives == 0:
        #        soundObj = pygame.mixer.Sound('KaBoom.wav')
        #        soundObj.play()
        #        SCORE += 1
        #    elif emitter.targetReached == True:
        #        noEmitterReachedTarget = False
        #        RECEIVER.lives -= 1
        #        if RECEIVER.lives == 0:
        #            result = GameResult.GAMEOVER
        #            break
        #        else:
        #            result = GameResult.LIFELOST
        #            break   
        #    else:
        #        liveEmitters.append(emitter)

        #EMITTERS = liveEmitters 
        
        #if len(EMITTERS) == 0 and noEmitterReachedTarget == True:
        #    result = GameResult.LEVELUP

        return result

    def UpdateWindow(self):
        # First, fill the whole screen with black
        self.surface.fill(BLACK)

        # Then update the status and display
        self.DrawStatus()
        self.DrawDisplay()
        
        # Redraw the screen
        pygame.display.update()

    def DrawDisplay(self):
        # Draw a border for the display
        displayBorderRect = pygame.Rect(0, STATUSHEIGHT, DISPLAYWIDTH, DISPLAYHEIGHT)
        pygame.gfxdraw.rectangle(self.surface, displayBorderRect, WHITE)


        # Draw the background noise
        self.DrawBackgroundNoise()
        
        # Draw the display on top
        AI_MK_IV_Img = pygame.image.load('Images/AI_MK_IV_TRANS_1024.png')
        self.surface.blit(AI_MK_IV_Img, (0, STATUSHEIGHT+1))

        
        
        # Draw the emitters
        #DrawEmitters()

        # Draw the Receiver
        #RECEIVER.Draw()
            
    def DrawStatus(self):       
        # Draw a border for the status
        statusBorderRect = pygame.Rect(0, 0, DISPLAYWIDTH, STATUSHEIGHT)
        pygame.gfxdraw.rectangle(self.surface, statusBorderRect, WHITE)
            
        fontObj = pygame.font.Font('freesansbold.ttf', 8)
        
        # Draw lives left
        textSurfaceObj = fontObj.render('Lives:', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (DISPLAYBORDER, 7)    
        self.surface.blit(textSurfaceObj, textRectObj)

        lifeNumber = 0
        #while lifeNumber < RECEIVER.lives:
        #    smallPiImg = pygame.image.load('PiSmall.png')
        #    self.surface.blit(smallPiImg, (DISPLAYBORDER + 20*lifeNumber, 20))
        #    lifeNumber += 1

        # Draw receiver speed 
        #textSurfaceObj = fontObj.render('Speed:', True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (400, 7)    
        #self.surface.blit(textSurfaceObj, textRectObj)
        #textSurfaceObj = fontObj.render(str(RECEIVER.speed), True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (445, 7)    
        #self.surface.blit(textSurfaceObj, textRectObj)

        # Draw receiver beam width
        #textSurfaceObj = fontObj.render('Width:', True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (400, 20)    
        #self.surface.blit(textSurfaceObj, textRectObj)
        #textSurfaceObj = fontObj.render(str(RECEIVER.width), True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (445, 20)    
        #self.surface.blit(textSurfaceObj, textRectObj)

        # Draw receiver direction
        #textSurfaceObj = fontObj.render('Direction:', True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (400, 33)    
        #self.surface.blit(textSurfaceObj, textRectObj)
        #textSurfaceObj = fontObj.render(str(RECEIVER.direction), True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (445, 33)    
        #self.surface.blit(textSurfaceObj, textRectObj)

        # Draw receiver strength
        #textSurfaceObj = fontObj.render('Power:', True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (300, 33)    
        #self.surface.blit(textSurfaceObj, textRectObj)
        #textSurfaceObj = fontObj.render(str(RECEIVER.power), True, GREEN, BLACK)
        #textRectObj = textSurfaceObj.get_rect()
        #textRectObj.topleft = (330, 33)    
        #self.surface.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj.render('Score:', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (300, 20)    
        self.surface.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render(str(SCORE), True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (330, 20)    
        self.surface.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj.render('Level:', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (300, 7)    
        self.surface.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj.render(str(LEVEL), True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (330, 7)    
        self.surface.blit(textSurfaceObj, textRectObj)

    def DrawEmitters(self):
        #for emitter in EMITTERS:
        #    emitter.Draw()
        pygame.display.set_caption('AI MK IV Simulation')

    def DrawBackgroundNoise(self):
        # Elevation tube
        #pygame.draw.aaline(self.surface, GREEN, (255, 250), (420, 250))
        for x in xrange(255, 420):
            linelength = random.randint(1,11)
            pygame.draw.aaline(self.surface, GREEN, (x, 250), (x, 250-linelength))
            pygame.draw.aaline(self.surface, GREEN, (x, 250), (x, 250+linelength))

        # Azimuth tube
        pygame.draw.aaline(self.surface, GREEN, (685, 140), (685, 365))
        for y in xrange(140, 365):
            linelength = random.randint(1,11)
            pygame.draw.aaline(self.surface, GREEN, (685-linelength, y), (685, y))
            pygame.draw.aaline(self.surface, GREEN, (685+linelength, y), (685, y))
    


