from mathclasses.rational import Rational
class Mul:
    @staticmethod
    def operate(a, b):
        n = a.numerator * b.numerator
        d = a.denominator * b.denominator
        return Rational(n, d)