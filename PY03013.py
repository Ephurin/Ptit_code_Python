def count(n, k):
    n1 = n
    if n < 10:
        if n >= k: return 1
        return 0
    if k == 0:
        cnt, p, save = n // 10 + 1, 10, n % 10
        n //= 10
        while(n >= 10):
            if n % 10 == 0:
                cnt += (n // 10 - 1) * p
                cnt += save + 1
            else: cnt += (n // 10) * p
            save += (n % 10) * p
            n //= 10
            p *= 10
        return cnt
    else:
        cnt, p, save = 0, 1, 0
        while(n > 10):
            if n % 10 > k: 
                cnt += (n // 10 + 1) * p
            elif n % 10 == k:
                cnt += (n // 10) * p
                cnt += save + 1
            else:
                cnt += (n // 10) * p
            save += (n % 10) * p
            n //= 10
            p *= 10
        if n == k: cnt += int(str(n1)[1:]) + 1
        if n > k: cnt += p
        return cnt
        
for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    for i in range(10):
        print(count(b, i) - count(a - 1, i), end = ' ')
    print()