from Shared.Scene import *


class AI_MK_VIII_SimulatorScene(Scene):

    def __init__(self, game=None):
        if game is not None:
            Scene.__init__(self, game)

    def render(self):
        self.clear_text()

        # do stuff

        Scene.render(self)

    def updateState(self):
        Scene.updateState(self)

        pass

    def handle_events(self, events):
        Scene.handle_events(self, events)

        for event in events:
            pass
                










                

