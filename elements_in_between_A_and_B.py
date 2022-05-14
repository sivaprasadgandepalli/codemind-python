n=int(input())
d=list(map(int,input().split()))
s=[]
h=0
a,b=map(int,input().split())
for i in range(0,len(d)):
    if a<=d[i]<=b:
        s.append(d[i])
        h=1
if h==1:
    print(*s)
else:
    print(-1)