import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

def valid(n):
    for i in range(len(n)):
        if not(prime(i) and prime(int(n[i])) or (not prime(i) and not prime(int(n[i])))): return False
    return True

for i in range(int(input())):
    string = input()
    if valid(string): print('YES')
    else: print('NO')