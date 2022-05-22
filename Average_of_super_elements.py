n=int(input())
d=list(map(int,input().split()))
s=[]
h=0
c1=0
for i in d:
    c=d.count(i)
    if i==c:
        h=1
        if i not in s:
            s.append(i)
            c1+=1
if h==1:
    avg=sum(s)/c1
    avg=format(avg,".2f")
    print(avg)
else:
    print(-1)