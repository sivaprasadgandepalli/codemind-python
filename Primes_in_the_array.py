from math import *
def isprime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
d=list(map(int,input().split()))
c=0
for i in range(0,len(d)):
    if isprime(d[i]):
        c+=1
    else:
        c=c
print(c)