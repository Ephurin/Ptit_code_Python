n = int(input())
a = [int(x) for x in input().split()]
s = 10 ** 9
for i in a:
    tmp = 0
    for j in a:
        tmp += abs(i - j)
    if s > tmp:
        s = tmp
        p = i

print(s, p)