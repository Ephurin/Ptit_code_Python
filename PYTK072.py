a = []
for i in range(int(input())):
    a.append(input())
s = a[0]
m, ok, ans = len(s), 1, 10**9

for i in range(m):
    tmp = 0
    for j in range(len(a)):
        x = a[j]
        for k in range(m):
            if x == s: 
                tmp += k
                break
            x = x[1:] + x[0]
        if x != s: ok = 0
    ans = min(tmp, ans)
    s = s[1:] + s[0]

if ok == 0: print(-1)
else: print(ans)
        