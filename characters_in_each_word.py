def count(n):
    c=0
    n=list(n)
    for i in n:
        if i==' ':
            c=c
        else:
            c+=1
    return c
n=input()
d=n.split()
s=[]
for i in d:
    k=count(i)
    if k!=0:
        s.append(k)
print(*s)
        
        