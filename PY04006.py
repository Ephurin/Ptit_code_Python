from math import sqrt
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return sqrt((pow(self.x - p.x, 2) + pow(self.y - p.y, 2)))

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def triangleArea(self):
        AB = self.a.distance(self.b)
        AC = self.a.distance(self.c)
        BC = self.b.distance(self.c)
        if (AB >= AC + BC) or (AB + AC <= BC) or (AB + BC <= AC):
            return 'INVALID'
        return '{:.2f}'.format(sqrt((AB + AC + BC) * (AB + AC - BC) * (AB + BC - AC) * (AC + BC - AB)) / 4)

t = int(input())
arr=[]
i=0
for j in range(t):
    arr.extend([float(x) for x in input().split()])
#for j in range(t):
    res = Triangle(Point(arr[i],arr[i+1]),Point(arr[i+2],arr[i+3]),Point(arr[i+4],arr[i+5]))
    i+=6
    print(res.triangleArea())