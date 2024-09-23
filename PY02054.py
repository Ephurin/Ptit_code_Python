n, m = map(int, input().split())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

if n > m:
    mark = 0
    while len(a) > m:
        a = a[:mark] + a[mark + 1:]
        mark += 1
    
elif m > n:
    mark = 1
    while len(a[0]) > n:
        for i in range(n):
            a[i] = a[i][:mark] + a[i][mark + 1:]
        mark += 1

for i in a:
    print(*i)