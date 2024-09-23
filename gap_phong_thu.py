def solve(n, m, h, w):
    ans = 0
    while n > h: 
        ans += 1
        h <<= 1
    while m > w:
        ans += 1
        h <<= 1
    return ans

if __name__=='__main__':
    n, m, h, w = [int(i) for i in input().split()]
    print (min(solve(n, m, h, w), solve(m, n, h, w)))
