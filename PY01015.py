def valid(string):
    for i in range(len(string)-1):
        if int(string[i]>string[i+1]): return False
    return True

for i in range(int(input())):
    string = input()
    if valid(string): print('YES')
    else: print('NO') 