import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.steelseries import SteelSeriesLEDController

class TestSteelSeriesController(unittest.TestCase):
    def test_steelseries_controller_initialization(self):
        controller = SteelSeriesLEDController(game_name="TEST_RGB")
        self.assertEqual(controller.game, "TEST_RGB")
        self.assertFalse(controller.is_active)
        self.assertTrue(controller.base_url.startswith("http://"))

if __name__ == "__main__":
    unittest.main()
