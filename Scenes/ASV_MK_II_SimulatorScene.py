from Shared.Scene import *
from Shared.Colours import *

class ASV_MK_II_SimulatorScene(Scene):

    def __init__(self, game):
        Scene.__init__(self, game)

    def render(self):
       
        self.clearText()

        # Draw Title
        self.addText('ASV MK II Game Info', 285, 20, Colours.GREEN, Colours.BLACK, 32) 

        Scene.render(self)

        
    def handleEvents(self, events):
        Scene.handleEvents(self, events)

             
                










                

