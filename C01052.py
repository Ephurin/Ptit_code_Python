i=int(input())
import math
for j in range(i):
    n=int(input())
    dem=0
    for k in range(1,int(n**0.5)+1):
        if n%k==0:
            if(k%2==0):dem+=1
            if (n//k) !=k and (n//k)%2==0 : dem+=1
    print(dem)