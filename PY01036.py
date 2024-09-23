for t in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        ans = 0
        for i in range(2,n+1,2):
            ans += 1 / i
        print('%.6f'%ans)
    else:
        ans = 0
        for i in range(1,n+1,2):
            ans += 1 / i
        print('%.6f'%ans)