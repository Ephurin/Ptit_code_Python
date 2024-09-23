class mesuringStation:

    def __init__(self,ID ,name, start, stop, mes):
        self.name = name 
        self.ID = ID
        self.start = start
        self.stop = stop
        self.mes = mes
        self.time = (float(stop[0:2]) - float(start[0:2])) + (float(stop[-2:]) - float(start[-2:])) / 60
    
    def add(self, a, b, c):
        self.time += (float(b[0:2]) - float(a[0:2])) + (float(b[-2:]) - float(a[-2:])) / 60
        self.mes += c
    
    def ans(self):
        return self.mes / self.time

    def __str__(self) -> str:
        return '{} {} {:.2f}'.format(self.ID, self.name, self.ans())

if __name__=='__main__':
    ans = {}
    for t in range(int(input())):
        ID = 'T0' + str(len(ans) + 1)
        name = input()
        start = input()
        stop = input()
        mes = float(input())
        if name in ans:
            ans[name].add(start, stop, mes)
        else: ans[name] = mesuringStation(ID, name, start, stop, mes)

    for i in ans:
        print(ans[i])