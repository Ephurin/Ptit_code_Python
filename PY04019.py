class participant:
    def __init__(self, ID, name, lt, th):
        self.name = name
        self.lt = lt
        self.th = th
        self.ID = ID

    def avg(self):
        if self.lt > 10: self.lt /= 10
        if self.th > 10: self.th /= 10
        return (self.th + self.lt) / 2
    
    def grade(self):
        if self.avg() > 9.5: return 'XUAT SAC'
        elif self.avg() >= 8: return 'DAT'
        elif self.avg() >= 5: return 'CAN NHAC'
        else: return 'TRUOT'

def cmp(a):
    return -a.avg()

if __name__=='__main__':
    a = []
    for t in range(1, int(input()) + 1):
        ID = 'TS0{}'.format(t)
        name = input()
        lt = float(input())
        th = float(input())
        tmp = participant(ID, name, lt, th)
        a.append(tmp)
    a.sort(key = cmp)
    for i in a:
        print('{} {} {:.2f} {}'.format(i.ID, i.name, i.avg(), i.grade()))