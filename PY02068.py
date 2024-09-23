if __name__=='__main__':
    for t in range(int(input())):
        n, m, k = map(int, input().split())
        a, kernel, ans = [], [], []
        for i in range(n):
            a.append([int(j) for j in input().split()])
        for i in range(k):
            kernel.append([1] * k)
        for i in range(n - k + 1):
            ans.append([0] * (m - k + 1))

        for i in range(n - k + 1):
            for j in range(m - k + 1):
                for x in range(k):
                    for y in range(k):
                        ans[i][j] += a[i + x][j + y] * kernel[x][y]
                ans[i][j] //= (k * k)
                
        
        for i in ans: print(*i)