n=int(input())
d=list(map(int,input().split()))
c=0
m=len(str(max(d)))
for i in d:
    l=len(str(i))
    if m==l:
        c+=1
print(c)
    