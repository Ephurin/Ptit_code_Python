if __name__=='__main__':
    n = int(input())
    a = []
    while(len(a) < n):
        a += [int(i) for i in input().split()]
    ans = []
    for i in range(1, a[n - 1]):
        if i not in a: ans.append(i)
    if len(ans) == 0: print('Excellent!')
    else:
        for i in ans: print(i)