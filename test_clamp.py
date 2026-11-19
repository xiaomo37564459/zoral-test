import unittest

from clamp import clamp


class TestClamp(unittest.TestCase):
    def test_within_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_below_lo(self):
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_above_hi(self):
        self.assertEqual(clamp(42, 0, 10), 10)

    def test_on_boundaries(self):
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_equal_bounds(self):
        self.assertEqual(clamp(7, 3, 3), 3)

    def test_floats(self):
        self.assertEqual(clamp(1.5, 0.0, 1.0), 1.0)

    def test_invalid_bounds(self):
        with self.assertRaises(ValueError):
            clamp(1, 10, 0)


if __name__ == "__main__":
    unittest.main()
