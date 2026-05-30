import unittest
from estuar_4 import largest

class TestLargest(unittest.TestCase):
    def test_largest_basic(self):
        self.assertEqual(largest(4, 9, 2), 9)
    
    def test_largest_first(self):
        self.assertEqual(largest(10, 5, 3), 10)
    
    def test_largest_last(self):
        self.assertEqual(largest(1, 5, 8), 8)
    
    def test_largest_equal(self):
        self.assertEqual(largest(5, 5, 3), 5)
        self.assertEqual(largest(5, 3, 5), 5)
        self.assertEqual(largest(3, 5, 5), 5)
    
    def test_largest_negative(self):
        self.assertEqual(largest(-1, -5, -3), -1)

if __name__ == "__main__":
    unittest.main()