import math
m,n=map(int,input().split())
mx=max(m,n)
mn=min(m,n)
for i in range(1,mn+1):
    if(mx%i==0 and mn%i==0):
        hcf=i
print(hcf)