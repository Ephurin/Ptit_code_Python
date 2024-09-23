def valid(n):
    tmp = 0
    for c in n:
        tmp += int(c)
    return tmp % 3 == 0

for t in range(int(input())):
    string = input()
    if valid(string): print('YES')
    else: print('NO')