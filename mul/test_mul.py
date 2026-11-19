import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mul import mul


class TestMul(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(mul(2, 3), 6)

    def test_negative(self):
        self.assertEqual(mul(-2, 3), -6)

    def test_zero(self):
        self.assertEqual(mul(0, 5), 0)

    def test_floats(self):
        self.assertAlmostEqual(mul(1.5, 2), 3.0)


if __name__ == "__main__":
    unittest.main()
