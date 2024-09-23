def valid(n):
    for c in n:
        if int(c) % 2 == 1: return False
    return n == n[::-1] and len(str(n)) % 2 == 0

for t in range(int(input())):
    n = int(input())
    for i in range(22,n,2):
        if valid(str(i)): print(i, end = ' ')
    print()