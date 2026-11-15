import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.razer import RazerChromaLEDController

class TestRazerController(unittest.TestCase):
    def test_razer_initial_state(self):
        controller = RazerChromaLEDController()
        self.assertFalse(controller.initialized)
        self.assertIsNone(controller.chroma)

if __name__ == "__main__":
    unittest.main()
