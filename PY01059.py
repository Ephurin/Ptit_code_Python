def digitsSum(n):
    tmp = 0
    for i in range(1,len(n),2):
        tmp += int(n[i])
    return tmp

def digitsTimes(n):
    tmp = 1
    isOK = False
    for i in range(0,len(n),2):
        if n[i] == '0': continue
        else: isOK = True
        tmp *= int(n[i])
    if isOK: return tmp
    return 0

for i in range(int(input())):
    string = input()
    print(digitsTimes(string), digitsSum(string), sep=' ')