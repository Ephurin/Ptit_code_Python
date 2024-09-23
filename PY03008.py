mp, n = {}, int(input())

for t in range(n - 1):
    a = [int(i) for i in input().split()]
    for i in a:
        if i in mp: mp[i] += 1
        else: mp[i] = 1
ok = True
for i in range(1, n + 1):
    if i not in mp or (mp[i] != 1 and mp[i] != n - 1):
        print('No')
        ok = False
        break
if ok: print('Yes')