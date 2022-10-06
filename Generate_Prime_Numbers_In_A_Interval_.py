from math import *
def isprime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if(n%i==0):
            return False
    return True
m=int(input())
n=int(input())
for i in range(m,n+1):
    if(isprime(i)):
        print(i)
