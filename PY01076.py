import math
for i in range(int(input())):
    divNum = int(input())
    divdNum = input()
    tmpNum = ''
    for c in divdNum:
        tmpNum += c
        tmpNum = str(int(tmpNum) % divNum)
    print(math.gcd(int(tmpNum), divNum))