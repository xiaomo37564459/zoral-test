import unittest

from slug import slugify


class TestSlugify(unittest.TestCase):
    def test_lowercase(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_spaces_become_hyphens(self):
        self.assertEqual(slugify("foo bar baz"), "foo-bar-baz")

    def test_underscores_become_hyphens(self):
        self.assertEqual(slugify("foo_bar_baz"), "foo-bar-baz")

    def test_strip_leading_and_trailing_hyphens(self):
        self.assertEqual(slugify("  hello world  "), "hello-world")
        self.assertEqual(slugify("_hello world_"), "hello-world")
        self.assertEqual(slugify("--hello--"), "hello")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_mixed(self):
        self.assertEqual(slugify("Hello_World Test"), "hello-world-test")


if __name__ == "__main__":
    unittest.main()
