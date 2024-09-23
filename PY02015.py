def valid(a):
    for i in a:
        if i != 0: return True
    return False

def isTheSame(a):
    for i in range(len(a)-1):
        if a[i] != a[i + 1]: return False
    return True

while True:
    a = [int(i) for i in input().split()]
    b = [0] * 4
    if not valid(a): break
    else:
        ans = 0
        while(not isTheSame(a)):
            ans += 1
            for j in range(4):
                if j == 3: b[3] = abs(a[3] - a[0])
                else: b[j] = abs(a[j] - a[j + 1])
            a = b
            b = [0] * 4
            
        print(ans)