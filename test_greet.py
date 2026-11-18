import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("world"), "hello, world")

    def test_greet_with_name(self):
        self.assertEqual(greet("DeepSeek"), "hello, DeepSeek")


if __name__ == "__main__":
    unittest.main()
