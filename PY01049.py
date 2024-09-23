import math

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return n > 1

def valid(n):
    countPrime = 0
    countNonPrime = 0
    for c in n:
        if c in '2 3 5 7'.split(): countPrime += 1
        else: countNonPrime += 1
    return countPrime > countNonPrime

for t in range(int(input())):
    string = input()
    if valid(string) and prime(len(string)): print('YES')
    else: print('NO')