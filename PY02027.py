ans = []

for t in range(int(input())):
    s = input()
    tmp = ''
    for i in s + ' ':
        if i in '0123456789': tmp += i
        else:
            if tmp != '':
                ans.append(int(tmp))
                tmp = ''

ans.sort()
for i in ans: print(i)