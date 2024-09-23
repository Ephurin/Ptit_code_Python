import sys

n = int(input())
i, p0, s, it = 0, -1, 0, 0
v, ans = -1000000001, -1
for a in input().split():
    i += 1
    a = int(a)
    if a == 0 and p0 < 0: p0 = i
    if a < 0 and a > v: 
        v,pneg = a, i
    s += a
    if s < 0: it, s = i, 0
    elif s > ans:
        ans, q, p = s, i, it
if ans < 0:
    print(pneg, pneg, v)
elif ans == 0:
    print(p0, p0, '0')
else:
    print(p+1, q, ans)