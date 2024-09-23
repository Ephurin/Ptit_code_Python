n = int(input())
a = []
for i in range(n - 1):
    a.append(int(input()))
a.sort()
Found = False
for i in range(1, n):
    if a[i - 1] != i:
        Found = True
        print(i)
        break
if not Found: print(n)