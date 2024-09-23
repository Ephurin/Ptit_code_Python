for t in range(int(input())):
    n = int(input())
    ans = 0
    a, b, f = [0] * n, [0] * n, [1] * n
    for i in range(n):
        a[i], b[i] = map(float, input().split())
    for i in range(n):
        for j in range(0, i):
            if a[j] < a[i] and b[j] > b[i]:
                f[i] = max(f[i], f[j] + 1)
        ans = max(ans, f[i])
    print(ans)