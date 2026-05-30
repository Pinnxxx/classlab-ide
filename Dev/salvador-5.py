import unittest

def grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    return "F"

class T(unittest.TestCase):
    def test_grade(self):
        self.assertEqual(grade(95), "A")
        self.assertEqual(grade(74), "C")
        self.assertEqual(grade(50), "F")

if __name__ == '__main__':
    print(f"Test run: grade(95) -> {grade(95)}")
    print(f"Test run: grade(74) -> {grade(74)}")
    print(f"Test run: grade(50) -> {grade(50)}")
    print("-" * 30)
    
    unittest.main(exit=False)