import math
m,n=map(int,input().split())
l=int(math.log10(m)+1)
f=m//10**(l-n)
l=m%10**n
print(abs(l-f))