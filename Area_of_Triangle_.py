from math import *
m,n,k=map(int,input().split())
s=(m+n+k)/2
a=sqrt(s*(s-m)*(s-n)*(s-k))
a="{:.2f}".format(a)
print(a)
