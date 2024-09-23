ans = []

def Try(n, a, k):
    if sum(a) == k:
        b = a.copy()
        ans.append(b)
    elif sum(a) < k:
        for i in range(n, 0, -1):
            a.append(i)
            Try(i, a, k)
            a.pop() 

for t in range(int(input())):
    n = int(input())
    ans.clear()
    Try(n, [], n)
    print(len(ans))
    for i in ans:
        print('(', end = '')
        print(*i, end = '')
        print(')', end = ' ')
    print()

