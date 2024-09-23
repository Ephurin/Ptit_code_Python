def valid(n):
    if n < 10: return False
    return n == int(str(n)[::-1])

if __name__=='__main__':
    n, m = [int(i) for i in input().split()]
    a, loc, ans = [], [], -1 
    for i in range(n):
        a.append([int(j) for j in input().split()])
    for i in range(n):
        for j in range(m):
            if valid(a[i][j]):
                if a[i][j] > ans:
                    loc = []
                    ans = a[i][j]
                    loc.append((i, j))
                elif a[i][j] == ans:
                    loc.append((i, j))
    if ans == -1: print('NOT FOUND')
    else:
        print(ans)
        for i in loc:
            print('Vi tri [{}][{}]'.format(i[0], i[1]))