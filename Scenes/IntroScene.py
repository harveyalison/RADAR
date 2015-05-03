import pygame
from Shared.Constants import *
from Shared.Colours import *
from Shared.Scene import *
from Shared.Enums import *

class IntroScene(Scene):    
    
    def __init__(self, game=None):
        if game is not None:
            Scene.__init__(self, game)
            self.__whatIsRadarSprite = pygame.image.load(Constants.WHAT_IS_RADAR)
            self.__AI_Mk_IV_Sprite = pygame.image.load(Constants.AI_MK_IV)
            self.__ASV_Mk_II_Sprite = pygame.image.load(Constants.ASV_MK_II)
            self.__AI_MK_VIII_Sprite = pygame.image.load(Constants.AI_MK_VIII)
            self.__AI_MK_X_Sprite = pygame.image.load(Constants.AI_MK_X)
            self.__airborneIntercept_Sprite = pygame.image.load(Constants.AIRBORNE_INTERCEPT)

        self.__selectedOption = Enums.IntroOptions.WHAT_IS_RADAR
        self.__TICKS_SINCE_LAST_EVENT = 0

    def render(self):
       
        self.clear_text()

        # Draw Title
        self.add_text('WWII Night Fighter RADAR Interception', 420, 20, Colours.YELLOW, Colours.BLACK, 32)

        # Top row

        # Draw 'What is RADAR?'image and text
        self.get_game().screen.blit(self.__whatIsRadarSprite, (158, 90))
        self.add_text('What is RADAR?', 158, 250, Colours.YELLOW, Colours.BLACK, 24)

        if self.__selectedOption == Enums.IntroOptions.WHAT_IS_RADAR:
            selectedRect = pygame.Rect(148, 80, 240, 195)
            pygame.draw.rect(self.get_game().screen, Colours.RED, selectedRect, 2)

        # Draw AI MK IV image and text
        self.get_game().screen.blit(self.__AI_Mk_IV_Sprite, (428, 90))
        self.add_text('AI MK IV', 428, 250, Colours.YELLOW, Colours.BLACK, 24)

        if self.__selectedOption == Enums.IntroOptions.AI_MK_IV:
            selectedRect = pygame.Rect(418, 80, 425, 195)
            pygame.draw.rect(self.get_game().screen, Colours.RED, selectedRect, 2)

        # Draw ASV MK II image and text
        self.get_game().screen.blit(self.__ASV_Mk_II_Sprite, (878, 90))
        self.add_text('ASV MK II', 878, 250, Colours.YELLOW, Colours.BLACK, 24)

        if self.__selectedOption == Enums.IntroOptions.ASV_MK_II:
            selectedRect = pygame.Rect(868, 80, 270, 195)
            pygame.draw.rect(self.get_game().screen, Colours.RED, selectedRect, 2)

        # Second row

        # Draw 'Airborne Interception' image and text
        self.get_game().screen.blit(self.__airborneIntercept_Sprite, (158, 290))
        self.add_text('Airborne Intercept', 158, 450, Colours.YELLOW, Colours.BLACK, 24)

        if self.__selectedOption == Enums.IntroOptions.AIRBORNE_INTERCEPT:
            selectedRect = pygame.Rect(148, 280, 240, 195)
            pygame.draw.rect(self.get_game().screen, Colours.RED, selectedRect, 2)
            
        # Draw AI MK VIII image and text
        self.get_game().screen.blit(self.__AI_MK_VIII_Sprite, (428, 290))
        self.add_text('AI MK VIII', 428, 450, Colours.YELLOW, Colours.BLACK, 24)

        if self.__selectedOption == Enums.IntroOptions.AI_MK_VIII:
            selectedRect = pygame.Rect(418, 280, 425, 195)
            pygame.draw.rect(self.get_game().screen, Colours.RED, selectedRect, 2)

        # Draw AI MK X image and text
        self.get_game().screen.blit(self.__AI_MK_X_Sprite, (878, 290))
        self.add_text('AI MK X', 878, 450, Colours.YELLOW, Colours.BLACK, 24)

        if self.__selectedOption == Enums.IntroOptions.AI_MK_X:
            selectedRect = pygame.Rect(868, 280, 270, 195)
            pygame.draw.rect(self.get_game().screen, Colours.RED, selectedRect, 2)

        # Draw Instructions
        self.add_text('Instructions:', 158, 500, Colours.YELLOW, Colours.BLACK, 32)
        self.add_text('Use the joystick to select an option', 158, 530, Colours.YELLOW, Colours.BLACK, 32)
        self.add_text('Press the green button for more information', 158, 560, Colours.YELLOW, Colours.BLACK, 32)
        self.add_text('Press the blue button to return to the front screen', 158, 590, Colours.YELLOW, Colours.BLACK, 32)
        if self.__selectedOption == Enums.IntroOptions.AI_MK_IV:
            self.add_text('Press the red button for a simulation', 158, 620, Colours.YELLOW, Colours.BLACK, 32)
        
        Scene.render(self)
        
    def handle_events(self, events):
        Scene.handle_events(self, events)

        for event in events:

            self.__TICKS_SINCE_LAST_EVENT = 0
 
            # events that change selection     
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                if self.__selectedOption == Enums.IntroOptions.WHAT_IS_RADAR:
                    self.__selectedOption = Enums.IntroOptions.AI_MK_IV
                elif self.__selectedOption == Enums.IntroOptions.AI_MK_IV:
                    self.__selectedOption = Enums.IntroOptions.ASV_MK_II
                elif self.__selectedOption == Enums.IntroOptions.AIRBORNE_INTERCEPT:
                    self.__selectedOption = Enums.IntroOptions.AI_MK_VIII
                elif self.__selectedOption == Enums.IntroOptions.AI_MK_VIII:
                    self.__selectedOption = Enums.IntroOptions.AI_MK_X
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                if self.__selectedOption == Enums.IntroOptions.ASV_MK_II:
                    self.__selectedOption = Enums.IntroOptions.AI_MK_IV
                elif self.__selectedOption == Enums.IntroOptions.AI_MK_IV:
                    self.__selectedOption = Enums.IntroOptions.WHAT_IS_RADAR
                elif self.__selectedOption == Enums.IntroOptions.AI_MK_X:
                    self.__selectedOption = Enums.IntroOptions.AI_MK_VIII
                elif self.__selectedOption == Enums.IntroOptions.AI_MK_VIII:
                    self.__selectedOption = Enums.IntroOptions.AIRBORNE_INTERCEPT
            elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                if self.__selectedOption == Enums.IntroOptions.AIRBORNE_INTERCEPT:
                    self.__selectedOption = Enums.IntroOptions.WHAT_IS_RADAR
                elif self.__selectedOption == Enums.IntroOptions.AI_MK_VIII:
                    self.__selectedOption = Enums.IntroOptions.AI_MK_IV
                elif self.__selectedOption == Enums.IntroOptions.AI_MK_X:
                    self.__selectedOption = Enums.IntroOptions.ASV_MK_II
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                if self.__selectedOption == Enums.IntroOptions.WHAT_IS_RADAR:
                    self.__selectedOption = Enums.IntroOptions.AIRBORNE_INTERCEPT
                elif self.__selectedOption == Enums.IntroOptions.AI_MK_IV:
                    self.__selectedOption = Enums.IntroOptions.AI_MK_VIII
                elif self.__selectedOption == Enums.IntroOptions.ASV_MK_II:
                    self.__selectedOption = Enums.IntroOptions.AI_MK_X
 
            # Events that cause us to return to main
            elif event.type == pygame.KEYUP and self.__selectedOption == Enums.IntroOptions.AI_MK_VIII:
                if event.key == pygame.K_c or event.key == pygame.K_RETURN:
                    self.get_game().change_scene(Enums.Scene.AI_MK_VIII_INFO)
                if event.key == pygame.K_a:
                    self.get_game().change_scene(Enums.Scene.AI_MK_VIII_SIMULATOR)
            elif event.type == pygame.KEYUP and self.__selectedOption == Enums.IntroOptions.AI_MK_IV:
                if event.key == pygame.K_c or event.key == pygame.K_RETURN:
                    self.get_game().change_scene(Enums.Scene.AI_MK_IV_INFO)
                if event.key == pygame.K_a:
                    self.get_game().change_scene(Enums.Scene.AI_MK_IV_SIMULATOR)
            elif event.type == pygame.KEYUP and self.__selectedOption == Enums.IntroOptions.WHAT_IS_RADAR:
                if event.key == pygame.K_c or event.key == pygame.K_RETURN:
                    self.get_game().change_scene(Enums.Scene.WHAT_IS_RADAR)
            elif event.type == pygame.KEYUP and self.__selectedOption == Enums.IntroOptions.AIRBORNE_INTERCEPT:
                if event.key == pygame.K_c or event.key == pygame.K_RETURN:
                    self.get_game().change_scene(Enums.Scene.AIRBORNE_INTERCEPT)
            elif event.type == pygame.KEYUP and self.__selectedOption == Enums.IntroOptions.ASV_MK_II:
                if event.key == pygame.K_c or event.key == pygame.K_RETURN:
                    self.get_game().change_scene(Enums.Scene.ASV_MK_II_INFO)
                if event.key == pygame.K_a:
                    self.get_game().change_scene(Enums.Scene.ASV_MK_II_SIMULATOR)
            elif event.type == pygame.KEYUP and self.__selectedOption == Enums.IntroOptions.AI_MK_X:
                if event.key == pygame.K_c or event.key == pygame.K_RETURN:
                    self.get_game().change_scene(Enums.Scene.AI_MK_X_INFO)
                if event.key == pygame.K_a:
                    self.get_game().change_scene(Enums.Scene.AI_MK_X_SIMULATOR)
                     
        








                

