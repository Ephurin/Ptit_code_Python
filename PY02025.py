if __name__=='__main__':
    n, m = map(int, input().split())
    a = set([int(i) for i in input().split()])
    b = set([int(i) for i in input().split()])
    AdifB = list(a.difference(b))
    BdifA = list(b.difference(a))
    a = list(a)
    b = list(b)
    AB = []
    for i in a:
        if i in b: AB.append(i)
    AB.sort()
    AdifB.sort()
    BdifA.sort()
    print(*AB)
    print(*AdifB)
    print(*BdifA)