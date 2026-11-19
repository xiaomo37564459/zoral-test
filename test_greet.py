import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_normal_name(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_single_character(self):
        self.assertEqual(greet("A"), "Hello, A!")

    def test_empty_string(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_whitespace_name(self):
        self.assertEqual(greet("  "), "Hello,   !")

    def test_unicode_name(self):
        self.assertEqual(greet("世界"), "Hello, 世界!")


if __name__ == "__main__":
    unittest.main()
