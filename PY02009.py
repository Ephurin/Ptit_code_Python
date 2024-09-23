for t in range(int(input())):
    count = [0]*1001
    N = int(input())
    maxx = 0
    for i in range(N):
        k = int(input())
        count[k] += 1
        maxx = max(maxx, count[k])
    for i in range(1001):
        if count[i] == maxx:
            print(i)
            break