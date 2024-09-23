import math
def prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0: return False
    return n > 1

for t in range(int(input())):
    n = int(input())
    print('1 ',end='')
    for i in range(2,int(math.sqrt(n))):
        tmp = 0
        while n % i == 0 and prime(i):
            n /= i
            tmp += 1
        if tmp  != 0: print('* '+str(i)+'^'+str(tmp),end=' ')
    if n > 1: print('* '+str(int(n))+'^1')
    else: print()