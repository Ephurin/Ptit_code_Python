from math import ceil

f = [0] * 51
f[3], f[4] = 1, 1
for i in range(5, 9): f[i] = 2
for i in range(9, 17): f[i] = 3
for i in range(17, 33): f[i] = 4
for i in range(33, 51): f[i] = 5

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(n - 1):
        k = ceil(max(a[i], a[i + 1]) / min(a[i], a[i + 1]))
        ans += f[k]
    print(ans)

if __name__=='__main__':
    for t in range(int(input())):
        solve()