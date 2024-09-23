import sys

from math import gcd


mp = {}
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    ucln = gcd(x, y)
    if ucln != 0:
        x //= ucln
        y //= ucln
    if (x, y) not in mp.values():
        mp[i] = (x, y)

if len(mp) == 1:
    print("No")
else:
    print("Yes")
    count = 0
    for key, value in mp.items():
        print(key+1,end=' ')
        count += 1
        if count == 3:
            break
