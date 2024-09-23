s = {}
for i in range(int(input())):
    a = input().split()
    tmp = 0
    if a[3] == 'IN':
        if a[1] == 'Xe_con':
            if a[2] == '5': tmp = 10000
            if a[2] == '7': tmp = 15000
        elif a[1] == 'Xe_tai': tmp = 20000
        elif a[1] == 'Xe_khach': 
            if a[2] == '29': tmp = 50000
            if a[2] == '45': tmp = 70000
    if a[4] in s: s[a[4]] += tmp
    else: s[a[4]] = tmp

for key, value in s.items():
    print(key + ':', value)