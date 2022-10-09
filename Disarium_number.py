import math
def isdis(n):
    s=0
    org=n
    i=int(math.log10(n)+1)
    while n>0:
        r=n%10
        s=s+r**i
        n=n//10
        i-=1
    if(org==s):
        return True
    else:
        return False
m=int(input())
if(isdis(m)):
    print("True")
else:
    print("False")