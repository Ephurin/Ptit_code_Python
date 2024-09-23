n, m = map(int, input().split())
ans = 0
a, q, b = [], [], [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
for i in range(n):
    a.append([int(i) for i in input().split()])
    for j in range(m):
        if a[i][j] == -1: q.append([i, j])

for i in q:
    for j in b:
        x, y = i[0] + j[0], i[1] + j[1]
        if x >= 0 and x < n and y >= 0 and y < m:
            ans += a[x][y]
            a[x][y] = 0

print(ans)