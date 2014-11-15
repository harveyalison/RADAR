from Shared.Scene import *
from Shared.Colours import *

class AI_MK_X_SimulatorScene(Scene):

    def __init__(self, game=None):
        if game is not None:
            Scene.__init__(self, game)

    def render(self):
       
        self.clear_text()

        # Draw Title
        self.add_text('AI MK X Airbourne Interception RADAR Game Info', 285, 20, Colours.GREEN, Colours.BLACK, 32)

        Scene.render(self)

        
    def handle_events(self, events):
        Scene.handle_events(self, events)

             
                










                

