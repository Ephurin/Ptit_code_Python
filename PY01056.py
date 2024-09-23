import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

def valid(n):
    tmp = 0
    for i in range(len(n)):
        tmp += int(n[i])
        if (i % 2 == 1 and int(n[i]) % 2 == 0) or (i % 2 == 0 and int(n[i]) % 2 == 1): return False
    return prime(tmp)

for t in range(int(input())):
    string = input()
    if valid(string): print('YES')
    else: print('NO')
