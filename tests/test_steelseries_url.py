import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.steelseries import get_steelseries_url

class TestSteelSeriesURL(unittest.TestCase):
    def test_get_steelseries_url_returns_valid_string(self):
        url = get_steelseries_url()
        self.assertIsInstance(url, str)
        self.assertTrue(url.startswith("http://"))

if __name__ == "__main__":
    unittest.main()
