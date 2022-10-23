from math import *
def ispm(n):
    if n<2:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if(n%i==0):
            return False
    return True
def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())

if(ispm(n)):
    k=rev(n)
    if(ispm(k)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")