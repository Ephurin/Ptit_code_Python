ans, lans = '', 0
for i in input().split():
    if len(i) > lans:
        ans, lans = i, len(i)
print(ans, lans)