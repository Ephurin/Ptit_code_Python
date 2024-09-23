def prime(n):
    if n==1:
        return False
    for i in range(2,round(n**0.5+1)):
        if n%i==0:
            return False
    return True
t=int(input())
for i in range(t):
    n=int(input())
    for j in range(1,n//2+1):
        if prime(j) and prime(n-j):
            print(j,n-j,sep=' ')
            break