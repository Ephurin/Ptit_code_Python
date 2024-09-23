prime = [1] * 10001
prime_num = []
for i in range(2, 10001):
    if prime[i]:
        prime_num.append(i)
        for j in range(i + i, 10001, i):
            prime[j] = 0

n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for i in a:
    s = 10**9
    for j in prime_num:
        s = min(s, abs(i - j))
    ans = max(ans, s)

print(ans)