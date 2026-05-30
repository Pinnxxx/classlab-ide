import unittest
from josh_4 import average

class T(unittest.TestCase):
    def test_avg(self):
        self.assertEqual(average([12,8,20,16]), 14.0)