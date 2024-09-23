class student:
    
    def __init__(self, name, dob, firstPoint, secondPoint, thirdPoint):
        self.name = name
        self.dob = dob
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint
        self.thirdPoint = thirdPoint
    
    def agv(self):
        avgPoint = self.firstPoint + self.secondPoint + self.thirdPoint
        return avgPoint

    def printing(self):
        print(self.name, self.dob, '{:.1f}'.format(self.agv()))

if __name__=='__main__':
    Input = []
    for i in range(5):
        Input.append(input())
    for i in range(2, 5):
        Input[i] = float(Input[i])
    student1 = student(Input[0], Input[1], Input[2], Input[3], Input[4])
    student1.printing()