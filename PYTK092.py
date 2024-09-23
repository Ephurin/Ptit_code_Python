class participant:

    def __init__(self, ID, name, grade, nationality, section):
        self.ID = ID
        self.name = ''
        self.grade = grade
        self.nationality = nationality
        self.section = section
        for i in name.split():
            self.name += i.capitalize() + ' '

        if self.section == 1: self.grade += 1.5
        elif self.section == 2: self.grade += 1

        if self.nationality != 'Kinh': self.grade += 1.5

    def sol(self):
        if self.grade >= 20.5: return 'Do'
        else: return 'Truot'

    def __str__(self):
        return '{} {}{:.1f} {}'.format(self.ID, self.name, self.grade, self.sol())

if __name__=='__main__':
    a = []
    for t in range(int(input())):
        ID = 'TS0' + str(t + 1)
        name = input()
        grade = float(input())
        nationality = input()
        section = int(input())
        a.append(participant(ID, name, grade, nationality, section))
    
    a.sort(key=lambda n: -n.grade)
    for i in a: print(i)