def solve():
    n, m  = map(int, input().split())
    a, b = [], []
    for i in range(n):
        a.append([int(j) for j in input().split()])
    for i in range(3):
        b.append([int(j) for j in input().split()])
    
    ans = 0

    for i in range(n - 2):
        for j in range(m - 2):
            for k in range(3):
                for h in range(3):
                    ans += a[i + k][j + h] * b[k][h]

    print(ans)

if __name__=='__main__':
    for t in range(int(input())):
        solve()