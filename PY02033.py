if __name__=='__main__':
    s = input()
    a = []
    for i in range(0, len(s) - 1, 2):
        tmp = int(s[i : i + 2])
        if tmp not in a: a.append(tmp)
    print(*a)