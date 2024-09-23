import math

def reverse_num(n):
    tmp = 0
    while n > 0:
        tmp = tmp * 10 + n % 10
        n //= 10
    return tmp

for i in range(int(input())):
    n = int(input())
    rev = reverse_num(n)
    if math.gcd(n, rev) == 1:
        print('YES')
    else: print('NO')