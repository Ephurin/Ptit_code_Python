n = int(input())
a = sorted([int(i) for i in input().split()])
print(max(a[0] * a[1], a[-1] * a[-2], a[0] * a[1] * a[-1], a[-1] * a[-2] * a[-3]))