class ComplexNum:
    def __init__(self, real, imagi):
        self.real = real
        self.imagi = imagi

    def plus(self, another):
        real = self.real + another.real
        imagi = self.imagi + another.imagi
        return ComplexNum(real, imagi)

    def times(self, another):
        real = self.real * another.real - self.imagi * another.imagi
        imagi = self.imagi * another.real + self.real * another.imagi
        return ComplexNum(real, imagi)

    def display(self):
        return '{} + {}i'.format(self.real, self.imagi)
    
if __name__=='__main__':
    a = []
    for t in range(int(input())):
        while(len(a) < 4): a += [int(i) for i in input().split()]
        x = ComplexNum(a[0], a[1])
        y = ComplexNum(a[2], a[3])
        z =  x.plus(y)
        ans1 = z.times(x)
        ans2 = z.times(z)
        print(ans1.display() + ', ' + ans2.display())
        a = a[4:]