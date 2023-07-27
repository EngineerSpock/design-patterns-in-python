from unittest import TestCase
from exercise import *

class Evaluate(TestCase):
    def test_exercise(self):
        line1 = Line(
            Point(3, 3),
            Point(10, 10)
        )
        line2 = line1.deep_copy()
        line1.start.x = line1.end.x = line1.start.y = line1.end.y = 0

        self.assertEqual(3, line2.start.x)
        self.assertEqual(3, line2.start.y)
        self.assertEqual(10, line2.end.x)
        self.assertEqual(10, line2.end.y)
