import unittest

from numx.clamp import clamp


class TestClamp(unittest.TestCase):
    def test_below(self):
        self.assertEqual(clamp(-5, 0, 10), 0)

    def test_above(self):
        self.assertEqual(clamp(15, 0, 10), 10)

    def test_within(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_boundaries(self):
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_floats(self):
        self.assertEqual(clamp(1.5, 0.0, 1.0), 1.0)

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)


if __name__ == "__main__":
    unittest.main()
