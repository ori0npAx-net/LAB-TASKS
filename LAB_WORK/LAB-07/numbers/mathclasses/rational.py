class Rational:
    
    def __init__(self, n, d=1):
        if d == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = n
        self.denominator = d
        self.simplify()

    def simplify(self):
        # GCD nikal ke fraction simplify karein
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def add(self, other):
        return Add.operate(self, other)

    def sub(self, other):
        return Sub.operate(self, other)

    def mul(self, other):
        return Mul.operate(self, other)

    def div(self, other):
        return Div.operate(self, other)