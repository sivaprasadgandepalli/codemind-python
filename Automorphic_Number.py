from math import *
def length(n):
    c=0
    while n>0:
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())
sq=n**2
l=length(n)
if((sq%10**l)==n):
    print("Automorphic Number")
else:
     print("Not an Automorphic Number")
