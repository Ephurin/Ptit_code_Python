def thuannghich(n):
    k=n
    h=0
    while k>0:
        h=h*10+k%10
        k//=10
    if n==h:
        return 1
    return 0
def ngto(n):
    if n==1:
        return 0
    for i in range(2,round(n**0.5+1)):
        if n%i==0:
            return 0
    return 1
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    dem=0
    for j in range(a,b+1):
        if ngto(j)==1 and thuannghich(j)==1:
            print(j,end=" ")
            dem+=1
            if dem%10==0:
                print()
    print()