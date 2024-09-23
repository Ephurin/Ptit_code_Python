if __name__=='__main__':
    n = input()
    a = {}
    for i in range(0, len(n)-1, 2):
        tmp = int(n[i : i + 2])
        if tmp not in a:
            a[tmp] = 1
        else: a[tmp] += 1
    for i in a:
        print(i, a[i])