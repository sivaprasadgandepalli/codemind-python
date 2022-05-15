from math import *
def prime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
d=list(map(int,input().split()))
k=int(input())
c=0
for i in range(0,len(d)):
   if prime(d[i]):
       if d[i]>=k:
           c+=1
           
print(c)