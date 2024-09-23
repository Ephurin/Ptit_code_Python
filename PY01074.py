from math import sqrt

prime = [True] * 2000001
prime[0], prime[1] = False, False
for i in range(2, 2000001):
    if prime[i]:
        for j in range(i * 2, 2000001, i):
            prime[j] = False

def divisibleSum(n):
    sum = 0
    if prime[n]: pass
    else:
        for i in range(2, int(sqrt(n)) + 1):
            while n % i == 0:
                n //= i
                sum += i
    if n != 1: sum += n
    return sum

if __name__=='__main__':
    ans = 0
    for t in range(int(input())):
        n = int(input())
        ans += divisibleSum(n)
    print(ans)