import unittest

def largest(a, b, c):
    """Returns the largest of three numbers."""
    return max(a, b, c) 

if __name__ == '__main__':
    print(f"Test run: largest(4, 9, 2) -> {largest(4, 9, 2)}")
    print("-" * 30)
    
    unittest.main(exit=False)