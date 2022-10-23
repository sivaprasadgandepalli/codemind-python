from math import *
n=int(input())
c=0
sq=int(sqrt(n))
for i in range(1,sq+1):
    if(i*(i+1)==n):
        print("YES")
        c=1
        break
if(c==0):
    print("NO")