n = int(input())
a = []
row_count = [0]*n
col_count = [0]*n

for i in range(n):
    a.append(input())

for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            row_count[i] += 1
            col_count[j] += 1

ans = 0
for i in row_count:
    ans += i * (i - 1) / 2
for i in col_count:
    ans += i * (i - 1) / 2

print(int(ans))