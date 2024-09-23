class Students:
    def __init__(self, SId, name, points):
        self.SId = SId
        self.name = name
        self.a = [float(i) for i in points.split()]
    
    def avgScore(self):
        tmp = 0
        for i in self.a:
            tmp += i
        return round((tmp + self.a[0] + self.a[1]) / 12 + 0.01, 1)

    def StuGrade(self):
        tmp = self.avgScore()
        if tmp >= 9.0: return 'XUAT SAC'
        elif tmp >= 8.0: return 'GIOI'
        elif tmp >= 7.0: return 'KHA'
        elif tmp >= 5.0: return 'TB'
        else: return 'YEU'
    

if __name__=='__main__':
    students = []
    for i in range(1, int(input()) + 1):
        SId = ''
        if i < 10: SId = 'HS0' + str(i)
        else: SId = 'HS' + str(i)
        name = input()
        points = input()
        tmpStu = Students(SId, name, points)
        students.append(tmpStu)
    cmp = lambda stu: (-stu.avgScore(), stu.SId)
    students.sort(key = cmp)
    for i in students:
        print(i.SId, i.name, '{:.1f}'.format(i.avgScore()), i.StuGrade())