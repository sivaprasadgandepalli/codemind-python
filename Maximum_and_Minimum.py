n=int(input())
d=list(map(int,input().split()))
s=[]
h=0
for i in d:
    c=d.count(i)
    if c==i:
        h=1
        if i not in s:
            s.append(i)
if h==1:
    print(min(s),max(s))
else:
    print(-1)
    
