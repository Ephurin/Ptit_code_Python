def cmp(a):
    return (-a[1], a[0])

dictt = {}
tmp = ''
for t in range(int(input())):
    s = input().lower()
    for i in s + ' ':
        if (i >= 'a' and i <= 'z'):
            tmp += i
        elif (i >= '0' and i <= '9'):
            pass
        else:
            if tmp != '':
                if tmp in dictt: dictt[tmp] += 1
                else: dictt[tmp] = 1
                tmp = ''
a = sorted(dictt.items(), key = cmp)
for i in a:
    print(i[0], i[1])