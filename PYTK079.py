def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    a = list(set(a))
    maxElement = a[0]
    minElement = a[0]
    for i in range(len(a)):
        maxElement = max(maxElement, a[i])
        minElement = min(minElement, a[i])
    ans = maxElement - minElement + 1 - len(a)
    print(ans)

if __name__=='__main__':
    for t in range(int(input())):
        solve()