fibo = [0] * 94
fibo[1] = 1
for i in range(2, 94):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

for t in range(int(input())):
    n, m = map(int,input().split())
    for i in range(n, m+1):
        print(fibo[i], end = ' ')
    print()