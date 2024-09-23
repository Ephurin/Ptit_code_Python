prime = [True] * 32000
prime[0], prime[1] = False, False
for i in range(2, 32000):
    if prime[i]:
        for j in range(i + i, 32000, i):
            prime[j] = False
PrimeNum = []
for i in range(2, 32000):
    if prime[i]: PrimeNum.append(i**2)

if __name__=='__main__':
    ans = 0
    n = int(input())
    i, isOK = 0, True
    while i < len(PrimeNum) and isOK:
        if PrimeNum[i]**4 <= n: ans += 1
        j = i + 1
        isOK = False
        while j < len(PrimeNum):
            if PrimeNum[i] * PrimeNum[j] <= n:
                ans += 1
                isOK = True
            else: break
        i += 1
        if PrimeNum[i] < 32000: break
    print(ans)