m,n=map(int,input().split())
d=list(map(int,input().split()))
c=0
for i in range(0,len(d)):
    if d[i]%n==0:
        c+=1
print(c)
        