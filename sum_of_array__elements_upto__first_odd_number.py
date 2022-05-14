n=int(input())
d=list(map(int,input().split()))
s=0
for i in range(0,len(d)):
    if d[i]%2==0:
        s+=d[i]
    else:
        break
print(s)