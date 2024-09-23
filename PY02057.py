if __name__=='__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append([int(i) for i in input().split()])
    maxx, minn, loc = 0, 10000, []
    for i in range(n):
        for j in range(m):
            maxx = max(a[i][j], maxx)
            minn = min(a[i][j], minn)
    ans = maxx - minn
    for i in range(n):
        for j in range(m):
            if a[i][j] == ans:
                loc.append([i, j])
    if len(loc) == 0: print('NOT FOUND')
    else:
        print(ans)
        for i in loc:
            print('Vi tri [{}][{}]'.format(i[0], i[1]))