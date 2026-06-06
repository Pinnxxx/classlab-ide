import unittest
from main import greet, add


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_greet(self):
        self.assertIn("Hello", greet("Sam"))


if __name__ == "__main__":
    unittest.main()
