if __name__=='__main__':
    m, n = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = list(set(a))
    b = list(set(b))
    OK = True
    for i in a:
        if i not in b:
            print('NO')
            OK = False
            break
    if OK: print('YES')