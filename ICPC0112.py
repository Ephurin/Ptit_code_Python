MAX = int(1e6 + 1)
prime = [True] * MAX

prime[0], prime[1] = False, False
for i in range(2, MAX):
    if prime[i]:
        for j in range(i * 2, MAX, i):
            prime[j] = False

for t in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(2, n - 5):
        if prime[i] and prime[i + 6]:
            if prime[i + 2] or prime[i + 4]: ans += 1

    print(ans)