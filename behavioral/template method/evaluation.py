from unittest import TestCase
from exercise import *

class Evaluate(TestCase):
    def test_impasse(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1), 'Combat should yield -1 since nobody died.')
        self.assertEqual(-1, game.combat(0, 1), 'Combat should yield -1 since nobody died.')

    def test_temporary_murder(self):
        c1 = Creature(1, 1)
        c2 = Creature(2, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(1, game.combat(0, 1))

    def test_double_murder(self):
        c1 = Creature(2, 1)
        c2 = Creature(2, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1))

    def test_permanent_damage_death(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 3)
        game = PermanentDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1), 'Nobody should win this battle.')
        self.assertEqual(1, c1.health)
        self.assertEqual(2, c2.health)
        self.assertEqual(1, game.combat(0, 1), 'Creature at index 1 should win this')
