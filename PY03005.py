def cmp(a):
    return (-a[1], a[0])

dictt = {}
tmp = ''
n, k = map(int, input().split())
for t in range(n):
    s = input().lower()
    for i in s + ' ':
        if (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9'):
            tmp += i
        else:
            if tmp != '':
                if tmp in dictt: dictt[tmp] += 1
                else: dictt[tmp] = 1
                tmp = ''
a = sorted(dictt.items(), key = cmp)
for i in a:
    if i[1] >= k:
        print(i[0], i[1])