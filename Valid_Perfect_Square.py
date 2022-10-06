from math import *
def vps(n):
    sq=int(sqrt(n))
    sq1=sqrt(n)
    if(abs(sq1-sq==0)):
        return True
    else:
        return False
n=int(input())
s=[]
for i in range(1,n+1):
    v=int(input())
    if(vps(v)):
        s.append("True")
    else:
        s.append("False")
for i in s:
    print(i)