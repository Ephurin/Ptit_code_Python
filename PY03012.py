ans = []

def cmp(a):
    return -a[1], a[2], a[0]

for t in range(int(input())):
    name = input()
    accepted, submited = map(int, input().split())
    a = [name, accepted, submited]
    ans.append(a)

ans.sort(key = cmp)

for i in ans:
    print(*i)