# Tests for the euclid module

import unittest
import sys
sys.path.append("/Users/adrian.trejo/Worspace/cypherPy")


from src.cypherpy.utils import euclid

class TestSimple(unittest.TestCase):

    def test_euclid_one(self):
        self.assertEqual(euclid(2366, 273), 91)
    def test_euclid_two(self):
        self.assertEqual(euclid(2366, 0), 2366)

if __name__ == '__main__':  
    unittest.main()