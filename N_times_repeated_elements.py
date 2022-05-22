n=input()
d=list(map(str,input().split()))
k=int(input())
s=[]
h=0
for i in d:
    c=d.count(i)
    if c==k:
        h=1
        if i not in s:
            s.append(i)
if h==1:
    print(*s)
else:
    print(-1)
        
