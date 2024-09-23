import math

class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        print(int(self.numerator / gcd), '/', int(self.denominator/gcd), sep = '')
    
    def add(self, another):
        denom = self.denominator * another.denominator
        numm = self.numerator * another.denominator + self.denominator * another.numerator
        p = Fraction(numm, denom)
        return p.reduce()

a, b, c, d = map(int,input().split())
Frac_1 = Fraction(a, b)
Frac_2 = Fraction(c, d)
Frac_1.add(Frac_2)