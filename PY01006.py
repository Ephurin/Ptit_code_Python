def valid(num):
    for c in num:
        if c != '4' and c!= '7': return False
    return True

t = int(input())
for i in range (t):
    num = input()
    if valid(num): print('YES')
    else: print('NO')