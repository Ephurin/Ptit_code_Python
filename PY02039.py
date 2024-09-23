if __name__=='__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(i) for i in input().split()])
    k = int(input())
    upperSum, lowerSum = 0, 0
    for i in range(n):
        for j in range(n):
            if i < j: upperSum += a[i][j]
            if i > j: lowerSum += a[i][j]
    ans = abs(upperSum - lowerSum)
    if ans <= k: print('YES')
    else: print('NO')
    print(ans)