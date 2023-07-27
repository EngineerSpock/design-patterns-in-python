import unittest
from abc import ABC
from enum import Enum
from exercise import *

class Evaluate(unittest.TestCase):
def test(self):
    game = Game()
    goblin = Goblin(game)
    game.creatures.append(goblin)

    self.assertEqual(1, goblin.attack)
    self.assertEqual(1, goblin.defense)

    goblin2 = Goblin(game)
    game.creatures.append(goblin2)

    self.assertEqual(1, goblin.attack)
    self.assertEqual(2, goblin.defense, 'There are two goblins in play')

    goblin3 = GoblinKing(game)
    game.creatures.append(goblin3)

    self.assertEqual(2, goblin.attack)
    self.assertEqual(3, goblin.defense)