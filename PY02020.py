if __name__=='__main__':
    n = int(input())
    a = [float(i) for i in input().split()]
    tmp, cnt = 0, 0
    a.sort()
    for i in a:
        if i != a[0] and i != a[n - 1]:
            tmp += i
            cnt += 1
    
    print('{:.2f}'.format(tmp / cnt))
    