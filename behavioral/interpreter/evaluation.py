import re
import unittest
from enum import Enum


class FirstTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ep = ExpressionProcessor()
        ep.variables['x'] = 5
        cls.ep = ep

    def test_simple(self):
        self.assertEqual(1, self.ep.calculate('1'))

    def test_addition(self):
        self.assertEqual(3, self.ep.calculate('1+2'))

    def test_addition_with_variable(self):
        self.assertEqual(6, self.ep.calculate('1+x'))

    def test_failure(self):
        self.assertEqual(0, self.ep.calculate('1+xy'))
