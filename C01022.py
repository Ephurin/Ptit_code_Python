t=int(input())
while t>0:
    n=int(input())
    k=0
    while n>0:
        k+=n%10
        n//=10
    print(k)
    t=t-1