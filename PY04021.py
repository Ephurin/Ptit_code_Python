class Customer:
    def __init__(self, ID, name, inTime, outTime):
        self.ID = ID
        self.name = name
        self.inTime = inTime
        self.outTime = outTime

    def timeCount(self):
        hour = int(self.outTime[0:2]) - int(self.inTime[0:2])
        minute = int(self.outTime[3:]) - int(self.inTime[3:])
        if minute < 0:
            minute += 60
            hour -= 1
        return (hour, minute)

    def __str__(self):
        a = self.timeCount()
        return('{} {} {} gio {} phut'.format(self.ID, self.name, a[0], a[1]))

def cmp(a):
    return a.timeCount()

if __name__=='__main__':
    a = []
    for t in range(int(input())):
        ID, name, inTime, outTime = input(), input(), input(), input()
        a.append(Customer(ID, name, inTime, outTime))
    a.sort(key = cmp, reverse = True)
    for i in a: print(i)