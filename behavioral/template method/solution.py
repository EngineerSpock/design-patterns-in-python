from abc import ABC


class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        first = self.creatures[c1_index]
        second = self.creatures[c2_index]
        self.hit(first, second)
        self.hit(second, first)
        first_alive = first.health > 0
        second_alive = second.health > 0
        if first_alive == second_alive: return -1
        return c1_index if first_alive else c2_index

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        old_health = defender.health
        defender.health -= attacker.attack
        if defender.health > 0:
            defender.health = old_health


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack