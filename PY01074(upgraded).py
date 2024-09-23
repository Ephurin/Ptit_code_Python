PrimeDivisibleSum = [0] * 1000001
for i in range(2, 1000001):
    if PrimeDivisibleSum[i] == 0:
        PrimeDivisibleSum[i] = i
        for j in range (i + i, 1000001, i):
            PrimeDivisibleSum[j] = i

for i in range(2, 1000001):
    PrimeDivisibleSum[i] += PrimeDivisibleSum[i // PrimeDivisibleSum[i]]
PrimeDivisibleSum[1] = 1
if __name__=='__main__':
    ans = 0
    for t in range(int(input())):
        n = int(input())
        ans += PrimeDivisibleSum[n]
    print(ans)