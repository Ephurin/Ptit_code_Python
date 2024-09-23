prime = [True] * 1000001
for i in range(2,   1000001):
    if prime[i]:
        for j in range(2 * i, 1000001, i):
            prime[j] = False

def solve():
    n = int(input())
    visited = [False] * 1000001
    for i in range(13, n):
        if prime[i] and prime[int(str(i)[::-1])] and not visited[i] and i != int(str(i)[::-1]) and int(str(i)[::-1]) < n:
            print(i, int(str(i)[::-1]), sep = ' ', end = ' ')
            visited[i], visited[int(str(i)[::-1])] = True, True

if __name__=='__main__':
    for t in range(int(input())):
        solve()
        print()