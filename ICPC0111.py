for t in range(int(input())):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    print(*(a[k:] + a[:k]))