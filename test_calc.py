import unittest

from calc import power


class TestPower(unittest.TestCase):
    def test_positive_exp(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 1), 5)

    def test_zero_exp(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 0), 1)

    def test_zero_base(self):
        self.assertEqual(power(0, 5), 0)

    def test_negative_base(self):
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-2, 2), 4)

    def test_negative_exp_raises(self):
        with self.assertRaises(ValueError) as ctx:
            power(2, -1)
        self.assertEqual(str(ctx.exception), "exp must be >= 0")


if __name__ == "__main__":
    unittest.main()
