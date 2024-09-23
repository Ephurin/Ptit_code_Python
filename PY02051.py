n = int(input())
ans, a = [], []
for i in range(n): a.append([int(j) for j in input().split()])
if n == 2:
    tmp = a[1][0] // 2
    print(tmp, tmp)

elif n == 3:
    tmp = (a[0][1] + a[1][2] + a[0][2]) // 2
    print(tmp - a[1][2], tmp - a[0][2], tmp - a[0][1])

else:
    ans.append((a[0][1] + a[0][2] - a[1][2]) // 2)
    ans.append((a[1][2] + a[1][3] - a[2][3]) // 2)
    for i in range(2, n):
        ans.append((a[0][i] + a[1][i] - a[0][1]) // 2)
    
    print(*ans)