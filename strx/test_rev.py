import unittest

from strx.rev import rev


class TestRev(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(rev(""), "")

    def test_simple(self):
        self.assertEqual(rev("abc"), "cba")

    def test_palindrome(self):
        self.assertEqual(rev("level"), "level")

    def test_unicode(self):
        self.assertEqual(rev("你好"), "好你")

    def test_spaces(self):
        self.assertEqual(rev("a b"), "b a")


if __name__ == "__main__":
    unittest.main()
