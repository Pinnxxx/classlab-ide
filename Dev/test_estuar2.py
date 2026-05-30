import unittest
from estuar_5 import grade

class TestGrade(unittest.TestCase):
    def test_a_grade(self):
        self.assertEqual(grade(95), 'A')
        self.assertEqual(grade(90), 'A')
    
    def test_b_grade(self):
        self.assertEqual(grade(85), 'B')
        self.assertEqual(grade(80), 'B')
    
    def test_c_grade(self):
        self.assertEqual(grade(75), 'C')
        self.assertEqual(grade(70), 'C')
    
    def test_d_grade(self):
        self.assertEqual(grade(65), 'D')
        self.assertEqual(grade(60), 'D')
    
    def test_f_grade(self):
        self.assertEqual(grade(59), 'F')
        self.assertEqual(grade(0), 'F')

if __name__ == "__main__":
    unittest.main()