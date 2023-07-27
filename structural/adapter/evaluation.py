from unittest import TestCase
from exercise import *

class Evaluate(TestCase):
    def test_exercise(self):
        sq = Square(11)
        adapter = SquareToRectangleAdapter(sq)
        self.assertEqual(121, calculate_area(adapter))
        sq.side = 10
        self.assertEqual(100, calculate_area(adapter))