if __name__=='__main__':
    s = input()
    a = []
    for i in range(0, len(s) - 1, 2):
        a.append(int(s[i : i + 2]))
    a = list(set(a))
    a.sort()
    print(*a)