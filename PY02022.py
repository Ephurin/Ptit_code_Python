from math import sqrt

def prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

if __name__=='__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    m = {}
    for i in a:
        if prime(i):
            if i in m:
                m[i] += 1
            else: m[i] = 1
    for key in m:
        print(key, m[key], sep = ' ')