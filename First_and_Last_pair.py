n=int(input())
d=list(map(int,input().split()))
l=len(d)
s=[]
k=0
c=-1
if n%2:
    while k<n:
        s.append(d[k])
        if k==(l//2):
            break
        s.append(d[c])
        k+=1
        c-=1
else:
    while k<n:
        if k==l//2:
            break
        s.append(d[k])
        s.append(d[c])
        k+=1
        c-=1
if n%2==0:
    print(*s)
else:
    s.append(0)
    print(*s)
