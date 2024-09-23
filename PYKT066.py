from math import gcd
def solve():
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    f = [0] * n
    for i in range(n):
        if a[i] == k:
            if i == 0: f[i] = 1
            else: f[i] = f[i - 1] + 1
        elif a[i] % k == 0:
            if i == 0: f[i] = 1
            else:
                tmp = f[i - 1]
                mark = i - 1
                while tmp > 0:
                    if gcd(a[i], a[mark]) == k: f[i] += 1
                    else: break
                    tmp -= 1
        else: f[i] = 0
    print(*f)

if __name__=='__main__':
    for t in range(int(input())):
        solve()