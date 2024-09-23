def Try(n, k, name, tmp, i):
    if len(tmp) == k:
        print(*tmp)
    else:
        for j in range(i, n):
            tmp.append(name[j])
            Try(n, k, name, tmp, j + 1)
            tmp.pop()

n, k = map(int, input().split())
name = []
while len(name) < n:
    name += [i for i in input().split()]
name = list(set(name))
name.sort()
n = len(name)
Try(n, k, name, [], 0)