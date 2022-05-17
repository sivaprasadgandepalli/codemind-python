m,n=map(int,input().split())
d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
s=[]
for i in d1:
    if i not in d2:
        s.append(i)
for i in d2:
    if i not in d1:
        s.append(i)
print(*s)