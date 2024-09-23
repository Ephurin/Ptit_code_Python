for t in range(int(input())):
    n, m, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    m1, m2, m3 = 0, 0, 0
    ans = []
    while m1 < n and m2 < m and m3 < k:
        if a[m1] == b[m2] and b[m2] == c[m3]:
            ans.append(a[m1])
            m1 += 1
            m2 += 1
            m3 += 1
        elif a[m1] < b[m2]: m1 += 1
        elif b[m2] < c[m3]: m2 += 1
        elif c[m3] < a[m1]: m3 += 1
    if len(ans) == 0: print('NO')
    else: print(*ans)