a, k, n = map(int, input().split())
ans = []
mark = 0
for i in range(n - a + 1):
    if (a + i) % k == 0 and i != 0:
        mark = i
        break
for i in range(mark, n - a + 1, k):
    if i != 0: ans.append(i)
    
if len(ans) == 0: print(-1)
else: print(*ans)