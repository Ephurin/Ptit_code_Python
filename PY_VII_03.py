n = int(input())
a = []
for i in range(n):
    a.append([0]*n)

for i in range(n):
    for j in range(n):
        a[i][j] = abs(i - j)

for i in a:
    print(*i)