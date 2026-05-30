import unittest
from julian_task5 import is_palindrome

class T(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("Hello"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))

if __name__ == "__main__":
    unittest.main()