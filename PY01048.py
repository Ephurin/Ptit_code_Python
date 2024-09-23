from math import sqrt

if __name__=='__main__':
    for t in range(int(input())):
        n = int(input()) * 2
        ans = 0
        for i in range(2, int(sqrt(n) + 1)):
            if n % i == 0:
                if (n / i - i + 1) % 2 == 0:
                    ans += 1
        print(ans)