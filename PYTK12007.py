for t in range(int(input())):
    n = int(input())
    u = float(input())
    a = [float(i) for i in input().split()]
    b = [0] * n
    b[0] = a[0]
    a.sort()
    for i in range(1, n):
        b[i] += b[i - 1] + a[i]
    mark = -1
    for i in range(n - 1):
        if b[i] + u < a[i + 1] * (i + 1):
            mark = i
            break
    ans = 0
    if mark == -1:
        ans = (b[n - 1] + u) / n
        if ans > 1: ans = 1
        else: ans = ans ** n
    else:
        ans = (b[mark] + u) / (mark + 1)
        ans = ans ** (mark + 1)
        for i in range(mark + 1, n):
            ans *= a[i]
    print('{:.6f}'.format(ans))