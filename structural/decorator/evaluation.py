from unittest import TestCase
from exercise import *

class Evaluate(TestCase):
  def test_circle(self):
    circle = ColoredShape(Circle(5), 'red')
    self.assertEqual(
      'A circle of radius 5 has the color red',
      str(circle)
    )
    circle.resize(2)
    self.assertEqual(
      'A circle of radius 10 has the color red',
      str(circle)
    )

  def test_no_resize_in_square(self):
    square = Square(4)
    r = getattr(square, 'resize', None)
    self.assertFalse(callable(r),
                     'Please do not add resize() to Square')

  def test_square(self):
    square = ColoredShape(Square(2), 'blue')
    self.assertEqual(
      'A square with side 2 has the color blue',
      str(square)
    )
    square.resize(2)
    self.assertEqual(
      'A square with side 2 has the color blue',
      str(square)
    )