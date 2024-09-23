import math
def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

m, n = map(int,input().split())
a = []
for i in range(m):
    a.append([])
    a[i] = input().split()

for i in range(m):
    for j in range(n):
        if prime(int(a[i][j])): print(1, end = ' ')
        else: print(0, end = ' ')
    print()