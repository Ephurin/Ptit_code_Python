def prime(n):
    if n==1:
        return 0
    for i in range (2,round(n**0.5+1)):
        if n%i==0:
            return 0
    return 1
t=int(input())
for i in range(t):
    n=int(input())
    if prime(n)==0:
        print("NO")
    else: print("YES")