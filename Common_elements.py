def unique(d):
    s=[]
    for i in range(0,len(d)):
        if d[i] not in s:
            s.append(d[i])
    return s
n,m=map(int,input().split())
d1=list(map(int,input().strip().split()))
d2=list(map(int,input().strip().split()))
r1=unique(d1)
r2=unique(d2)
c=[]
for i in range(0,len(r1)):
    if r1[i] in r2:
        c.append(r1[i])
print(*c)
