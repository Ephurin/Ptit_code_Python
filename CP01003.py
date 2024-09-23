def ngto(n):
    if n==1:
        return 0
    for i in range(2,round(n**0.5+1)):
        if n%i==0:
            return 0
    return 1
def digitsum(n):
    k=0
    while n>0:
        k+=n%10
        n//=10
    if ngto(k)==0:
        return 0
    return 1
def primedigit(n):
    while n>0:
        k=n%10
        if k!=2 and k!=3 and k!=5 and k!=7:
            return 0
        n//=10
    return 1
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    count=0
    for j in range (a,b+1):
        if ngto(j)==1 and digitsum(j)==1 and primedigit(j)==1:
            count+=1
    print(count)