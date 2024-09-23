def solve():
    n = int(input())
    a = []
    while len(a) < n:
        a += [int(i) for i in input().split()]
    odd, even, oddCount, evenCount = [], [], 0, 0
    for i in a:
        if i % 2 == 0: even.append(i)
        else: odd.append(i)
    even.sort()
    odd.sort(reverse=True)
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] = even[evenCount]
            evenCount += 1
        else:
            a[i] = odd[oddCount]
            oddCount += 1
    print(*a)
if __name__=='__main__':
    solve()