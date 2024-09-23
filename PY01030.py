import math

n, k = map(int,input().split())
beg = pow(10, k-1)
end = pow(10, k)
cnt = 0
for i in range(beg, end):
    if math.gcd(n, i) == 1:
        print(i,end=' ')
        cnt += 1
    if cnt == 10:
        cnt = 0
        print()