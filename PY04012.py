class Student:
    def __init__(self, SID, name, cls):
        self.SID = SID
        self.name = name
        self.cls = cls
        self.grade = 0

    def gradeCounting(self, s):
        ans = 10
        for i in s:
            if i == 'v': ans -= 2
            elif i == 'm': ans -= 1
        if ans < 0: ans == 0
        self.grade = ans

    def __str__(self):
        if self.grade == 0:
            return '{} {} {} {} KDDK'.format(self.SID, self.name, self.cls, self.grade)
        else: return '{} {} {} {}'.format(self.SID, self.name, self.cls, self.grade)

classroom = {}
n = int(input()) 
for t in range(n):
    a = []
    for i in range(3):
        a.append(input())
    classroom[a[0]] = Student(a[0], a[1], a[2])

for t in range(n):
    a = input().split()
    classroom[a[0]].gradeCounting(a[1])

for i in classroom:
    print(classroom[i])