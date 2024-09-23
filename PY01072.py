n, k = map(int, input().split())
a = [i for i in range(0, k + 1)]
def sinh():
    i = k
    while i > 0 and a[i] == i + n - k:
        i -= 1
    if i == 0:  return False
    else:
        a[i] += 1
        for j in range(i + 1, k + 1):
            a[j] = a[j - 1] + 1
    return True

b = [int(i) for i in input().split()]
b = list(set(b))
b.sort()
n = len(b) 
for i in range(1, k+1):
    print(b[a[i] - 1], end = ' ')
print()
while sinh():
    for i in range(1, k+1):
        print(b[a[i] - 1], end = ' ')
    print()