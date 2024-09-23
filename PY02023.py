def digitSum(n):
    tmp = str(n)
    a = sum(int(i) for i in tmp)
    return (a, n)

if __name__=='__main__':
    for t in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        a.sort(key=digitSum)
        print(*a)