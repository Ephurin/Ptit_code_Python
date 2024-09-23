for t in range(int(input())):
    n, c, d = map(int, input().split())
    a = [int(i) for i in input().split()]
    if c > d: c, d = d, c
    a.sort(reverse=True)
    csum, dsum = 0, 0
    for i in range(c + d):
        if i < c: csum += a[i]
        else: dsum += a[i]
    if c == 0: c = 1
    if d == 0: d = 1
    ans = csum / c + dsum / d
    print('{:.6f}'.format(ans))