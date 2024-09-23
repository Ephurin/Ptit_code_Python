def valid(inin):
    tmp = 0
    for i in range(len(inin)-1):
        if int(inin[i]) >= int(inin[i + 1]):
            tmp = i
            break
    if tmp == 0: return False
    for i in range(tmp, len(inin)-1):
        if int(inin[i]) <= int(inin[i + 1]): return False
    return True

for i in range(int(input())):
    inin = input()
    if valid(inin): print('YES')
    else: print('NO')