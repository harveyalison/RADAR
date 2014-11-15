import unittest
from Scenes.AI_MK_IV_SimulatorScene import *
from Shared.Constants import *

class AI_MK_IV_Sim_Tests(unittest.TestCase):
    """ Tests for the AI MK IV Simulator"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_updaterange(self):
        mysim = AI_MK_IV_SimulatorScene()
        AI_MK_IV_SimulatorScene.updateRange(mysim)


if __name__ == "__main__":
    unittest.main()