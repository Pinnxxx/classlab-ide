def largest(a, b, c):
    return max(a, b, c)

import unittest

class T(unittest.TestCase):
    def test_largest(self):
        self.assertEqual(largest(4, 9, 2), 9)