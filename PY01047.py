import math

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return n > 1

for i in range(int(input())):
    string = input()
    n = string[len(string)-4:]
    if prime(int(n)): print('YES')
    else: print('NO')