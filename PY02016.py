def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    if len(a) == 1: print(a[0])
    else:
        m, ans, maxFre = {}, a[0], 1
        for i in a:
            if i in m:
                m[i] += 1
                if m[i] > maxFre:
                    ans, maxFre = i, m[i]
            else:
                m[i] = 1
        if maxFre * 2 > len(a): print(ans)
        else: print('NO')

if __name__=='__main__':
    for t in range(int(input())):
        solve()