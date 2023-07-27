from unittest import TestCase
from exercise import *

class Evaluate(TestCase):
    def test_simple_addition(self):
        simple = AdditionExpression(Value(2), Value(3))
        ep = ExpressionPrinter()
        ep.visit(simple)
        self.assertEqual("(2+3)", str(ep))

    def test_product_of_addition_and_value(self):
        expr = MultiplicationExpression(
            AdditionExpression(Value(2), Value(3)),
            Value(4)
        )
        ep = ExpressionPrinter()
        ep.visit(expr)
        self.assertEqual("(2+3)*4", str(ep))