from Shared.Constants import *
from Shared.Scene import *
from Shared.Enums import *

class FrontScene(Scene):

    def __init__(self, game=None):
        if game is not None:
            Scene.__init__(self, game)

            self.__explosionSprite = pygame.image.load(Constants.EXPLOSION)
            self.__leftGunSprite = pygame.image.load(Constants.LEFT_GUN)
            self.__rightGunSprite = pygame.image.load(Constants.RIGHT_GUN)
            self.__nightVisionFighterSprite = pygame.image.load(Constants.JU88_NIGHT_REAR)
            self.__catsEyesSprite = pygame.image.load(Constants.CATS_EYES)
            self.__starryNightSprite = pygame.image.load(Constants.STARRY_NIGHT)
            self.__cockpitSprite = pygame.image.load(Constants.BEAUFIGHTER_COCKPIT)
            self.__greenButtonSprite = pygame.image.load(Constants.ARCADE_GREEN)

        self.__fighterFading = 'IN'
        self.__initialFighterPosition = self.start_position()
        self.__fighterPosition = self.__initialFighterPosition
        self.__fighterSize = [128.0, 25.0]
        self.__alpha = 0
        self.__shooting = False
        self.__shootingCounter = 0

    def render(self):
         
        # Draw starry background
        self.get_game().screen.blit(self.__starryNightSprite, (128, 80))

        # Draw fighter
        fighterSpriteScaled = pygame.transform.scale(self.__nightVisionFighterSprite, (int(self.__fighterSize[0]), int(self.__fighterSize[1])))
        fighterPosition = [self.__fighterPosition[0] - fighterSpriteScaled.get_width() / 2, self.__fighterPosition[1] - fighterSpriteScaled.get_height() / 2]
        self.blit_alpha2(self.get_game().screen, fighterSpriteScaled, fighterPosition, self.__alpha)
            
        # Draw shooting and explosion, if required
        if self.__shooting:
            self.get_game().screen.blit(self.__explosionSprite, (502, 130))
            self.get_game().screen.blit(self.__leftGunSprite, (502, 180))
            self.get_game().screen.blit(self.__rightGunSprite, (602, 180))

        # Draw cockpit
        self.get_game().screen.blit(self.__cockpitSprite, (128, 80))

        # Draw cats eyes
        self.blit_alpha2(self.get_game().screen, self.__catsEyesSprite, (128, 80), self.__alpha)

        # Draw label at the top
        self.clear_text()
        self.add_text('RADAR - seeing in the dark!', 328, 20, Colours.YELLOW, Colours.BLACK, 64)

        # Draw Labels at bottom
        self.add_text('Press the green button to find out more!', 428, 735, Colours.YELLOW, Colours.BLACK, 32)
        self.get_game().screen.blit(self.__greenButtonSprite, (378, 730))
        self.get_game().screen.blit(self.__greenButtonSprite, (868, 730))

        Scene.render(self)

    def updateState(self):
        Scene.updateState(self)

        # Set fighter position
        if self.__shooting:
            self.__shootingCounter += 1
            if self.__shootingCounter >= 200:
                self.__shooting = False
                self.__fighterPosition = self.start_position()
        elif self.__fighterPosition[0] <= 628:
            self.__shooting = True
            self.__shootingCounter = 0
        else:
            self.__fighterPosition[0] -= 1
            self.__fighterPosition[1] += 0.2

        # Set fighter size
        sizeScale = (self.__fighterPosition[0] - 628) / 400
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

    def handle_events(self, events):
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
                    self.get_game().change_scene(Enums.Scene.INTRO)

    @staticmethod
    def blit_alpha2(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

    @staticmethod
    def start_position():
        return [1028.0, 100.0]