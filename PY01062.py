import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

def valid(n):
    primeCount = 0
    nonPrimeCount = 0
    for i in n:
        if i in '2 3 5 7'.split(): primeCount += 1
        else: nonPrimeCount += 1
    return prime(len(n)) and primeCount > nonPrimeCount

for i in range(int(input())):
    string = input()
    if valid(string): print('YES')
    else: print('NO')