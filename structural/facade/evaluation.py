from unittest import TestCase
from exercise import *

class Evaluate(TestCase):
  def test_exercise(self):
    gen = MagicSquareGenerator()
    square = gen.generate(2)

    print(square)

    v = Verifier()
    self.assertTrue(v.verify(square),
                    'Verification failed. '
                    'This is not a valid magic square.')