def valid(n):
    for i in range(0,len(n)-2,2):
        if n[i] != n[i + 2]: return False
    return n[0] != n[1] and len(n) % 2 == 1

for t in range(int(input())):
    string = input()
    if valid(string): print('YES')
    else: print('NO')