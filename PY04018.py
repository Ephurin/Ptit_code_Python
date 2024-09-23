class Teacher:
    def __init__(self, ID, name, prio, point1, point2):
        self.ID = ID
        self.name = name
        self.prio = prio
        self.point1 = point1
        self.point2 = point2
    
    def subject(self):
        if self.prio[0] == 'A': return 'TOAN'
        elif self.prio[0] == 'B': return 'LY'
        else: return 'HOA'

    def prioPoint(self):
        if self.prio[1] == '1': return 2.0
        elif self.prio[1] == '2': return 1.5
        elif self.prio[1] == '3': return 1.0
        else: return 0

    def point(self):
        return self.point1 * 2 + self.point2 + self.prioPoint()

    def acp(self):
        if self.point() >= 18: return 'TRUNG TUYEN'
        else: return 'LOAI'

    def __str__(self):
        return('{} {} {} {:.1f} {}'.format(self.ID, self.name, self.subject(), self.point(), self.acp()))
def cmp(a):
    return -a.point()

if __name__=='__main__':
    a = []
    for i in range(1, int(input()) + 1):
        ID = 'GV0{}'.format(i) if i <= 9 else 'GV{}'.format(i)
        name = input()
        prio = input()
        point1 = float(input())
        point2 = float(input())
        a.append(Teacher(ID, name, prio, point1, point2))
    a.sort(key = cmp)
    for i in a: print(i)