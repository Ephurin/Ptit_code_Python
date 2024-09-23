if __name__=='__main__':
    for t in range(int(input())):
        n = int(input())
        a = sorted([int(i) for i in input().split()])
        ans = 0
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while(l - r):
                tmp = a[i] + a[l] + a[r]
                if not tmp:
                    ans += 1
                    l += 1
                elif tmp < 0:
                    l += 1
                else: r -= 1
        print(ans)