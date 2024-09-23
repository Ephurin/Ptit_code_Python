def digitsum(n):
    k=0
    while n>0:
        k+=n%10
        n//=10
    return k
def gsum(n):
    i=2
    k=0
    while i<=n:
        if n%i==0:
            k+=digitsum(i)
            n//=i
        else: i+=1
    return k
t=int(input())
for i in range(t):
    n=int(input())
    if gsum(n)==digitsum(n):
        print("YES")
    else : print("NO")

