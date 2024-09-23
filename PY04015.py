class Customer:
    def __init__(self, cid, name, pre, now):
        self.cid = cid
        self.name = name
        self.pre = pre
        self.now = now
        self.consum = now - pre

    def cash(self):
        if self.consum <= 50:
            total = self.consum * 100 * 1.02
        elif self.consum <= 100:
            total = (50 * 100 + (self.consum - 50) * 150) * 1.03
        else:
            total = (50 * 100 + 50 * 150 + (self.consum - 100) * 200) * 1.05
        total = round(total)  # phải làm tròn ko sẽ WA
        return total

def cmp(a):
    return -a.cash()

if __name__=='__main__':
    a = []
    for t in range(1, int(input()) + 1):
        cid = 'KH'
        if t <= 9: cid += '0{}'.format(t)
        else: cid += '{}'.format(t)
        name = input()
        pre = int(input())
        now = int(input())
        cs = Customer(cid, name, pre, now)
        a.append(cs)
    a.sort(key = cmp)
    for i in a:
        print(i.cid, i.name, i.cash())