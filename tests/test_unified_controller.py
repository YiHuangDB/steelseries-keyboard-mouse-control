import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.controller import UnifiedRGBController

class TestUnifiedController(unittest.TestCase):
    def test_unified_controller_composition(self):
        controller = UnifiedRGBController()
        self.assertIsNotNone(controller.steelseries)
        self.assertIsNotNone(controller.razer)

if __name__ == "__main__":
    unittest.main()
