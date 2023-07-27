import unittest
from exercise import *

class Evaluate(unittest.TestCase):
    def test_exercise(self):
        s = Sentence('alpha beta gamma')
        s[1].capitalize = True
        self.assertEqual(str(s), 'alpha BETA gamma')