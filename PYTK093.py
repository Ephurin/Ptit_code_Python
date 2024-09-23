sol = []

for t in range(int(input())):
    ID = 'SV0' + str(t + 1)
    s = [i.capitalize() for i in input().split()]
    a = []
    for i in range(3):
        a.append(int(input()))
    
    name = ''
    for i in s: name += i + ' '
    name = name[:-1]
    grade = a[0] * 3 + a[1] * 3 + a[2] * 2
    grade = round(grade * 100 / 8 + 0.01) / 100
    sol.append([ID, name, grade])

sol.sort(key=lambda a: (-a[2], a[0]))
for i in range(len(sol)):
    if i != 0 and sol[i][2] == sol[i - 1][2]:
        sol[i].append(sol[i - 1][3])
    else:
        sol[i].append(i + 1)

for i in sol:
    print('{} {} {:.2f} {}'.format(i[0], i[1], i[2], i[3]))
