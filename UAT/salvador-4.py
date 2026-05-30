import unittest

def largest(a, b, c):
    """Returns the largest of three numbers."""
    return max(a, b, c)

class T(unittest.TestCase):
    def test_largest(self):
        self.assertEqual(largest(4, 9, 2), 9)
        self.assertEqual(largest(10, 5, 8), 10) 
        self.assertEqual(largest(3, 3, 1), 3)    
        self.assertEqual(largest(-5, -2, -10), -2) 

if __name__ == '__main__':
    print(f"Test run: largest(4, 9, 2) -> {largest(4, 9, 2)}")
    print("-" * 30)
    
    unittest.main(exit=False)