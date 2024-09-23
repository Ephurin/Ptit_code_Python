n, k = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort()
ans = []
marking_point = 0
for i in range(1, len(a)):
    if a[i] - a[i - 1] > k:
        ans.append(a[marking_point : i])
        marking_point = i

ans.append(a[marking_point :])
print(len(ans))