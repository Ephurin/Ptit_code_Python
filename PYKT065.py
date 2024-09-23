prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def valid(k, n):
    for i in range(len(prime)):
        if prime[i] > n: break
        if k % prime[i] == 0: return False
    return True

while True:
    a = input()
    if a == '-1': break
    else:
        l, r = map(int, a.split())
        n = int(input())
        ans = 0
        for k in range(l, r + 1):
            if valid(k, n): ans += 1
        print(ans)