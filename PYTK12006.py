if __name__=='__main__':
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    diff = {}
    for i in range(n):
        diff[i] = a[i] - b[i]
    items = list(diff.items())
    items.sort(key = lambda a: a[1])
    ans = 0
    for i in items:
        if i[1] < 0:
            ans += a[i[0]]
            k -= 1
        elif i[1] >= 0 and k > 0:
            ans += a[i[0]]
            k -= 1
        else: ans += b[i[0]]
    print(ans)