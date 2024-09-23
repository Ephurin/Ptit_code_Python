prime = [True] * 10001
prime[1] = False
for i in range(2, 10001):
    if prime[i]:
        for j in range(i + i, 10001, i):
            prime[j] = False

primeNum = []
for i in range(10001):
    if prime[i]: primeNum.append(i)

N, X = [int(i) for i in input().split()]
tmp = X
for i in range(N + 1):
    print(tmp + primeNum[i], end = ' ')
    tmp += primeNum[i]