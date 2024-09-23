if __name__=='__main__':
    s = input()
    n = int(input())
    ans = {}
    while len(s) >= 2:
        a = int(s[0:2])
        s = s[2:]
        if a in ans:
            ans[a] += 1
        else: ans[a] = 1
    ans = list(ans.items())
    ans.sort(key = lambda a: a[0])
    ok = False
    for i in ans:
        if i[1] >= n:
            ok = True
            print(i[0], i[1])
    if not ok: print('NOT FOUND')