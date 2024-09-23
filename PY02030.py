from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0: return False
    return n > 1

n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
    if i not in b: b.append(i)
for i in range(1, len(b)):
    b[i] += b[i - 1]
k = len(b) - 1
ok = False
for i in range(k):
    if isPrime(b[i]) and isPrime(b[k] - b[i]):
        ok = True
        print(i)
        break
if not ok: print('NOT FOUND')