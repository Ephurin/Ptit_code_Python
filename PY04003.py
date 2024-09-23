import math

class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        print(int(self.numerator / gcd), '/', int(self.denominator/gcd), sep = '')

a, b = map(int, input().split())
f = Fraction(a, b)
f.reduce()