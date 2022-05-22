n=int(input())
d=list(map(int,input().split()))
count=0
s=[]
for i in d:
    c=d.count(i)
    if c==i:
        if i not in s:
            s.append(i)
            count+=1
print(count)
    
