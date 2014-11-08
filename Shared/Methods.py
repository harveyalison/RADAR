try:
    import pygame
    import os
except ImportError, err:
        print "couldn't load module. %s" % (err)
        sys.exit(2)

def load_png(name):
        """ Load image and return image object"""
        fullname = os.path.join('Assets', name)
        try:
                image = pygame.image.load(fullname)
                if image.get_alpha is None:
                        image = image.convert()
                else:
                        image = image.convert_alpha()
        except pygame.error, message:
                print 'Cannot load image:', fullname
                raise SystemExit, message
        return image, image.get_rect()