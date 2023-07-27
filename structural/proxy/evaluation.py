from unittest import TestCase
from exercise import *

class Evaluate(TestCase):
  def test_exercise(self):
    p = Person(10)
    rp = ResponsiblePerson(p)

    self.assertEqual('too young', rp.drive())
    self.assertEqual('too young', rp.drink())
    self.assertEqual('dead', rp.drink_and_drive())

    rp.age = 20

    self.assertEqual('driving', rp.drive())
    self.assertEqual('drinking', rp.drink())
    self.assertEqual('dead', rp.drink_and_drive())