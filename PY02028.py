from math import sqrt

def prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

if __name__=='__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    b = []
    for i in a:
        if prime(i): b.append(i)
    b.sort()
    cnt = 0
    for i in range(len(a)):
        if prime(a[i]):
            a[i] = b[cnt]
            cnt += 1
    print(*a)