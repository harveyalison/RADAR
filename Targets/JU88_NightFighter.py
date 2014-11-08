from Shared import GameObject
from Shared import Constants

class JU88_NightFighter(GameObject):

    def __init__(self, position, sprite, game):
        self.__game = game
        self.__hitPoints = 100
        self.__lives = 1
        GameObject.__init__(self, position, Constants.NIGHT_FIGHTER_SIZE, sprite)

    def getGame(self):
        return self.__game

    def isDestroyed(self):
        return self.__lives <= 0

    def getHitPoints(self):
        return self.__hitPoints

    def hit(self):
        self.__lives -= 1

    def getHitSound(self):
        pass




   



