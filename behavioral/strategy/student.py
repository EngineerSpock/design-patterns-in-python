from abc import ABC


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        # todo


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        # todo


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        # todo