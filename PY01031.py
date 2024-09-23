board = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for t in range(int(input())):
    n, k = map(int, input().split())
    ans = ''
    while n > 0:
        ans = board[n % k] + ans
        n //= k
    print(ans)