def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [1] * n
    for i in range(1, n):
        k = i - 1
        while k >= 0:
            if a[i] >= a[k]:
                b[i] += b[k]
                k -= b[k]
            else: break
    print(*b)

if __name__=='__main__':
    for t in range(int(input())):
        solve()