from mathclasses.rational import Rational
class Div:
    @staticmethod
    def operate(a, b):
        if b.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        n = a.numerator * b.denominator
        d = a.denominator * b.numerator
        return Rational(n, d)
