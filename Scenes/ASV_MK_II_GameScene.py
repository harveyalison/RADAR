from Shared.Scene import *
from Shared.Colours import *

class ASV_MK_II_GameScene(Scene):

    def __init__(self, game=None):
        if game is not None:
            Scene.__init__(self, game)

    def render(self):
       
        self.clear_text()

        # Draw Title
        self.add_text('ASV MK II Game', 285, 20, Colours.GREEN, Colours.BLACK, 32)

        Scene.render(self)

        
    def handle_events(self, events):
        Scene.handle_events(self, events)

             
                










                

