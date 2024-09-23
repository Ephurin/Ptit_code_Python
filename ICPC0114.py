from math import sqrt

def prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

def reverseNumber(n):
    return int(str(n)[::-1])

def perfectPrime(n):
    if not (prime(n) and prime(reverseNumber(n))): return False
    for i in str(n):
        if not(prime(int(i))): return False
    return True

def solve():
    n = int(input())
    if perfectPrime(n): print('Yes')
    else: print('No')

if __name__=='__main__':
    for t in range(int(input())):
        solve()