class Rational:
    def __init__(self, n1,d1):
        self.n1=n1
        self.d1=d1
        
    def simple(self):
        return Rational({self.n1/self.d1})
    
    def __str__(self):
        return f"fraction={self.n1}/{self.d1}"
    
        