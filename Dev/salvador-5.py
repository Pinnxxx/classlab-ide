import unittest

def grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    return "F"

if __name__ == '__main__':
    print(f"Test run: grade(95) -> {grade(95)}")
    print(f"Test run: grade(80) -> {grade(80)}")
    print(f"Test run: grade(74) -> {grade(74)}")
    print(f"Test run: grade(67) -> {grade(67)}")
    print(f"Test run: grade(59) -> {grade(59)}")
    print("-" * 30)
    
    unittest.main(exit=False)