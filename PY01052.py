import math

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return n > 1

def valid(n):
    tmp = 0
    for c in n:
        tmp += int(c)
    if prime(tmp): return 'YES'
    else: return 'NO'

for t in range(int(input())):
    string = input()
    print(valid(string))