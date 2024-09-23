def valid(n):
    tmp = 0
    for c in n:
        tmp += int(c)
    tmp = str(tmp)
    return tmp == tmp[::-1] and len(tmp) > 1

for t in range(int(input())):
    string = input()
    if valid(string): print('YES')
    else: print('NO')