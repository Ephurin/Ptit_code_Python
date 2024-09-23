for t in range(int(input())):
    n = int(input())
    a, f = [], 1
    for i in range(n):
        a.append(tuple(map(int, input().split())))
    a.sort(key = lambda a: a[1])
    mark = a[0][1]
    for i in range(1, n):
        if a[i][0] >= mark:
            f += 1
            mark = a[i][1]
    print(f)