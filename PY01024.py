def valid1(n):
    sum = 0
    for c in n:
        sum += int(c)
    return sum % 10 == 0

def valid2(n):
    for i in range(len(n)-1):
        tmp = int(n[i]) - int(n[i+1])
        if tmp != 2 and tmp != -2: return False
    return True

for i in range(int(input())):
    string = input()
    if valid1(string) and valid2(string): print('YES')
    else: print('NO')