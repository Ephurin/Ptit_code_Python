import os

fi = open('VANBAN.in', 'r')
a = []
for i in fi: a += i.split()
ans, maxLen = {}, 0
for i in a:
    if i == i[::-1]:
        if len(i) > maxLen:
            maxLen = len(i)
            ans.clear()
            ans[i] = 1
        elif len(i) == maxLen:
            if i not in ans: ans[i] = 1
            else: ans[i] += 1

for i in ans:
    print(i, ans[i])

fi.close()