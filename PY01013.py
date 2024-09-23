import math
def prime(n):
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return n > 1

for t in range(int(input())):
    a, b = map(int, input().split())
    c = math.gcd(a, b)
    c = str(c)
    ans = 0
    for i in c:
        ans += int(i)
    if prime(ans): print('YES')
    else: print('NO')