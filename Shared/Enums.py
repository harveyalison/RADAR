class Enums:
    def enum(**enums):
        return type('Enum', (), enums)

    GameResult = enum(NOWT=0, QUIT=1, SUMMAT=2, LEVELUP=3, GAMEOVER=4, NEWGAME=5, LIFELOST=6)


    Scene = enum(FRONT=0, INTRO=1, WHAT_IS_RADAR=2, AIRBORNE_INTERCEPT=3, \
        ASV_MK_II_INFO=4, ASV_MK_II_SIMULATOR=5, ASV_MK_II_GAME=6, \
        AI_MK_IV_INFO=7, AI_MK_IV_SIMULATOR=8, AI_MK_IV_GAME=9, \
        AI_MK_VIII_INFO=10, AI_MK_VIII_SIMULATOR=11, AI_MK_VIII_GAME=12, \
        AI_MK_X_INFO=13, AI_MK_X_SIMULATOR=14, AI_MK_X_GAME=15)

    IntroOptions = enum(WHAT_IS_RADAR=0, AI_MK_IV=1, ASV_MK_II=2, AIRBORNE_INTERCEPT=3, AI_MK_VIII=4, AI_MK_X=5)

