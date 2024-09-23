class participant:
    def __init__(self, name, division, arrivalTime):
        self.name = name
        self.division = division
        self.arrivalTime = arrivalTime
    
    def travelingTime(self):
        if len(self.arrivalTime) == 4:
            hour = int(self.arrivalTime[0])
        else: hour = int(self.arrivalTime[0:2])
        minute = int(self.arrivalTime[-2:])
        travelingTime = (hour - 6) * 60 + minute 
        return travelingTime / 60
    
    def ID(self):
        a = []
        a += self.division.split()
        a += self.name.split()
        ID = ''
        for i in a:
            ID += i[0]
        return ID
    
    def speed(self):
        return 120 / self.travelingTime()

def cmp(a):
    return -a.speed()

if __name__=='__main__':
    a = []
    for i in range(int(input())):
        name = input()
        division = input()
        time = input()
        tmp = participant(name, division, time)
        a.append(tmp)
    a.sort(key = cmp)
    for i in a:
        print('{} {} {} {} Km/h'.format(i.ID(), i.name, i.division, round(i.speed())))