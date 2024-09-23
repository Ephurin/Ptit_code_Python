a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
if b[0] < a[0]: b[0] += 24
ans = ((b[0] - a[0]) * 60 + (b[1] - a[1])) * 60 + (b[2] - a[2])
print(ans)