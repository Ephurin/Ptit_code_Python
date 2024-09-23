if __name__=='__main__':
    a = [i.lower() for i in input().split()]
    b = [i.lower() for i in input().split()]
    a = list(set(a))
    b = list(set(b))
    c = a + b
    c = list(set(c))
    c.sort()
    d = []
    for i in a:
        if i in b: d.append(i)
    d.sort()
    print(*c)
    print(*d)