from mathclasses.rational import Rational
class Sub:
    @staticmethod
    def operate(a, b):
        n = a.numerator * b.denominator - b.numerator * a.denominator
        d = a.denominator * b.denominator
        return Rational(n, d)