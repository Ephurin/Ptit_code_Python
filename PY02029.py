n, m = map(int, input().split())
a = [int(i) for i in input().split()]
ans = {}
for i in range(1, m + 1):
    ans[i] = 0

for i in a:
    ans[i] += 1

ans = list(ans.items())
ans.sort(key=lambda a: (-a[1], a[0]))
ok = False
for i in range(1, m):
    if ans[i][1] < ans[i - 1][1] and ans[i][1] > 0: 
        print(ans[i][0])
        ok = True
        break

if not ok: print('NONE')