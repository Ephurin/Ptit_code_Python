def primeDivisible(n, p):
    ans = 0
    while n % p == 0:
        n //= p
        ans += 1
    return ans

if __name__=='__main__':
    for t in range(int(input())):
        n, p = map(int, input().split())
        ans = 0
        for i in range(p, n + 1):
            ans += primeDivisible(i, p)
        print(ans)