import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

def valid(n):
    l = len(n)
    if prime(int(n[:3])) and prime(int(n[l-3:])): return 'YES'
    return 'NO'

for i in range(int(input())):
    string = input()
    print(valid(string))