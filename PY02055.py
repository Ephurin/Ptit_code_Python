prime = [True] * 10001
prime[0], prime[1] = False, False
for i in range(2, 10001):
    if prime[i]:
        for j in range(i*2, 10001, i):
            prime[j] = False

if __name__=='__main__':
    n, m = [int(i) for i in input().split()]
    a, loc, ans = [], [], 0 
    for i in range(n):
        a.append([int(j) for j in input().split()])
    for i in range(n):
        for j in range(m):
            if prime[a[i][j]]:
                if a[i][j] > ans:
                    loc = []
                    ans = a[i][j]
                    loc.append((i, j))
                elif a[i][j] == ans:
                    loc.append((i, j))
    if ans == 0: print('NOT FOUND')
    else:
        print(ans)
        for i in loc:
            print('Vi tri [{}][{}]'.format(i[0], i[1]))