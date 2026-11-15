import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.razer import RazerChromaLEDController

class TestRazerAvailability(unittest.TestCase):
    def test_razer_availability_check(self):
        controller = RazerChromaLEDController()
        # Should return boolean indicating whether Chroma SDK DLL exists
        avail = controller.is_available()
        self.assertIsInstance(avail, bool)

if __name__ == "__main__":
    unittest.main()
