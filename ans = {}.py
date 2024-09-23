ans  = {}
a = []
def cmp(a):
    return -a[1], a[0]
for i in range(int(input())):
    for j in input().split():
        if j not in ans:
            ans[j] = 1
        else: ans[j] += 1

for i in ans:
    a.append(i, a[i])

a.sort(key = def)
for i in a: print(i[0], i[1])