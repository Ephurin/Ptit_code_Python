for t in range(int(input())):
    n = int(input())
    cnt = 0
    while(n > 10):
        n /= 10
        n = round(n + 0.01)
        cnt += 1
    n = n * (10 ** cnt)
    print(n)